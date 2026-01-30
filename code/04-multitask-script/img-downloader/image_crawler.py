#!/usr/bin/env python3
"""
Image Crawler & Downloader
==========================
Script untuk crawling halaman web dan mendownload semua gambar yang ditemukan.

Fitur:
- Crawling halaman web untuk mencari gambar
- Support berbagai format: jpg, jpeg, png, gif, webp, bmp, svg, ico
- Download gambar dengan resolusi tinggi
- Menyimpan ke folder khusus
- Support untuk situs dengan proteksi (seperti Pixiv)
- Progress tracking dan logging

Penggunaan:
    python image_crawler.py

Author: Claude AI Assistant
"""

import os
import re
import sys
import time
import hashlib
import argparse
import mimetypes
from urllib.parse import urljoin, urlparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Set, List, Optional, Tuple

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("=" * 60)
    print("Library yang diperlukan belum terinstall!")
    print("Jalankan perintah berikut untuk menginstall:")
    print("  pip install requests beautifulsoup4 lxml")
    print("=" * 60)
    sys.exit(1)


# ============================================================================
# KONFIGURASI
# ============================================================================

# Format gambar yang didukung
IMAGE_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.webp', 
    '.bmp', '.svg', '.ico', '.tiff', '.tif'
}

# MIME types untuk gambar
IMAGE_MIMETYPES = {
    'image/jpeg', 'image/png', 'image/gif', 'image/webp',
    'image/bmp', 'image/svg+xml', 'image/x-icon', 'image/tiff'
}

# Default headers untuk request
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Timeout untuk requests (dalam detik)
REQUEST_TIMEOUT = 30

# Delay antara request (dalam detik) - untuk menghindari rate limiting
REQUEST_DELAY = 0.5

# Jumlah maksimum thread untuk download paralel
MAX_WORKERS = 5


# ============================================================================
# KELAS UTAMA
# ============================================================================

class ImageCrawler:
    """Kelas utama untuk crawling dan download gambar dari web."""
    
    def __init__(self, base_url: str, output_dir: str = None, max_depth: int = 1):
        """
        Inisialisasi crawler.
        
        Args:
            base_url: URL halaman yang akan di-crawl
            output_dir: Direktori output untuk menyimpan gambar
            max_depth: Kedalaman maksimum crawling (default: 1)
        """
        self.base_url = base_url
        self.parsed_base = urlparse(base_url)
        self.domain = self.parsed_base.netloc
        self.max_depth = max_depth
        
        # Setup session dengan headers
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        
        # Tambahkan referer berdasarkan domain
        self.session.headers['Referer'] = f"{self.parsed_base.scheme}://{self.domain}/"
        
        # Setup output directory
        if output_dir:
            self.output_dir = output_dir
        else:
            # Buat nama folder berdasarkan domain
            safe_domain = re.sub(r'[^\w\-.]', '_', self.domain)
            self.output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"downloaded_images_{safe_domain}")
        
        # Set untuk tracking URL yang sudah diproses
        self.visited_urls: Set[str] = set()
        self.image_urls: Set[str] = set()
        self.downloaded_hashes: Set[str] = set()
        
        # Statistik
        self.stats = {
            'pages_crawled': 0,
            'images_found': 0,
            'images_downloaded': 0,
            'images_skipped': 0,
            'errors': 0
        }
        
        # Site-specific configurations
        self._setup_site_specific()
    
    def _setup_site_specific(self):
        """Setup konfigurasi khusus untuk situs tertentu."""
        
        # Pixiv
        if 'pixiv.net' in self.domain:
            self.session.headers['Referer'] = 'https://www.pixiv.net/'
            print("[INFO] Detected Pixiv - menggunakan konfigurasi khusus")
            print("[INFO] Note: Beberapa gambar mungkin memerlukan login untuk resolusi penuh")
        
        # Twitter/X
        elif 'twitter.com' in self.domain or 'x.com' in self.domain:
            print("[INFO] Detected Twitter/X - menggunakan konfigurasi khusus")
        
        # DeviantArt
        elif 'deviantart.com' in self.domain:
            print("[INFO] Detected DeviantArt - menggunakan konfigurasi khusus")
    
    def _is_valid_image_url(self, url: str) -> bool:
        """Cek apakah URL adalah gambar valid."""
        parsed = urlparse(url)
        path_lower = parsed.path.lower()
        
        # Cek ekstensi file
        for ext in IMAGE_EXTENSIONS:
            if path_lower.endswith(ext):
                return True
        
        # Cek pattern URL gambar umum
        image_patterns = [
            r'/img/', r'/image/', r'/images/', r'/photo/', r'/photos/',
            r'/pic/', r'/pics/', r'/artwork/', r'/uploads/',
            r'\.pximg\.net', r'\.twimg\.com', r'\.imgur\.com'
        ]
        
        for pattern in image_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                return True
        
        return False
    
    def _get_filename_from_url(self, url: str, response: requests.Response = None) -> str:
        """Extract nama file dari URL atau response headers."""
        parsed = urlparse(url)
        path = unquote(parsed.path)
        
        # Ambil nama file dari path
        filename = os.path.basename(path)
        
        # Jika tidak ada nama file, generate dari hash URL
        if not filename or '.' not in filename:
            url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
            
            # Coba tentukan ekstensi dari content-type
            ext = '.jpg'  # Default
            if response:
                content_type = response.headers.get('content-type', '')
                if 'png' in content_type:
                    ext = '.png'
                elif 'gif' in content_type:
                    ext = '.gif'
                elif 'webp' in content_type:
                    ext = '.webp'
            
            filename = f"image_{url_hash}{ext}"
        
        # Bersihkan nama file
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        
        return filename
    
    def _upgrade_to_high_res(self, img_url: str) -> str:
        """Mencoba mengupgrade URL gambar ke resolusi lebih tinggi."""
        
        # Pixiv - upgrade ke resolusi original
        if 'pximg.net' in img_url:
            # c/250x250_80_a2 -> img-original atau img-master
            img_url = re.sub(r'/c/\d+x\d+[^/]*/', '/img-original/', img_url)
            img_url = re.sub(r'_square\d+', '', img_url)
            img_url = re.sub(r'_master\d+', '', img_url)
        
        # Twitter - upgrade ke resolusi original
        elif 'twimg.com' in img_url:
            # Hapus suffix ukuran seperti ?format=jpg&name=small
            img_url = re.sub(r'\?.*$', '', img_url)
            img_url = re.sub(r'&name=\w+', '', img_url)
            if '?' in img_url:
                img_url += '&name=orig'
            else:
                img_url += '?name=orig'
        
        # DeviantArt - upgrade ke resolusi full
        elif 'deviantart.com' in img_url or 'wixmp.com' in img_url:
            # Hapus parameter resize
            img_url = re.sub(r'/v1/fill/.*?/', '/', img_url)
        
        # Imgur - upgrade ke original
        elif 'imgur.com' in img_url:
            # Hapus suffix ukuran (s, m, l, h)
            img_url = re.sub(r'([a-zA-Z0-9]+)[smhl]\.', r'\1.', img_url)
        
        return img_url
    
    def crawl_page(self, url: str, depth: int = 0) -> Set[str]:
        """
        Crawl satu halaman web untuk mencari gambar.
        
        Args:
            url: URL halaman
            depth: Kedalaman crawling saat ini
            
        Returns:
            Set URL gambar yang ditemukan
        """
        if url in self.visited_urls:
            return set()
        
        if depth > self.max_depth:
            return set()
        
        self.visited_urls.add(url)
        found_images: Set[str] = set()
        
        print(f"\n[CRAWL] Depth {depth}: {url}")
        
        try:
            response = self.session.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            self.stats['pages_crawled'] += 1
            
            # Parse HTML
            soup = BeautifulSoup(response.text, 'lxml')
            
            # 1. Cari dari tag <img>
            for img in soup.find_all('img'):
                for attr in ['src', 'data-src', 'data-original', 'data-lazy-src', 'srcset']:
                    img_url = img.get(attr)
                    if img_url:
                        # Handle srcset
                        if attr == 'srcset':
                            # Ambil URL dengan resolusi tertinggi
                            srcset_parts = img_url.split(',')
                            for part in srcset_parts:
                                src = part.strip().split()[0]
                                full_url = urljoin(url, src)
                                found_images.add(self._upgrade_to_high_res(full_url))
                        else:
                            full_url = urljoin(url, img_url)
                            found_images.add(self._upgrade_to_high_res(full_url))
            
            # 2. Cari dari tag <a> yang mengarah ke gambar
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href and self._is_valid_image_url(href):
                    full_url = urljoin(url, href)
                    found_images.add(self._upgrade_to_high_res(full_url))
            
            # 3. Cari dari tag <picture> dan <source>
            for source in soup.find_all(['source', 'picture']):
                for attr in ['src', 'srcset', 'data-srcset']:
                    src = source.get(attr)
                    if src:
                        if 'srcset' in attr:
                            srcset_parts = src.split(',')
                            for part in srcset_parts:
                                src_url = part.strip().split()[0]
                                full_url = urljoin(url, src_url)
                                found_images.add(self._upgrade_to_high_res(full_url))
                        else:
                            full_url = urljoin(url, src)
                            found_images.add(self._upgrade_to_high_res(full_url))
            
            # 4. Cari dari background-image di style
            style_pattern = r'background(?:-image)?\s*:\s*url\(["\']?([^"\')\s]+)["\']?\)'
            for element in soup.find_all(style=True):
                style = element.get('style', '')
                matches = re.findall(style_pattern, style)
                for match in matches:
                    full_url = urljoin(url, match)
                    if self._is_valid_image_url(full_url):
                        found_images.add(self._upgrade_to_high_res(full_url))
            
            # 5. Cari dari CSS inline <style>
            for style_tag in soup.find_all('style'):
                if style_tag.string:
                    matches = re.findall(style_pattern, style_tag.string)
                    for match in matches:
                        full_url = urljoin(url, match)
                        if self._is_valid_image_url(full_url):
                            found_images.add(self._upgrade_to_high_res(full_url))
            
            # 6. Cari dari meta tags (og:image, twitter:image)
            for meta in soup.find_all('meta'):
                if meta.get('property') in ['og:image', 'twitter:image']:
                    img_url = meta.get('content')
                    if img_url:
                        found_images.add(self._upgrade_to_high_res(urljoin(url, img_url)))
            
            # 7. Cari dari JSON-LD dan script tags
            for script in soup.find_all('script'):
                if script.string:
                    # Cari URL gambar dalam script
                    img_patterns = [
                        r'"(?:image|thumbnail|photo|artwork)[Uu]rl?"\s*:\s*"([^"]+)"',
                        r'"(?:original|full|large)[Uu]rl"\s*:\s*"([^"]+)"',
                        r'"url"\s*:\s*"(https?://[^"]+\.(?:jpg|jpeg|png|gif|webp))"',
                    ]
                    for pattern in img_patterns:
                        matches = re.findall(pattern, script.string)
                        for match in matches:
                            if self._is_valid_image_url(match):
                                found_images.add(self._upgrade_to_high_res(match))
            
            # Crawl deeper jika diperlukan
            if depth < self.max_depth:
                for link in soup.find_all('a', href=True):
                    href = link.get('href')
                    if href:
                        next_url = urljoin(url, href)
                        # Hanya crawl URL dalam domain yang sama
                        if urlparse(next_url).netloc == self.domain:
                            time.sleep(REQUEST_DELAY)
                            deeper_images = self.crawl_page(next_url, depth + 1)
                            found_images.update(deeper_images)
            
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Gagal crawl {url}: {e}")
            self.stats['errors'] += 1
        except Exception as e:
            print(f"[ERROR] Error saat parsing {url}: {e}")
            self.stats['errors'] += 1
        
        # Update statistik
        new_images = found_images - self.image_urls
        self.image_urls.update(found_images)
        print(f"  -> Ditemukan {len(new_images)} gambar baru (total: {len(self.image_urls)})")
        
        return found_images
    
    def download_image(self, img_url: str) -> Tuple[bool, str]:
        """
        Download satu gambar.
        
        Args:
            img_url: URL gambar
            
        Returns:
            Tuple (success, message)
        """
        try:
            # Download gambar
            response = self.session.get(img_url, timeout=REQUEST_TIMEOUT, stream=True)
            response.raise_for_status()
            
            # Validasi content type
            content_type = response.headers.get('content-type', '')
            if not any(mime in content_type for mime in ['image', 'octet-stream']):
                return False, f"Bukan gambar: {content_type}"
            
            # Baca content
            content = response.content
            
            # Cek duplikat berdasarkan hash
            content_hash = hashlib.md5(content).hexdigest()
            if content_hash in self.downloaded_hashes:
                return False, "Duplikat (sudah didownload)"
            
            # Generate filename
            filename = self._get_filename_from_url(img_url, response)
            filepath = os.path.join(self.output_dir, filename)
            
            # Handle nama file duplikat
            base, ext = os.path.splitext(filepath)
            counter = 1
            while os.path.exists(filepath):
                filepath = f"{base}_{counter}{ext}"
                counter += 1
            
            # Simpan file
            with open(filepath, 'wb') as f:
                f.write(content)
            
            self.downloaded_hashes.add(content_hash)
            
            # Ukuran file
            size_kb = len(content) / 1024
            return True, f"Tersimpan: {os.path.basename(filepath)} ({size_kb:.1f} KB)"
            
        except requests.exceptions.RequestException as e:
            return False, f"Request error: {e}"
        except Exception as e:
            return False, f"Error: {e}"
    
    def download_all_images(self, parallel: bool = True):
        """
        Download semua gambar yang ditemukan.
        
        Args:
            parallel: Gunakan parallel download (default: True)
        """
        if not self.image_urls:
            print("\n[INFO] Tidak ada gambar untuk didownload.")
            return
        
        # Buat output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"\n{'='*60}")
        print(f"MEMULAI DOWNLOAD")
        print(f"{'='*60}")
        print(f"Total gambar: {len(self.image_urls)}")
        print(f"Output folder: {self.output_dir}")
        print(f"{'='*60}\n")
        
        if parallel and len(self.image_urls) > 1:
            # Parallel download
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = {
                    executor.submit(self.download_image, url): url 
                    for url in self.image_urls
                }
                
                for i, future in enumerate(as_completed(futures), 1):
                    url = futures[future]
                    success, message = future.result()
                    
                    status = "✓" if success else "✗"
                    print(f"[{i}/{len(self.image_urls)}] {status} {message}")
                    
                    if success:
                        self.stats['images_downloaded'] += 1
                    else:
                        self.stats['images_skipped'] += 1
        else:
            # Sequential download
            for i, url in enumerate(self.image_urls, 1):
                success, message = self.download_image(url)
                
                status = "✓" if success else "✗"
                print(f"[{i}/{len(self.image_urls)}] {status} {message}")
                
                if success:
                    self.stats['images_downloaded'] += 1
                else:
                    self.stats['images_skipped'] += 1
                
                time.sleep(REQUEST_DELAY)
    
    def run(self):
        """Jalankan crawler dan downloader."""
        print(f"\n{'='*60}")
        print(f"IMAGE CRAWLER & DOWNLOADER")
        print(f"{'='*60}")
        print(f"Target URL: {self.base_url}")
        print(f"Domain: {self.domain}")
        print(f"Max Depth: {self.max_depth}")
        print(f"{'='*60}")
        
        # Fase 1: Crawling
        print(f"\n[FASE 1] Crawling halaman web...")
        self.crawl_page(self.base_url)
        
        self.stats['images_found'] = len(self.image_urls)
        
        # Fase 2: Download
        print(f"\n[FASE 2] Downloading gambar...")
        self.download_all_images()
        
        # Print statistik
        self._print_stats()
    
    def _print_stats(self):
        """Print statistik akhir."""
        print(f"\n{'='*60}")
        print(f"STATISTIK")
        print(f"{'='*60}")
        print(f"Halaman di-crawl  : {self.stats['pages_crawled']}")
        print(f"Gambar ditemukan  : {self.stats['images_found']}")
        print(f"Gambar didownload : {self.stats['images_downloaded']}")
        print(f"Gambar dilewati   : {self.stats['images_skipped']}")
        print(f"Error             : {self.stats['errors']}")
        print(f"{'='*60}")
        print(f"Output folder: {self.output_dir}")
        print(f"{'='*60}")


# ============================================================================
# FUNGSI BANTUAN
# ============================================================================

def interactive_mode():
    """Mode interaktif untuk user."""
    print("\n" + "="*60)
    print("  IMAGE CRAWLER & DOWNLOADER")
    print("  Crawling web dan download gambar otomatis")
    print("="*60 + "\n")
    
    # Input URL
    while True:
        url = input("Masukkan URL website: ").strip()
        if url:
            # Tambahkan https:// jika tidak ada
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            break
        print("[ERROR] URL tidak boleh kosong!")
    
    # Input depth
    while True:
        depth_input = input("Kedalaman crawling (default: 1, max: 3): ").strip()
        if not depth_input:
            depth = 1
            break
        try:
            depth = int(depth_input)
            if 0 <= depth <= 3:
                break
            print("[ERROR] Kedalaman harus antara 0-3!")
        except ValueError:
            print("[ERROR] Masukkan angka yang valid!")
    
    # Konfirmasi
    print(f"\n[INFO] URL: {url}")
    print(f"[INFO] Kedalaman: {depth}")
    confirm = input("\nLanjutkan? (y/n): ").strip().lower()
    
    if confirm in ['y', 'yes', '']:
        crawler = ImageCrawler(url, max_depth=depth)
        crawler.run()
    else:
        print("\n[INFO] Dibatalkan.")


def main():
    """Fungsi utama."""
    parser = argparse.ArgumentParser(
        description='Image Crawler & Downloader - Crawling web dan download gambar',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Contoh penggunaan:
  python image_crawler.py                           # Mode interaktif
  python image_crawler.py https://example.com       # Crawl URL langsung
  python image_crawler.py -u https://example.com -d 2 -o ./my_images
        '''
    )
    
    parser.add_argument('url', nargs='?', help='URL website untuk di-crawl')
    parser.add_argument('-u', '--url', dest='url_opt', help='URL website (alternatif)')
    parser.add_argument('-d', '--depth', type=int, default=1, 
                        help='Kedalaman crawling (default: 1)')
    parser.add_argument('-o', '--output', help='Folder output untuk menyimpan gambar')
    parser.add_argument('-q', '--quiet', action='store_true', 
                        help='Mode quiet (minimal output)')
    
    args = parser.parse_args()
    
    # Tentukan URL
    url = args.url or args.url_opt
    
    if url:
        # Mode command line
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        crawler = ImageCrawler(url, output_dir=args.output, max_depth=args.depth)
        crawler.run()
    else:
        # Mode interaktif
        interactive_mode()


if __name__ == '__main__':
    main()
