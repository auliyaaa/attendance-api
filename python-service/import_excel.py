import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use localhost when running outside Docker
DB_URI = os.getenv("PYTHON_DBURI_LOCAL") 


# Baca file Excel
import os
# Get absolute path to seed.xlsx
file_path = os.path.join(os.path.dirname(__file__), "seed.xlsx")



df = pd.read_excel(file_path)

# Koneksi ke PostgreSQL
conn = psycopg2.connect(DB_URI)
cursor = conn.cursor()

# Pastikan tabel sudah ada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id SERIAL PRIMARY KEY,
        Date DATE NOT NULL,
        Name VARCHAR(255) NOT NULL,
        Time TIME NOT NULL,
        Location VARCHAR(255) NOT NULL
    );
""")
conn.commit()

# Masukkan data ke database
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO attendance (date, name, time, location)
        VALUES (%s, %s, %s, %s)
    """, (row['Date'], row['Name'], row['Time'], row['Location']))

conn.commit()
cursor.close()
conn.close()

print("✅ Data berhasil diimpor ke PostgreSQL!")
