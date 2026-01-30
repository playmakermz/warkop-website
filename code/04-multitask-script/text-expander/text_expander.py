#!/usr/bin/env python3
"""
Text Expander - Mengembangkan kalimat menjadi paragraf berdasarkan dokumen
Menggunakan Markov Chain dan N-gram Language Model (tanpa AI/LLM)

Author: Claude
"""

import re
import random
import string
from collections import defaultdict, Counter
from pathlib import Path
import math


class DocumentProcessor:
    """Memproses dan membersihkan dokumen markdown"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.raw_text = ""
        self.sentences = []
        self.words = []
        self.paragraphs = []
        
    def load_document(self) -> str:
        """Membaca file markdown"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.raw_text = f.read()
        return self.raw_text
    
    def clean_markdown(self, text: str) -> str:
        """Membersihkan syntax markdown"""
        # Hapus headers markdown
        text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
        # Hapus bold/italic
        text = re.sub(r'\*{1,3}(.*?)\*{1,3}', r'\1', text)
        text = re.sub(r'_{1,3}(.*?)_{1,3}', r'\1', text)
        # Hapus links
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        # Hapus images
        text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', text)
        # Hapus code blocks
        text = re.sub(r'```[\s\S]*?```', '', text)
        text = re.sub(r'`([^`]+)`', r'\1', text)
        # Hapus horizontal rules
        text = re.sub(r'^[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)
        # Hapus blockquotes
        text = re.sub(r'^>\s+', '', text, flags=re.MULTILINE)
        # Hapus list markers
        text = re.sub(r'^[\s]*[-*+]\s+', '', text, flags=re.MULTILINE)
        text = re.sub(r'^[\s]*\d+\.\s+', '', text, flags=re.MULTILINE)
        
        return text
    
    def extract_sentences(self, text: str) -> list:
        """Ekstrak kalimat dari teks"""
        # Split berdasarkan tanda baca akhir kalimat
        sentences = re.split(r'(?<=[.!?])\s+', text)
        # Bersihkan dan filter kalimat kosong
        sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 10]
        return sentences
    
    def extract_words(self, text: str) -> list:
        """Ekstrak kata-kata dari teks"""
        # Lowercase dan ekstrak kata
        words = re.findall(r'\b[a-zA-Z\u00C0-\u024F]+\b', text.lower())
        return words
    
    def extract_paragraphs(self, text: str) -> list:
        """Ekstrak paragraf dari teks"""
        paragraphs = re.split(r'\n\s*\n', text)
        paragraphs = [p.strip() for p in paragraphs if p.strip() and len(p.strip()) > 50]
        return paragraphs
    
    def process(self) -> dict:
        """Proses dokumen lengkap"""
        self.load_document()
        cleaned = self.clean_markdown(self.raw_text)
        
        self.sentences = self.extract_sentences(cleaned)
        self.words = self.extract_words(cleaned)
        self.paragraphs = self.extract_paragraphs(cleaned)
        
        return {
            'sentences': self.sentences,
            'words': self.words,
            'paragraphs': self.paragraphs,
            'word_count': len(self.words),
            'sentence_count': len(self.sentences),
            'unique_words': len(set(self.words))
        }


class MarkovChain:
    """Markov Chain untuk text generation"""
    
    def __init__(self, order: int = 2):
        self.order = order  # N-gram order
        self.chain = defaultdict(list)
        self.starters = []  # Kata-kata pembuka kalimat
        
    def train(self, sentences: list):
        """Melatih model dari kalimat-kalimat"""
        for sentence in sentences:
            words = sentence.split()
            if len(words) < self.order + 1:
                continue
            
            # Simpan starter (kata awal kalimat)
            starter = tuple(words[:self.order])
            self.starters.append(starter)
            
            # Bangun chain
            for i in range(len(words) - self.order):
                key = tuple(words[i:i + self.order])
                next_word = words[i + self.order]
                self.chain[key].append(next_word)
    
    def generate(self, seed_words: list = None, max_words: int = 50) -> str:
        """Generate teks dari seed words"""
        if seed_words and len(seed_words) >= self.order:
            # Cari key yang cocok dengan seed
            current = self._find_matching_key(seed_words)
        else:
            # Gunakan random starter
            if not self.starters:
                return ""
            current = random.choice(self.starters)
        
        result = list(current)
        
        for _ in range(max_words - self.order):
            if current not in self.chain:
                # Coba cari key yang mirip
                current = self._find_similar_key(current)
                if not current:
                    break
            
            next_words = self.chain[current]
            if not next_words:
                break
                
            next_word = random.choice(next_words)
            result.append(next_word)
            current = tuple(result[-self.order:])
            
            # Berhenti jika menemukan tanda akhir kalimat
            if next_word.endswith(('.', '!', '?')):
                break
        
        return ' '.join(result)
    
    def _find_matching_key(self, words: list) -> tuple:
        """Cari key yang cocok dengan kata-kata"""
        words_lower = [w.lower() for w in words]
        
        # Coba exact match
        for i in range(len(words_lower) - self.order + 1):
            key = tuple(words_lower[i:i + self.order])
            if key in self.chain:
                return key
        
        # Coba partial match
        for key in self.chain.keys():
            key_lower = tuple(w.lower() for w in key)
            if any(w in key_lower for w in words_lower):
                return key
        
        # Fallback ke random starter
        return random.choice(self.starters) if self.starters else None
    
    def _find_similar_key(self, current: tuple) -> tuple:
        """Cari key yang mirip"""
        current_lower = tuple(w.lower() for w in current)
        
        for key in self.chain.keys():
            key_lower = tuple(w.lower() for w in key)
            # Cek jika ada kata yang sama
            if any(w in current_lower for w in key_lower):
                return key
        
        return random.choice(self.starters) if self.starters else None


class SimilarityFinder:
    """Mencari kalimat/paragraf yang mirip dengan input"""
    
    def __init__(self, sentences: list, paragraphs: list):
        self.sentences = sentences
        self.paragraphs = paragraphs
        self.word_idf = {}  # Inverse Document Frequency
        self._calculate_idf()
    
    def _calculate_idf(self):
        """Hitung IDF untuk setiap kata"""
        doc_count = len(self.sentences)
        word_doc_count = defaultdict(int)
        
        for sentence in self.sentences:
            words = set(re.findall(r'\b[a-zA-Z\u00C0-\u024F]+\b', sentence.lower()))
            for word in words:
                word_doc_count[word] += 1
        
        for word, count in word_doc_count.items():
            self.word_idf[word] = math.log(doc_count / (1 + count))
    
    def _get_tfidf_vector(self, text: str) -> dict:
        """Dapatkan TF-IDF vector untuk teks"""
        words = re.findall(r'\b[a-zA-Z\u00C0-\u024F]+\b', text.lower())
        word_count = Counter(words)
        total_words = len(words)
        
        vector = {}
        for word, count in word_count.items():
            tf = count / total_words if total_words > 0 else 0
            idf = self.word_idf.get(word, 0)
            vector[word] = tf * idf
        
        return vector
    
    def _cosine_similarity(self, vec1: dict, vec2: dict) -> float:
        """Hitung cosine similarity antara dua vector"""
        common_words = set(vec1.keys()) & set(vec2.keys())
        
        if not common_words:
            return 0.0
        
        dot_product = sum(vec1[w] * vec2[w] for w in common_words)
        norm1 = math.sqrt(sum(v ** 2 for v in vec1.values()))
        norm2 = math.sqrt(sum(v ** 2 for v in vec2.values()))
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)
    
    def find_similar_sentences(self, query: str, top_n: int = 5) -> list:
        """Cari kalimat yang paling mirip dengan query"""
        query_vec = self._get_tfidf_vector(query)
        
        similarities = []
        for sentence in self.sentences:
            sent_vec = self._get_tfidf_vector(sentence)
            sim = self._cosine_similarity(query_vec, sent_vec)
            similarities.append((sentence, sim))
        
        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_n]
    
    def find_similar_paragraphs(self, query: str, top_n: int = 3) -> list:
        """Cari paragraf yang paling mirip dengan query"""
        query_vec = self._get_tfidf_vector(query)
        
        similarities = []
        for paragraph in self.paragraphs:
            para_vec = self._get_tfidf_vector(paragraph)
            sim = self._cosine_similarity(query_vec, para_vec)
            similarities.append((paragraph, sim))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_n]


class TextExpander:
    """Kelas utama untuk mengembangkan kalimat menjadi paragraf"""
    
    def __init__(self, document_path: str):
        self.document_path = document_path
        self.processor = None
        self.markov = None
        self.similarity = None
        self.data = None
        
    def initialize(self):
        """Inisialisasi semua komponen"""
        print(f"📖 Memuat dokumen: {self.document_path}")
        
        # Proses dokumen
        self.processor = DocumentProcessor(self.document_path)
        self.data = self.processor.process()
        
        print(f"   ✓ {self.data['sentence_count']} kalimat ditemukan")
        print(f"   ✓ {self.data['word_count']} kata total")
        print(f"   ✓ {self.data['unique_words']} kata unik")
        print(f"   ✓ {len(self.data['paragraphs'])} paragraf")
        
        # Inisialisasi Markov Chain
        print("\n🔗 Membangun Markov Chain...")
        self.markov = MarkovChain(order=2)
        self.markov.train(self.data['sentences'])
        print(f"   ✓ Model dilatih dengan {len(self.markov.chain)} transisi")
        
        # Inisialisasi Similarity Finder
        print("\n🔍 Membangun indeks kesamaan...")
        self.similarity = SimilarityFinder(
            self.data['sentences'], 
            self.data['paragraphs']
        )
        print(f"   ✓ IDF dihitung untuk {len(self.similarity.word_idf)} kata")
        
        print("\n✅ Sistem siap!\n")
    
    def expand(self, input_sentence: str, method: str = 'hybrid', 
               num_sentences: int = 4) -> str:
        """
        Mengembangkan kalimat input menjadi paragraf
        
        Args:
            input_sentence: Kalimat input
            method: Metode yang digunakan ('markov', 'similarity', 'hybrid')
            num_sentences: Jumlah kalimat dalam output
            
        Returns:
            Paragraf hasil ekspansi
        """
        if method == 'markov':
            return self._expand_markov(input_sentence, num_sentences)
        elif method == 'similarity':
            return self._expand_similarity(input_sentence, num_sentences)
        else:  # hybrid
            return self._expand_hybrid(input_sentence, num_sentences)
    
    def _expand_markov(self, input_sentence: str, num_sentences: int) -> str:
        """Ekspansi menggunakan Markov Chain murni"""
        words = input_sentence.split()
        sentences = [input_sentence]
        used_content = set()
        used_content.add(input_sentence.lower().strip())
        
        attempts = 0
        max_attempts = num_sentences * 8
        
        while len(sentences) < num_sentences and attempts < max_attempts:
            attempts += 1
            
            # Variasi seed untuk diversitas
            if attempts % 2 == 0 and len(sentences) > 1:
                # Gunakan kata dari kalimat random sebelumnya
                random_sent = random.choice(sentences)
                words = random_sent.split()[-3:]
            else:
                # Gunakan kata terakhir dari kalimat terakhir
                words = sentences[-1].split()[-2:]
            
            generated = self.markov.generate(words, max_words=35)
            
            if generated:
                normalized = generated.lower().strip()
                
                # Cek duplikasi
                is_duplicate = False
                for used in used_content:
                    gen_words = set(normalized.split())
                    used_words = set(used.split())
                    if gen_words and used_words:
                        overlap = len(gen_words & used_words) / min(len(gen_words), len(used_words))
                        if overlap > 0.6:
                            is_duplicate = True
                            break
                
                if not is_duplicate and len(generated.split()) > 4:
                    sentences.append(generated)
                    used_content.add(normalized)
        
        return ' '.join(sentences)
    
    def _expand_similarity(self, input_sentence: str, num_sentences: int) -> str:
        """Ekspansi menggunakan pencarian kesamaan"""
        # Cari kalimat yang mirip
        similar = self.similarity.find_similar_sentences(input_sentence, num_sentences * 2)
        
        # Pilih kalimat yang tidak terlalu mirip satu sama lain
        result = [input_sentence]
        used_words = set(input_sentence.lower().split())
        
        for sentence, score in similar:
            if len(result) >= num_sentences:
                break
            
            # Hindari duplikasi
            sent_words = set(sentence.lower().split())
            overlap = len(used_words & sent_words) / len(sent_words) if sent_words else 1
            
            if overlap < 0.7 and score > 0.1:  # Tidak terlalu mirip tapi relevan
                result.append(sentence)
                used_words.update(sent_words)
        
        return ' '.join(result)
    
    def _expand_hybrid(self, input_sentence: str, num_sentences: int) -> str:
        """Ekspansi menggunakan kombinasi Markov dan Similarity"""
        result = [input_sentence]
        used_content = set()
        used_content.add(input_sentence.lower().strip())
        
        # Cari paragraf dan kalimat yang relevan untuk konteks
        similar_paras = self.similarity.find_similar_paragraphs(input_sentence, 3)
        similar_sents = self.similarity.find_similar_sentences(input_sentence, num_sentences * 3)
        
        # Kumpulkan kalimat kandidat dari similarity
        candidate_sentences = []
        for sent, score in similar_sents:
            normalized = sent.lower().strip()
            if normalized not in used_content and score > 0.05:
                candidate_sentences.append((sent, score))
        
        # Gunakan kata-kata dari paragraf relevan sebagai seed tambahan
        context_words = []
        for para, _ in similar_paras:
            words = re.findall(r'\b[a-zA-Z\u00C0-\u024F]+\b', para.lower())
            context_words.extend(words[:30])
        
        # Generate kalimat dengan kombinasi Markov dan Similarity
        attempts = 0
        max_attempts = num_sentences * 5
        
        while len(result) < num_sentences and attempts < max_attempts:
            attempts += 1
            generated = None
            
            # Alternatif antara Markov dan Similarity
            if attempts % 3 != 0:
                # Gunakan Markov dengan seed dari konteks
                if context_words:
                    idx = random.randint(0, max(0, len(context_words) - 3))
                    temp_seed = context_words[idx:idx + 2]
                else:
                    temp_seed = result[-1].split()[-3:]
                
                generated = self.markov.generate(temp_seed, max_words=30)
            else:
                # Ambil dari kandidat similarity
                if candidate_sentences:
                    generated, _ = candidate_sentences.pop(0)
            
            # Validasi dan tambahkan
            if generated:
                normalized = generated.lower().strip()
                # Cek duplikasi dengan fuzzy matching
                is_duplicate = False
                for used in used_content:
                    # Hitung overlap kata
                    gen_words = set(normalized.split())
                    used_words = set(used.split())
                    if gen_words and used_words:
                        overlap = len(gen_words & used_words) / min(len(gen_words), len(used_words))
                        if overlap > 0.7:  # Terlalu mirip
                            is_duplicate = True
                            break
                
                if not is_duplicate and len(generated.split()) > 3:
                    result.append(generated)
                    used_content.add(normalized)
        
        # Jika masih kurang, paksa tambahkan dari similarity
        while len(result) < num_sentences and candidate_sentences:
            sent, _ = candidate_sentences.pop(0)
            if sent.lower().strip() not in used_content:
                result.append(sent)
                used_content.add(sent.lower().strip())
        
        return ' '.join(result)
    
    def analyze_input(self, input_sentence: str) -> dict:
        """Analisis input dan tampilkan informasi"""
        words = re.findall(r'\b[a-zA-Z\u00C0-\u024F]+\b', input_sentence.lower())
        
        # Cari kata yang ada di dokumen
        doc_words = set(self.data['words'])
        matching_words = [w for w in words if w in doc_words]
        
        # Cari kalimat serupa
        similar = self.similarity.find_similar_sentences(input_sentence, 3)
        
        return {
            'input_words': len(words),
            'matching_words': matching_words,
            'match_ratio': len(matching_words) / len(words) if words else 0,
            'similar_sentences': similar
        }


def interactive_mode(expander: TextExpander):
    """Mode interaktif untuk pengguna"""
    print("=" * 60)
    print("📝 TEXT EXPANDER - Mode Interaktif")
    print("=" * 60)
    print("\nPerintah:")
    print("  - Ketik kalimat untuk mengembangkannya")
    print("  - 'analyze <kalimat>' - Analisis kalimat")
    print("  - 'method <markov|similarity|hybrid>' - Ubah metode")
    print("  - 'sentences <n>' - Ubah jumlah kalimat output")
    print("  - 'help' - Tampilkan bantuan")
    print("  - 'quit' atau 'exit' - Keluar")
    print("-" * 60)
    
    current_method = 'hybrid'
    num_sentences = 4
    
    while True:
        try:
            user_input = input("\n🖊️  Input: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Sampai jumpa!")
                break
            
            if user_input.lower() == 'help':
                print("\n📚 Bantuan:")
                print("  - Ketik kalimat apapun untuk mengembangkannya")
                print("  - Metode tersedia: markov, similarity, hybrid")
                print("  - Jumlah kalimat output: 2-10")
                continue
            
            if user_input.lower().startswith('method '):
                method = user_input[7:].strip().lower()
                if method in ['markov', 'similarity', 'hybrid']:
                    current_method = method
                    print(f"   ✓ Metode diubah ke: {method}")
                else:
                    print("   ✗ Metode tidak valid. Gunakan: markov, similarity, hybrid")
                continue
            
            if user_input.lower().startswith('sentences '):
                try:
                    n = int(user_input[10:].strip())
                    if 2 <= n <= 10:
                        num_sentences = n
                        print(f"   ✓ Jumlah kalimat diubah ke: {n}")
                    else:
                        print("   ✗ Jumlah harus antara 2-10")
                except ValueError:
                    print("   ✗ Masukkan angka yang valid")
                continue
            
            if user_input.lower().startswith('analyze '):
                query = user_input[8:].strip()
                analysis = expander.analyze_input(query)
                print(f"\n📊 Analisis:")
                print(f"   Jumlah kata: {analysis['input_words']}")
                print(f"   Kata cocok: {len(analysis['matching_words'])} ({analysis['match_ratio']:.1%})")
                print(f"   Kata yang ditemukan: {', '.join(analysis['matching_words'][:10])}")
                print(f"\n   Kalimat serupa:")
                for sent, score in analysis['similar_sentences']:
                    print(f"   [{score:.3f}] {sent[:80]}...")
                continue
            
            # Ekspansi kalimat
            print(f"\n⚙️  Memproses dengan metode '{current_method}'...")
            result = expander.expand(user_input, method=current_method, 
                                    num_sentences=num_sentences)
            
            print(f"\n📄 Output ({num_sentences} kalimat):")
            print("-" * 60)
            # Format output sebagai paragraf
            words = result.split()
            lines = []
            current_line = []
            for word in words:
                current_line.append(word)
                if len(' '.join(current_line)) > 70:
                    lines.append(' '.join(current_line))
                    current_line = []
            if current_line:
                lines.append(' '.join(current_line))
            print('\n'.join(lines))
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\n👋 Sampai jumpa!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


def main():
    """Fungsi utama"""
    import sys
    
    # Cari file markdown di direktori yang sama
    script_dir = Path(__file__).parent
    md_files = list(script_dir.glob("*.md"))
    
    # Filter: abaikan README.md dan file sistem lainnya
    ignored_files = {'readme.md', 'changelog.md', 'license.md', 'contributing.md'}
    md_files = [f for f in md_files if f.name.lower() not in ignored_files]
    
    if not md_files:
        print("❌ Tidak ada file markdown (.md) ditemukan!")
        print(f"   Letakkan file markdown di: {script_dir}")
        
        # Buat contoh file untuk demo
        sample_file = script_dir / "sample_document.md"
        print(f"\n📝 Membuat file contoh: {sample_file}")
        
        sample_content = """# Chapter 1: Pagi yang Cerah

Matahari terbit dengan indahnya di ufuk timur. Burung-burung berkicau merdu menyambut datangnya hari baru. Embun pagi masih menghiasi dedaunan yang hijau.

Di sebuah desa kecil, seorang pemuda bernama Arya sedang bersiap untuk memulai petualangannya. Dia mengenakan jubah biru tua dan membawa tas kulit berisi perbekalan.

"Hari ini adalah permulaan dari segalanya," gumamnya sambil menatap langit. Hatinya dipenuhi harapan dan semangat yang membara.

# Chapter 2: Perjalanan Dimulai

Arya berjalan melewati hutan yang lebat. Pohon-pohon tinggi menjulang ke langit, menciptakan kanopi yang menyejukkan. Sinar matahari menerobos celah-celah dedaunan.

Di tengah perjalanan, ia bertemu dengan seorang pedagang tua. Pedagang itu memiliki rambut putih dan mata yang bijaksana. Dia menawarkan air minum kepada Arya.

"Kau tampak seperti seorang petualang muda," kata pedagang itu. "Kemana tujuanmu?"

Arya menjawab dengan penuh keyakinan. "Aku mencari harta karun yang tersembunyi di pegunungan utara. Legenda mengatakan bahwa harta itu dijaga oleh naga."

Pedagang itu tersenyum dan mengangguk. "Berhati-hatilah, anak muda. Perjalanan ke utara penuh dengan bahaya."

# Chapter 3: Tantangan Pertama

Setelah berhari-hari berjalan, Arya tiba di sebuah jurang yang dalam. Jembatan gantung tua menjadi satu-satunya jalan untuk menyeberang. Angin bertiup kencang, membuat jembatan itu berayun.

Dengan keberanian, Arya melangkahkan kakinya ke jembatan. Setiap langkah terasa berat dan menegangkan. Papan-papan kayu berderit di bawah kakinya.

Di tengah jembatan, seekor elang besar terbang di atasnya. Sayapnya yang lebar menghalangi cahaya matahari untuk sesaat. Arya terpesona oleh keindahan burung tersebut.

Akhirnya, ia berhasil menyeberangi jurang. Di sisi lain, pemandangan yang menakjubkan menyambutnya. Padang rumput hijau membentang sejauh mata memandang.

# Chapter 4: Pertemuan Tak Terduga

Di padang rumput, Arya bertemu dengan sekelompok pengelana. Mereka duduk mengelilingi api unggun, menikmati makan malam. Aroma masakan yang harum menggelitik hidung Arya.

"Bergabunglah dengan kami," ajak seorang wanita berambut merah. Namanya adalah Maya, pemimpin kelompok pengelana tersebut.

Arya duduk bersama mereka dan berbagi cerita. Ternyata, mereka juga sedang mencari harta karun yang sama. Namun tujuan mereka berbeda.

"Kami tidak menginginkan harta," jelas Maya. "Kami mencari pengetahuan kuno yang tersimpan di sana."

Malam itu, mereka memutuskan untuk melanjutkan perjalanan bersama. Kekuatan dalam kebersamaan akan membantu mereka menghadapi tantangan yang lebih besar.
"""
        
        with open(sample_file, 'w', encoding='utf-8') as f:
            f.write(sample_content)
        
        md_files = [sample_file]
        print("   ✓ File contoh berhasil dibuat")
    
    # Gunakan file markdown pertama yang ditemukan
    document_path = md_files[0]
    print(f"\n📂 Menggunakan dokumen: {document_path.name}")
    
    if len(md_files) > 1:
        print(f"   (File lain yang ditemukan: {[f.name for f in md_files[1:]]})")
    
    # Inisialisasi TextExpander
    expander = TextExpander(str(document_path))
    expander.initialize()
    
    # Jalankan mode interaktif
    interactive_mode(expander)


if __name__ == "__main__":
    main()
