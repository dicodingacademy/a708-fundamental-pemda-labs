import requests
import pandas as pd
from bs4 import BeautifulSoup

# Tambahkan user-agent ke dalam header untuk menghindari blokir oleh server
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def extract_tourism_data(section):
    """Mengekstrak data tempat wisata dari satu elemen <section>."""
    tempat_wisata = section.find('h3').text
    deskripsi = section.find('p').text.replace('\n', '').strip()
    url_gambar = section.find('img')["src"]

    return {
        "tempat_wisata": tempat_wisata,
        "deskripsi": deskripsi,
        "url_gambar": url_gambar
    }


def fetch_page_content(url):
    """Mengambil konten HTML dari URL dengan user-agent yang ditentukan."""
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Memunculkan HTTPError untuk status yang buruk
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil {url}: {e}")
        return None



def scrape_tourism_data(url):
    """Melakukan scraping untuk semua data tempat wisata."""
    content = fetch_page_content(url)
    if not content:
        return []  # Kembalikan list kosong jika gagal mengambil konten

    soup = BeautifulSoup(content, 'html.parser')
    data = []
    articles = soup.find('article', id='wisata', class_='card')

    if articles:
        # Navigasi menggunakan .descendants untuk menemukan <section>
        sections = [desc for desc in articles.descendants if desc.name == 'section']
        for section in sections:
            tourism_data = extract_tourism_data(section)
            data.append(tourism_data)
    return data


def main():
    """Fungsi utama untuk menjalankan proses scraping dan menyimpan data."""
    url = 'https://halaman-profil-bandung-grid.netlify.app/'
    tourism_data = scrape_tourism_data(url)

    if tourism_data:
        df = pd.DataFrame(tourism_data)
        print(df)
    else:
        print("Tidak ada data yang ditemukan.")


if __name__ == "__main__":
    main()
