from sqlalchemy import create_engine

def store_to_postgre(data, db_url):
    """Fungsi untuk menyimpan data ke dalam PostgreSQL."""
    try:
        # Membuat engine database
        engine = create_engine(db_url)
        
        # Menyimpan data ke tabel 'bookstoscrape' jika tabel sudah ada, data akan ditambahkan (append)
        with engine.connect() as con:
            data.to_sql('bookstoscrape', con=con, if_exists='append', index=False)
            print("Data berhasil ditambahkan!")
    
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")
