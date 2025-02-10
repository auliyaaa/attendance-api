# Attendance API 🚀

Attendance API adalah sebuah sistem berbasis **Python (Flask)** dan **PHP (CodeIgniter)** yang berfungsi untuk mengelola data kehadiran, menyimpan data ke **PostgreSQL**, serta menyediakan endpoint untuk mengakses data kehadiran dalam format **JSON**.

## 📌 Fitur
- 📥 **Import data kehadiran** dari file **Excel (seed.xlsx)**
- 🗄️ **Simpan data ke PostgreSQL**
- 📡 **Expose API** dengan Flask dan CodeIgniter
- 🏗️ **Dockerized** untuk kemudahan deployment
- 📊 **View data kehadiran** dalam bentuk ringkasan

---

## 🛠️ Teknologi yang Digunakan
- **Python** (Flask, Pandas, psycopg2)
- **PHP** (CodeIgniter)
- **PostgreSQL**
- **Docker**
- **Git & GitHub**

---

## 📦 Instalasi dan Setup

### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/auliyaaa/attendance-api.git
cd attendance-api
```

### 2️⃣ **Buat dan Atur `.env`**
Buat file `.env` di root directory dengan isi berikut:
```env
PYTHON_DB_URI=postgresql://username:password@postgres:5432/attendance_db
```

### 3️⃣ **Jalankan dengan Docker**
```bash
docker-compose up --build -d
```

---

## 🔥 **Menjalankan API**
### 1️⃣ **Endpoint Flask (Python)**
| Endpoint | Method | Deskripsi |
|----------|--------|------------|
| `/api/attendance` | GET | Menampilkan semua data kehadiran |
| `/api/attendance_summary` | GET | Menampilkan ringkasan kehadiran |

### 2️⃣ **Endpoint CodeIgniter (PHP)**
| Endpoint | Method | Deskripsi |
|----------|--------|------------|
| `/attendance` | GET | Menampilkan semua data kehadiran |
| `/attendance_summary` | GET | Menampilkan ringkasan kehadiran |

---

## 📊 **Membuat View di PostgreSQL**
Jalankan perintah SQL berikut di database:
```sql
CREATE VIEW attendance_summary AS
SELECT 
    location, 
    date, 
    COUNT(id) AS total_attendance
FROM attendance
GROUP BY location, date
ORDER BY date DESC;
```

---

## 🤝 **Kontributor**
- [@auliyaaa](https://github.com/auliyaaa)

---

## 📜 Lisensi
Proyek ini menggunakan lisensi **MIT**. Anda bebas menggunakannya untuk keperluan pribadi atau komersial.

---

🎯 **Happy Coding!** 🚀
