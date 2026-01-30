#!/usr/bin/env python3
"""
Web Crawler - Pencari URL berdasarkan Kata Kunci
=================================================
Script ini melakukan crawling di internet untuk mencari halaman web
yang berhubungan dengan kata kunci yang diberikan.

Fitur:
- Mencari berdasarkan kata kunci
- Membatasi jumlah hasil
- Menyimpan hasil ke file text
- Menampilkan hasil di terminal

Author: Claude AI Assistant
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus, urljoin, urlparse
import time
import re
from datetime import datetime
import argparse
import sys


class WebCrawler:
    """Kelas untuk melakukan web crawling berdasarkan kata kunci."""
    
    def __init__(self, max_results=5, delay=1.0):
        """
        Inisialisasi WebCrawler.
        
        Args:
            max_results (int): Jumlah maksimal hasil yang dicari
            delay (float): Jeda antar request dalam detik
        """
        self.max_results = max_results
        self.delay = delay
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        self.results = []
    
    def search_duckduckgo(self, keyword):
        """
        Mencari menggunakan DuckDuckGo HTML.
        
        Args:
            keyword (str): Kata kunci pencarian
            
        Returns:
            list: Daftar URL yang ditemukan
        """
        print(f"\n🔍 Mencari: '{keyword}'")
        print(f"📊 Maksimal hasil: {self.max_results}")
        print("-" * 50)
        
        urls = []
        encoded_keyword = quote_plus(keyword)
        search_url = f"https://html.duckduckgo.com/html/?q={encoded_keyword}"
        
        try:
            response = requests.get(search_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Cari hasil pencarian dari DuckDuckGo
            results = soup.find_all('a', class_='result__a')
            
            for result in results:
                if len(urls) >= self.max_results:
                    break
                    
                href = result.get('href', '')
                
                # Filter URL yang valid
                if href and href.startswith(('http://', 'https://')):
                    # Bersihkan URL dari tracking
                    clean_url = self._clean_url(href)
                    if clean_url and clean_url not in urls:
                        urls.append(clean_url)
                        title = result.get_text(strip=True)
                        print(f"✅ [{len(urls)}] {title[:60]}...")
                        print(f"   🔗 {clean_url}")
                        
                time.sleep(self.delay * 0.5)
                
        except requests.RequestException as e:
            print(f"❌ Error saat mengakses DuckDuckGo: {e}")
        
        return urls
    
    def search_bing(self, keyword):
        """
        Mencari menggunakan Bing.
        
        Args:
            keyword (str): Kata kunci pencarian
            
        Returns:
            list: Daftar URL yang ditemukan
        """
        print(f"\n🔍 Mencari di Bing: '{keyword}'")
        print(f"📊 Maksimal hasil: {self.max_results}")
        print("-" * 50)
        
        urls = []
        encoded_keyword = quote_plus(keyword)
        search_url = f"https://www.bing.com/search?q={encoded_keyword}"
        
        try:
            response = requests.get(search_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Cari hasil pencarian dari Bing
            results = soup.find_all('li', class_='b_algo')
            
            for result in results:
                if len(urls) >= self.max_results:
                    break
                
                link = result.find('a')
                if link:
                    href = link.get('href', '')
                    
                    if href and href.startswith(('http://', 'https://')):
                        if href not in urls:
                            urls.append(href)
                            title = link.get_text(strip=True)
                            print(f"✅ [{len(urls)}] {title[:60]}...")
                            print(f"   🔗 {href}")
                
                time.sleep(self.delay * 0.5)
                
        except requests.RequestException as e:
            print(f"❌ Error saat mengakses Bing: {e}")
        
        return urls
    
    def _clean_url(self, url):
        """
        Membersihkan URL dari parameter tracking.
        
        Args:
            url (str): URL yang akan dibersihkan
            
        Returns:
            str: URL yang sudah bersih
        """
        try:
            # Parse URL
            parsed = urlparse(url)
            
            # Daftar domain yang tidak diinginkan
            skip_domains = ['duckduckgo.com', 'bing.com', 'google.com', 'yahoo.com']
            
            if any(domain in parsed.netloc for domain in skip_domains):
                return None
            
            # Kembalikan URL dasar tanpa parameter tracking
            clean = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            return clean.rstrip('/')
            
        except Exception:
            return url
    
    def crawl(self, keyword, search_engine='duckduckgo'):
        """
        Melakukan crawling berdasarkan kata kunci.
        
        Args:
            keyword (str): Kata kunci pencarian
            search_engine (str): Mesin pencari yang digunakan ('duckduckgo' atau 'bing')
            
        Returns:
            list: Daftar URL yang ditemukan
        """
        self.results = []
        
        if search_engine.lower() == 'bing':
            self.results = self.search_bing(keyword)
        else:
            self.results = self.search_duckduckgo(keyword)
        
        # Jika hasil kurang, coba mesin pencari lain
        if len(self.results) < self.max_results:
            print(f"\n⚠️ Hasil kurang dari {self.max_results}, mencoba mesin pencari lain...")
            remaining = self.max_results - len(self.results)
            
            if search_engine.lower() == 'duckduckgo':
                additional = self.search_bing(keyword)
            else:
                additional = self.search_duckduckgo(keyword)
            
            for url in additional:
                if url not in self.results and len(self.results) < self.max_results:
                    self.results.append(url)
        
        return self.results
    
    def save_results(self, filename=None, keyword=""):
        """
        Menyimpan hasil crawling ke file text.
        
        Args:
            filename (str): Nama file output (opsional)
            keyword (str): Kata kunci yang dicari
            
        Returns:
            str: Path file yang disimpan
        """
        if not self.results:
            print("\n⚠️ Tidak ada hasil untuk disimpan.")
            return None
        
        if not filename:
            # Buat nama file berdasarkan timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_keyword = re.sub(r'[^\w\s-]', '', keyword)[:30].strip().replace(' ', '_')
            filename = f"hasil_crawling_{safe_keyword}_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("HASIL WEB CRAWLING\n")
                f.write("=" * 60 + "\n\n")
                f.write(f"Kata Kunci  : {keyword}\n")
                f.write(f"Jumlah Hasil: {len(self.results)}\n")
                f.write(f"Waktu       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("\n" + "-" * 60 + "\n")
                f.write("DAFTAR URL:\n")
                f.write("-" * 60 + "\n\n")
                
                for i, url in enumerate(self.results, 1):
                    f.write(f"[{i}] {url}\n")
                
                f.write("\n" + "=" * 60 + "\n")
                f.write("Dihasilkan oleh Web Crawler Python\n")
                f.write("=" * 60 + "\n")
            
            print(f"\n💾 Hasil disimpan ke: {filename}")
            return filename
            
        except IOError as e:
            print(f"❌ Error saat menyimpan file: {e}")
            return None
    
    def display_summary(self, keyword):
        """
        Menampilkan ringkasan hasil crawling.
        
        Args:
            keyword (str): Kata kunci yang dicari
        """
        print("\n" + "=" * 60)
        print("📋 RINGKASAN HASIL CRAWLING")
        print("=" * 60)
        print(f"🔑 Kata Kunci  : {keyword}")
        print(f"📊 Jumlah URL  : {len(self.results)}")
        print(f"⏰ Waktu       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)
        
        if self.results:
            print("\n📄 DAFTAR URL YANG DITEMUKAN:\n")
            for i, url in enumerate(self.results, 1):
                print(f"  [{i}] {url}")
        else:
            print("\n⚠️ Tidak ada URL yang ditemukan.")
        
        print("\n" + "=" * 60)


def main():
    """Fungsi utama untuk menjalankan web crawler."""
    
    # Setup argument parser
    parser = argparse.ArgumentParser(
        description='Web Crawler - Pencari URL berdasarkan Kata Kunci',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:
  python web_crawler.py -k "pemrograman python untuk pemula" -m 5
  python web_crawler.py --keyword "tutorial machine learning" --max 10
  python web_crawler.py -k "belajar coding" -m 3 -o hasil.txt
        """
    )
    
    parser.add_argument(
        '-k', '--keyword',
        type=str,
        help='Kata kunci pencarian'
    )
    
    parser.add_argument(
        '-m', '--max',
        type=int,
        default=5,
        help='Jumlah maksimal hasil (default: 5)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Nama file output (opsional)'
    )
    
    parser.add_argument(
        '-e', '--engine',
        type=str,
        choices=['duckduckgo', 'bing'],
        default='duckduckgo',
        help='Mesin pencari yang digunakan (default: duckduckgo)'
    )
    
    parser.add_argument(
        '-d', '--delay',
        type=float,
        default=1.0,
        help='Jeda antar request dalam detik (default: 1.0)'
    )
    
    args = parser.parse_args()
    
    # Header aplikasi
    print("\n" + "=" * 60)
    print("🌐 WEB CRAWLER - PENCARI URL BERDASARKAN KATA KUNCI")
    print("=" * 60)
    
    # Jika tidak ada argumen, gunakan mode interaktif
    if not args.keyword:
        print("\n📝 Mode Interaktif")
        print("-" * 40)
        
        keyword = input("🔑 Masukkan kata kunci pencarian: ").strip()
        if not keyword:
            print("❌ Kata kunci tidak boleh kosong!")
            sys.exit(1)
        
        try:
            max_results = input("📊 Jumlah maksimal hasil [5]: ").strip()
            max_results = int(max_results) if max_results else 5
        except ValueError:
            max_results = 5
        
        output_file = input("💾 Nama file output (kosongkan untuk otomatis): ").strip()
        output_file = output_file if output_file else None
        
        search_engine = 'duckduckgo'
        delay = 1.0
    else:
        keyword = args.keyword
        max_results = args.max
        output_file = args.output
        search_engine = args.engine
        delay = args.delay
    
    # Validasi
    if max_results < 1:
        print("❌ Jumlah hasil minimal adalah 1!")
        sys.exit(1)
    
    if max_results > 50:
        print("⚠️ Jumlah hasil dibatasi maksimal 50.")
        max_results = 50
    
    # Inisialisasi crawler
    crawler = WebCrawler(max_results=max_results, delay=delay)
    
    # Mulai crawling
    print(f"\n🚀 Memulai crawling dengan mesin pencari: {search_engine}")
    
    try:
        results = crawler.crawl(keyword, search_engine=search_engine)
        
        # Tampilkan ringkasan
        crawler.display_summary(keyword)
        
        # Simpan hasil
        if results:
            saved_file = crawler.save_results(filename=output_file, keyword=keyword)
            
            if saved_file:
                print(f"\n✅ Crawling selesai! {len(results)} URL berhasil ditemukan.")
        else:
            print("\n⚠️ Tidak ada hasil yang ditemukan untuk kata kunci tersebut.")
            print("💡 Tips: Coba gunakan kata kunci yang lebih umum atau berbeda.")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Crawling dibatalkan oleh pengguna.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
