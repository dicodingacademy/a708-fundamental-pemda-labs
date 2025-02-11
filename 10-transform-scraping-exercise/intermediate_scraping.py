import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}


def fetching_content(url):
    """Mengambil konten HTML dari URL yang diberikan."""
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None


def extract_book_data(article):
    """Mengambil data buku berupa judul, harga, ketersediaan, dan rating dari article (element html)."""
    book_title = article.find('h3').text
    product_element = article.find('div', class_='product_price')
    price = product_element.find('p', class_='price_color').text
    availability_element = product_element.find('p', class_='instock availability')
    available = "Available" if availability_element else "Not Available"

    rating_element = article.find('p', class_='star-rating')
    rating = rating_element['class'][1] if rating_element else "Rating not found"

    books = {
        "Title": book_title,
        "Price": price,
        "Availability": available,
        "Rating": rating
    }

    return books


def scrape_book(base_url, start_page=1, delay=2):
    """Fungsi utama untuk mengambil keseluruhan data, mulai dari requests hingga menyimpannya dalam variabel data."""
    data = []
    page_number = start_page

    while True:
        url = base_url.format(page_number)
        print(f"Scraping halaman: {url}")

        content = fetching_content(url)
        if content:
            soup = BeautifulSoup(content, "html.parser")
            articles_element = soup.find_all('article', class_='product_pod')
            for article in articles_element:
                book = extract_book_data(article)
                data.append(book)

            next_button = soup.find('li', class_='next')
            if next_button:
                page_number += 1
                time.sleep(delay) # Delay sebelum halaman berikutnya
            else:
                break # Berhenti jika sudah tidak ada next button
        else:
            break # Berhenti jika ada kesalahan

    return data


def main():
    """Fungsi utama untuk keseluruhan proses scraping hingga menyimpannya."""
    BASE_URL = 'https://books.toscrape.com/catalogue/page-{}.html'
    all_books_data = scrape_book(BASE_URL)
    df = pd.DataFrame(all_books_data)
    print(df)


if __name__ == '__main__':
    main()
