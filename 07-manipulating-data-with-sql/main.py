from sqlalchemy import create_engine

# Membuat database engine
engine = create_engine('postgresql+psycopg2://developer:secretpassword@localhost:5432/companydb')

# Menghubungkan database engine
con = engine.connect()
print("Terhubung dengan basis data!")

# Menutup koneksi database
con.close()
