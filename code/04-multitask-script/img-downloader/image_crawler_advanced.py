#!/usr/bin/env python3
"""
Advanced Image Crawler & Downloader
====================================
Script untuk crawling dan download gambar dengan dukungan gallery-dl
untuk akses resolusi penuh pada situs yang memerlukan autentikasi.

Fitur:
- Integrasi dengan gallery-dl untuk situs populer (Pixiv, Twitter, Instagram, dll)
- Sistem autentikasi dengan config file terpisah
- Fallback ke crawler manual jika gallery-dl tidak tersedia
- Support cookies dan session management
- Download resolusi penuh dengan autentikasi

Penggunaan:
    python image_crawler_advanced.py

Author: Claude AI Assistant
Version: 2.0
"""

import os
import re
import sys
import json
import time
import shutil
import hashlib
import argparse
import subprocess
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Set, List, Optional, Tuple, Dict, Any

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("=" * 60)
    print("Library dasar belum terinstall!")
    print("Jalankan: pip install requests beautifulsoup4 lxml")
    print("=" * 60)
    sys.exit(1)


# ============================================================================
# PATHS & CONSTANTS
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.absolute()
CONFIG_FILE = SCRIPT_DIR / "config.json"
COOKIES_DIR = SCRIPT_DIR / "cookies"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "downloaded_images"

# Format gambar yang didukung
IMAGE_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.webp',
    '.bmp', '.svg', '.ico', '.tiff', '.tif'
}

# Situs yang didukung gallery-dl dengan autentikasi
SUPPORTED_SITES = {
    'pixiv': {
        'domains': ['pixiv.net', 'www.pixiv.net', 'i.pximg.net'],
        'auth_type': 'username_password',  # atau 'cookies'
        'auth_fields': ['username', 'password'],
        'gallery_dl_extractor': 'pixiv',
    },
    'twitter': {
        'domains': ['twitter.com', 'x.com', 'pbs.twimg.com'],
        'auth_type': 'cookies',
        'auth_fields': ['cookies_file'],
        'gallery_dl_extractor': 'twitter',
    },
    'instagram': {
        'domains': ['instagram.com', 'www.instagram.com', 'cdninstagram.com'],
        'auth_type': 'username_password',
        'auth_fields': ['username', 'password'],
        'gallery_dl_extractor': 'instagram',
    },
    'deviantart': {
        'domains': ['deviantart.com', 'www.deviantart.com', 'wixmp.com'],
        'auth_type': 'oauth',
        'auth_fields': ['client_id', 'client_secret'],
        'gallery_dl_extractor': 'deviantart',
    },
    'artstation': {
        'domains': ['artstation.com', 'www.artstation.com'],
        'auth_type': 'none',
        'auth_fields': [],
        'gallery_dl_extractor': 'artstation',
    },
    'danbooru': {
        'domains': ['danbooru.donmai.us'],
        'auth_type': 'api_key',
        'auth_fields': ['username', 'api_key'],
        'gallery_dl_extractor': 'danbooru',
    },
    'imgur': {
        'domains': ['imgur.com', 'i.imgur.com'],
        'auth_type': 'client_id',
        'auth_fields': ['client_id'],
        'gallery_dl_extractor': 'imgur',
    },
    'tumblr': {
        'domains': ['tumblr.com'],
        'auth_type': 'api_key',
        'auth_fields': ['api_key', 'api_secret'],
        'gallery_dl_extractor': 'tumblr',
    },
    'flickr': {
        'domains': ['flickr.com', 'www.flickr.com'],
        'auth_type': 'api_key',
        'auth_fields': ['api_key'],
        'gallery_dl_extractor': 'flickr',
    },
    'reddit': {
        'domains': ['reddit.com', 'www.reddit.com', 'i.redd.it'],
        'auth_type': 'client_credentials',
        'auth_fields': ['client_id', 'client_secret', 'user_agent'],
        'gallery_dl_extractor': 'reddit',
    },
}

# Default config template
DEFAULT_CONFIG = {
    "settings": {
        "output_directory": str(DEFAULT_OUTPUT_DIR),
        "max_workers": 5,
        "request_delay": 0.5,
        "request_timeout": 30,
        "use_gallery_dl": True,
        "fallback_to_crawler": True
    },
    "credentials": {
        "pixiv": {
            "username": "",
            "password": "",
            "refresh_token": ""
        },
        "twitter": {
            "cookies_file": "cookies/twitter_cookies.txt",
            "auth_token": ""
        },
        "instagram": {
            "username": "",
            "password": "",
            "session_id": ""
        },
        "deviantart": {
            "client_id": "",
            "client_secret": ""
        },
        "danbooru": {
            "username": "",
            "api_key": ""
        },
        "imgur": {
            "client_id": ""
        },
        "tumblr": {
            "api_key": "",
            "api_secret": ""
        },
        "flickr": {
            "api_key": ""
        },
        "reddit": {
            "client_id": "",
            "client_secret": "",
            "user_agent": "ImageCrawler/2.0"
        }
    },
    "gallery_dl_options": {
        "pixiv": {
            "ugoira": True,
            "metadata": True,
            "tags": True
        },
        "twitter": {
            "retweets": False,
            "videos": True,
            "cards": False
        },
        "instagram": {
            "stories": True,
            "highlights": True,
            "videos": True
        }
    }
}


# ============================================================================
# CONFIGURATION MANAGER
# ============================================================================

class ConfigManager:
    """Mengelola konfigurasi dan kredensial."""
    
    def __init__(self, config_path: Path = CONFIG_FILE):
        self.config_path = config_path
        self.config = self._load_or_create_config()
    
    def _load_or_create_config(self) -> Dict[str, Any]:
        """Load config atau buat baru jika tidak ada."""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                # Merge dengan default untuk field yang mungkin missing
                return self._merge_config(DEFAULT_CONFIG, config)
            except json.JSONDecodeError:
                print(f"[WARNING] Config file corrupt, membuat baru...")
                return self._create_default_config()
        else:
            return self._create_default_config()
    
    def _create_default_config(self) -> Dict[str, Any]:
        """Buat config default."""
        # Buat direktori cookies
        COOKIES_DIR.mkdir(exist_ok=True)
        
        # Simpan config
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4, ensure_ascii=False)
        
        print(f"[INFO] Config file dibuat: {self.config_path}")
        print(f"[INFO] Silakan edit file tersebut untuk menambahkan kredensial.")
        
        return DEFAULT_CONFIG.copy()
    
    def _merge_config(self, default: Dict, user: Dict) -> Dict:
        """Merge user config dengan default."""
        result = default.copy()
        for key, value in user.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_config(result[key], value)
            else:
                result[key] = value
        return result
    
    def save(self):
        """Simpan config ke file."""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)
    
    def get_credentials(self, site: str) -> Dict[str, str]:
        """Ambil kredensial untuk situs tertentu."""
        return self.config.get('credentials', {}).get(site, {})
    
    def set_credentials(self, site: str, credentials: Dict[str, str]):
        """Set kredensial untuk situs tertentu."""
        if 'credentials' not in self.config:
            self.config['credentials'] = {}
        self.config['credentials'][site] = credentials
        self.save()
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Ambil setting."""
        return self.config.get('settings', {}).get(key, default)
    
    def get_gallery_dl_options(self, site: str) -> Dict[str, Any]:
        """Ambil opsi gallery-dl untuk situs tertentu."""
        return self.config.get('gallery_dl_options', {}).get(site, {})


# ============================================================================
# GALLERY-DL WRAPPER
# ============================================================================

class GalleryDLWrapper:
    """Wrapper untuk gallery-dl command line tool."""
    
    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager
        self.gallery_dl_path = self._find_gallery_dl()
        self.gallery_dl_config_path = SCRIPT_DIR / "gallery-dl.conf"
    
    def _find_gallery_dl(self) -> Optional[str]:
        """Cari gallery-dl executable."""
        # Cek di PATH
        gallery_dl = shutil.which('gallery-dl')
        if gallery_dl:
            return gallery_dl
        
        # Cek di direktori script
        local_paths = [
            SCRIPT_DIR / 'gallery-dl',
            SCRIPT_DIR / 'gallery-dl.exe',
            SCRIPT_DIR / 'venv' / 'bin' / 'gallery-dl',
            SCRIPT_DIR / 'venv' / 'Scripts' / 'gallery-dl.exe',
        ]
        
        for path in local_paths:
            if path.exists():
                return str(path)
        
        return None
    
    def is_available(self) -> bool:
        """Cek apakah gallery-dl tersedia."""
        return self.gallery_dl_path is not None
    
    def install(self) -> bool:
        """Install gallery-dl via pip."""
        print("[INFO] Menginstall gallery-dl...")
        try:
            subprocess.run(
                [sys.executable, '-m', 'pip', 'install', 'gallery-dl', '-q'],
                check=True
            )
            self.gallery_dl_path = shutil.which('gallery-dl')
            return self.is_available()
        except subprocess.CalledProcessError:
            print("[ERROR] Gagal menginstall gallery-dl")
            return False
    
    def _generate_config(self, site: str) -> Dict[str, Any]:
        """Generate gallery-dl config untuk situs tertentu."""
        creds = self.config.get_credentials(site)
        options = self.config.get_gallery_dl_options(site)
        
        config = {
            "extractor": {},
            "downloader": {
                "rate": "1M",
                "retries": 3,
                "timeout": 30,
            },
            "output": {
                "mode": "terminal",
                "progress": True,
            }
        }
        
        # Konfigurasi per-situs
        if site == 'pixiv':
            config["extractor"]["pixiv"] = {
                "filename": "{id}_{title}_{num}.{extension}",
                "directory": ["pixiv", "{user[name]}"],
            }
            if creds.get('username') and creds.get('password'):
                config["extractor"]["pixiv"]["username"] = creds['username']
                config["extractor"]["pixiv"]["password"] = creds['password']
            elif creds.get('refresh_token'):
                config["extractor"]["pixiv"]["refresh-token"] = creds['refresh_token']
            
            if options.get('ugoira'):
                config["extractor"]["pixiv"]["ugoira"] = True
        
        elif site == 'twitter':
            config["extractor"]["twitter"] = {
                "filename": "{tweet_id}_{num}.{extension}",
                "directory": ["twitter", "{user[name]}"],
                "retweets": options.get('retweets', False),
                "videos": options.get('videos', True),
            }
            if creds.get('cookies_file'):
                cookies_path = Path(creds['cookies_file'])
                if not cookies_path.is_absolute():
                    cookies_path = SCRIPT_DIR / cookies_path
                if cookies_path.exists():
                    config["extractor"]["twitter"]["cookies"] = str(cookies_path)
            elif creds.get('auth_token'):
                config["extractor"]["twitter"]["cookies"] = {
                    "auth_token": creds['auth_token']
                }
        
        elif site == 'instagram':
            config["extractor"]["instagram"] = {
                "filename": "{shortcode}_{num}.{extension}",
                "directory": ["instagram", "{username}"],
                "stories": options.get('stories', True),
                "highlights": options.get('highlights', True),
                "videos": options.get('videos', True),
            }
            if creds.get('username') and creds.get('password'):
                config["extractor"]["instagram"]["username"] = creds['username']
                config["extractor"]["instagram"]["password"] = creds['password']
            elif creds.get('session_id'):
                config["extractor"]["instagram"]["cookies"] = {
                    "sessionid": creds['session_id']
                }
        
        elif site == 'deviantart':
            config["extractor"]["deviantart"] = {
                "filename": "{index}_{title}.{extension}",
                "directory": ["deviantart", "{author[username]}"],
                "flat": False,
                "original": True,
            }
            if creds.get('client_id') and creds.get('client_secret'):
                config["extractor"]["deviantart"]["client-id"] = creds['client_id']
                config["extractor"]["deviantart"]["client-secret"] = creds['client_secret']
        
        elif site == 'danbooru':
            config["extractor"]["danbooru"] = {
                "filename": "{id}_{md5}.{extension}",
                "directory": ["danbooru"],
            }
            if creds.get('username') and creds.get('api_key'):
                config["extractor"]["danbooru"]["username"] = creds['username']
                config["extractor"]["danbooru"]["api-key"] = creds['api_key']
        
        elif site == 'imgur':
            config["extractor"]["imgur"] = {
                "filename": "{id}_{num}.{extension}",
                "directory": ["imgur", "{album[title]|id}"],
                "mp4": True,
            }
            if creds.get('client_id'):
                config["extractor"]["imgur"]["client-id"] = creds['client_id']
        
        elif site == 'reddit':
            config["extractor"]["reddit"] = {
                "filename": "{id}_{num}.{extension}",
                "directory": ["reddit", "{subreddit}"],
                "comments": 0,
            }
            if creds.get('client_id') and creds.get('client_secret'):
                config["extractor"]["reddit"]["client-id"] = creds['client_id']
                config["extractor"]["reddit"]["client-secret"] = creds['client_secret']
                config["extractor"]["reddit"]["user-agent"] = creds.get('user_agent', 'ImageCrawler/2.0')
        
        return config
    
    def _save_temp_config(self, config: Dict[str, Any]) -> Path:
        """Simpan config sementara untuk gallery-dl."""
        config_path = SCRIPT_DIR / ".gallery-dl-temp.conf"
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        return config_path
    
    def detect_site(self, url: str) -> Optional[str]:
        """Deteksi situs dari URL."""
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        for site, info in SUPPORTED_SITES.items():
            for site_domain in info['domains']:
                if site_domain in domain:
                    return site
        
        return None
    
    def download(self, url: str, output_dir: Path, site: str = None) -> Tuple[bool, str, List[str]]:
        """
        Download menggunakan gallery-dl.
        
        Returns:
            Tuple (success, message, downloaded_files)
        """
        if not self.is_available():
            return False, "gallery-dl tidak tersedia", []
        
        # Deteksi situs jika tidak diberikan
        if not site:
            site = self.detect_site(url)
        
        if not site:
            return False, "Situs tidak didukung oleh gallery-dl", []
        
        # Generate dan simpan config
        config = self._generate_config(site)
        config_path = self._save_temp_config(config)
        
        # Buat output directory
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Build command
        cmd = [
            self.gallery_dl_path,
            '--config', str(config_path),
            '--dest', str(output_dir),
            '--write-metadata',
            url
        ]
        
        print(f"\n[GALLERY-DL] Mendownload dari {site}...")
        print(f"[GALLERY-DL] URL: {url}")
        print(f"[GALLERY-DL] Output: {output_dir}")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 menit timeout
            )
            
            # Hapus config sementara
            config_path.unlink(missing_ok=True)
            
            # Parse output untuk mendapatkan file yang didownload
            downloaded_files = []
            for line in result.stdout.split('\n'):
                if line.strip():
                    # gallery-dl biasanya print path file yang didownload
                    if output_dir.as_posix() in line or any(ext in line.lower() for ext in IMAGE_EXTENSIONS):
                        downloaded_files.append(line.strip())
            
            if result.returncode == 0:
                return True, f"Berhasil download dari {site}", downloaded_files
            else:
                error_msg = result.stderr or result.stdout or "Unknown error"
                return False, f"gallery-dl error: {error_msg[:200]}", downloaded_files
                
        except subprocess.TimeoutExpired:
            return False, "Timeout - proses terlalu lama", []
        except Exception as e:
            return False, f"Error: {str(e)}", []


# ============================================================================
# MANUAL CRAWLER (FALLBACK)
# ============================================================================

class ManualCrawler:
    """Crawler manual sebagai fallback."""
    
    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager
        self.session = requests.Session()
        self._setup_session()
        
        self.visited_urls: Set[str] = set()
        self.image_urls: Set[str] = set()
        self.downloaded_hashes: Set[str] = set()
    
    def _setup_session(self):
        """Setup session dengan headers."""
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
        })
    
    def _is_valid_image_url(self, url: str) -> bool:
        """Cek apakah URL adalah gambar."""
        path_lower = urlparse(url).path.lower()
        return any(path_lower.endswith(ext) for ext in IMAGE_EXTENSIONS)
    
    def _upgrade_to_high_res(self, img_url: str) -> str:
        """Upgrade URL ke resolusi tinggi."""
        # Pixiv
        if 'pximg.net' in img_url:
            img_url = re.sub(r'/c/\d+x\d+[^/]*/', '/img-original/', img_url)
            img_url = re.sub(r'_square\d+|_master\d+', '', img_url)
        # Twitter
        elif 'twimg.com' in img_url:
            img_url = re.sub(r'\?.*$', '', img_url)
            img_url += '?name=orig' if '?' not in img_url else '&name=orig'
        # Imgur
        elif 'imgur.com' in img_url:
            img_url = re.sub(r'([a-zA-Z0-9]+)[smhl]\.', r'\1.', img_url)
        
        return img_url
    
    def crawl_page(self, url: str, depth: int = 0, max_depth: int = 1) -> Set[str]:
        """Crawl halaman untuk gambar."""
        if url in self.visited_urls or depth > max_depth:
            return set()
        
        self.visited_urls.add(url)
        found_images: Set[str] = set()
        
        print(f"[CRAWL] Depth {depth}: {url}")
        
        try:
            response = self.session.get(
                url,
                timeout=self.config.get_setting('request_timeout', 30)
            )
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Cari gambar dari berbagai sumber
            # 1. Tag <img>
            for img in soup.find_all('img'):
                for attr in ['src', 'data-src', 'data-original', 'srcset']:
                    img_url = img.get(attr)
                    if img_url:
                        if attr == 'srcset':
                            for part in img_url.split(','):
                                src = part.strip().split()[0]
                                full_url = urljoin(url, src)
                                found_images.add(self._upgrade_to_high_res(full_url))
                        else:
                            full_url = urljoin(url, img_url)
                            found_images.add(self._upgrade_to_high_res(full_url))
            
            # 2. Tag <a> menuju gambar
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href and self._is_valid_image_url(href):
                    full_url = urljoin(url, href)
                    found_images.add(self._upgrade_to_high_res(full_url))
            
            # 3. Background images
            style_pattern = r'url\(["\']?([^"\')\s]+)["\']?\)'
            for element in soup.find_all(style=True):
                matches = re.findall(style_pattern, element.get('style', ''))
                for match in matches:
                    full_url = urljoin(url, match)
                    if self._is_valid_image_url(full_url):
                        found_images.add(self._upgrade_to_high_res(full_url))
            
            # 4. Meta tags
            for meta in soup.find_all('meta'):
                if meta.get('property') in ['og:image', 'twitter:image']:
                    img_url = meta.get('content')
                    if img_url:
                        found_images.add(self._upgrade_to_high_res(urljoin(url, img_url)))
            
            print(f"  -> Ditemukan {len(found_images)} gambar")
            
        except Exception as e:
            print(f"[ERROR] {e}")
        
        return found_images
    
    def download_image(self, img_url: str, output_dir: Path) -> Tuple[bool, str]:
        """Download satu gambar."""
        try:
            response = self.session.get(img_url, timeout=30, stream=True)
            response.raise_for_status()
            
            content = response.content
            content_hash = hashlib.md5(content).hexdigest()
            
            if content_hash in self.downloaded_hashes:
                return False, "Duplikat"
            
            # Generate filename
            filename = os.path.basename(urlparse(img_url).path)
            if not filename or '.' not in filename:
                ext = '.jpg'
                content_type = response.headers.get('content-type', '')
                if 'png' in content_type:
                    ext = '.png'
                elif 'gif' in content_type:
                    ext = '.gif'
                elif 'webp' in content_type:
                    ext = '.webp'
                filename = f"image_{content_hash[:12]}{ext}"
            
            filepath = output_dir / filename
            counter = 1
            while filepath.exists():
                stem = filepath.stem
                filepath = output_dir / f"{stem}_{counter}{filepath.suffix}"
                counter += 1
            
            with open(filepath, 'wb') as f:
                f.write(content)
            
            self.downloaded_hashes.add(content_hash)
            size_kb = len(content) / 1024
            
            return True, f"{filepath.name} ({size_kb:.1f} KB)"
            
        except Exception as e:
            return False, str(e)


# ============================================================================
# MAIN CRAWLER CLASS
# ============================================================================

class AdvancedImageCrawler:
    """Crawler utama dengan integrasi gallery-dl."""
    
    def __init__(self, url: str, output_dir: str = None, max_depth: int = 1):
        self.url = url
        self.max_depth = max_depth
        
        # Setup config
        self.config = ConfigManager()
        
        # Setup output directory
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            domain = urlparse(url).netloc
            safe_domain = re.sub(r'[^\w\-.]', '_', domain)
            self.output_dir = DEFAULT_OUTPUT_DIR / safe_domain
        
        # Setup gallery-dl wrapper
        self.gallery_dl = GalleryDLWrapper(self.config)
        
        # Setup manual crawler
        self.manual_crawler = ManualCrawler(self.config)
        
        # Deteksi situs
        self.detected_site = self.gallery_dl.detect_site(url)
        
        # Statistik
        self.stats = {
            'method': 'unknown',
            'images_found': 0,
            'images_downloaded': 0,
            'errors': 0
        }
    
    def _check_credentials(self) -> bool:
        """Cek apakah kredensial tersedia untuk situs terdeteksi."""
        if not self.detected_site:
            return False
        
        creds = self.config.get_credentials(self.detected_site)
        site_info = SUPPORTED_SITES.get(self.detected_site, {})
        
        if site_info.get('auth_type') == 'none':
            return True
        
        # Cek minimal satu credential field terisi
        for field in site_info.get('auth_fields', []):
            if creds.get(field):
                return True
        
        return False
    
    def run(self):
        """Jalankan crawler."""
        print("\n" + "=" * 60)
        print("ADVANCED IMAGE CRAWLER & DOWNLOADER v2.0")
        print("=" * 60)
        print(f"URL: {self.url}")
        print(f"Detected Site: {self.detected_site or 'Unknown'}")
        print(f"Output: {self.output_dir}")
        print("=" * 60)
        
        # Buat output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Coba gallery-dl terlebih dahulu
        use_gallery_dl = self.config.get_setting('use_gallery_dl', True)
        fallback_enabled = self.config.get_setting('fallback_to_crawler', True)
        
        success = False
        
        if use_gallery_dl and self.detected_site:
            if not self.gallery_dl.is_available():
                print("\n[INFO] gallery-dl tidak ditemukan. Mencoba install...")
                if not self.gallery_dl.install():
                    print("[WARNING] Gagal install gallery-dl, menggunakan manual crawler...")
                    use_gallery_dl = False
            
            if use_gallery_dl:
                # Cek kredensial
                has_creds = self._check_credentials()
                if not has_creds:
                    print(f"\n[WARNING] Kredensial untuk {self.detected_site} tidak ditemukan.")
                    print(f"[INFO] Edit file config.json untuk menambahkan kredensial.")
                    print(f"[INFO] Melanjutkan tanpa autentikasi (mungkin tidak dapat akses resolusi penuh)...")
                
                # Download dengan gallery-dl
                success, message, files = self.gallery_dl.download(
                    self.url,
                    self.output_dir,
                    self.detected_site
                )
                
                print(f"\n[RESULT] {message}")
                
                if success:
                    self.stats['method'] = 'gallery-dl'
                    self.stats['images_downloaded'] = len(files)
        
        # Fallback ke manual crawler
        if not success and fallback_enabled:
            print("\n[INFO] Menggunakan manual crawler sebagai fallback...")
            self.stats['method'] = 'manual'
            
            # Crawl
            images = self.manual_crawler.crawl_page(self.url, max_depth=self.max_depth)
            self.stats['images_found'] = len(images)
            
            # Download
            if images:
                print(f"\n[DOWNLOAD] Mendownload {len(images)} gambar...")
                
                for i, img_url in enumerate(images, 1):
                    success, msg = self.manual_crawler.download_image(img_url, self.output_dir)
                    status = "✓" if success else "✗"
                    print(f"[{i}/{len(images)}] {status} {msg}")
                    
                    if success:
                        self.stats['images_downloaded'] += 1
                    
                    time.sleep(self.config.get_setting('request_delay', 0.5))
        
        # Print summary
        self._print_summary()
    
    def _print_summary(self):
        """Print ringkasan."""
        print("\n" + "=" * 60)
        print("RINGKASAN")
        print("=" * 60)
        print(f"Metode           : {self.stats['method']}")
        print(f"Gambar ditemukan : {self.stats['images_found']}")
        print(f"Gambar didownload: {self.stats['images_downloaded']}")
        print(f"Output folder    : {self.output_dir}")
        print("=" * 60)


# ============================================================================
# CLI & INTERACTIVE MODE
# ============================================================================

def setup_credentials_interactive():
    """Setup kredensial secara interaktif."""
    config = ConfigManager()
    
    print("\n" + "=" * 60)
    print("SETUP KREDENSIAL")
    print("=" * 60)
    print("\nPilih situs untuk setup kredensial:")
    
    sites = list(SUPPORTED_SITES.keys())
    for i, site in enumerate(sites, 1):
        info = SUPPORTED_SITES[site]
        print(f"  {i}. {site.capitalize()} (Auth: {info['auth_type']})")
    
    print(f"  0. Kembali")
    
    try:
        choice = int(input("\nPilihan: "))
        if choice == 0:
            return
        
        site = sites[choice - 1]
        site_info = SUPPORTED_SITES[site]
        
        print(f"\n[INFO] Setup kredensial untuk {site.capitalize()}")
        print(f"[INFO] Auth type: {site_info['auth_type']}")
        
        creds = config.get_credentials(site)
        
        for field in site_info['auth_fields']:
            current = creds.get(field, '')
            display = '*' * len(current) if 'password' in field.lower() or 'secret' in field.lower() or 'token' in field.lower() else current
            
            value = input(f"  {field} [{display}]: ").strip()
            if value:
                creds[field] = value
        
        config.set_credentials(site, creds)
        print(f"\n[OK] Kredensial untuk {site} telah disimpan.")
        
    except (ValueError, IndexError):
        print("[ERROR] Pilihan tidak valid.")


def interactive_mode():
    """Mode interaktif."""
    print("\n" + "=" * 60)
    print("  ADVANCED IMAGE CRAWLER & DOWNLOADER v2.0")
    print("  Dengan dukungan gallery-dl untuk resolusi penuh")
    print("=" * 60)
    
    print("\nMenu:")
    print("  1. Download gambar dari URL")
    print("  2. Setup kredensial")
    print("  3. Lihat konfigurasi")
    print("  4. Keluar")
    
    try:
        choice = int(input("\nPilihan: "))
        
        if choice == 1:
            url = input("\nMasukkan URL: ").strip()
            if not url:
                print("[ERROR] URL tidak boleh kosong!")
                return
            
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            depth_input = input("Kedalaman crawling (default: 1): ").strip()
            depth = int(depth_input) if depth_input else 1
            
            crawler = AdvancedImageCrawler(url, max_depth=depth)
            crawler.run()
        
        elif choice == 2:
            setup_credentials_interactive()
        
        elif choice == 3:
            config = ConfigManager()
            print("\n" + "=" * 60)
            print("KONFIGURASI SAAT INI")
            print("=" * 60)
            print(json.dumps(config.config, indent=2, ensure_ascii=False))
        
        elif choice == 4:
            print("\nSampai jumpa!")
            sys.exit(0)
        
    except ValueError:
        print("[ERROR] Input tidak valid.")


def main():
    """Fungsi utama."""
    parser = argparse.ArgumentParser(
        description='Advanced Image Crawler dengan gallery-dl',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Contoh:
  python image_crawler_advanced.py                    # Mode interaktif
  python image_crawler_advanced.py https://pixiv.net/users/123
  python image_crawler_advanced.py -u URL -d 2 -o ./output
  python image_crawler_advanced.py --setup           # Setup kredensial
        '''
    )
    
    parser.add_argument('url', nargs='?', help='URL untuk di-crawl')
    parser.add_argument('-u', '--url', dest='url_opt', help='URL (alternatif)')
    parser.add_argument('-d', '--depth', type=int, default=1, help='Kedalaman crawling')
    parser.add_argument('-o', '--output', help='Folder output')
    parser.add_argument('--setup', action='store_true', help='Setup kredensial')
    parser.add_argument('--install-gallery-dl', action='store_true', help='Install gallery-dl')
    
    args = parser.parse_args()
    
    if args.setup:
        setup_credentials_interactive()
        return
    
    if args.install_gallery_dl:
        config = ConfigManager()
        wrapper = GalleryDLWrapper(config)
        if wrapper.install():
            print("[OK] gallery-dl berhasil diinstall!")
        return
    
    url = args.url or args.url_opt
    
    if url:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        crawler = AdvancedImageCrawler(url, output_dir=args.output, max_depth=args.depth)
        crawler.run()
    else:
        interactive_mode()


if __name__ == '__main__':
    main()
