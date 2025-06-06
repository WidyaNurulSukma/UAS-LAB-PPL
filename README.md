# 🏟️ Futsal Booking App

Aplikasi ini memungkinkan pengguna untuk memesan lapangan futsal melalui halaman web dan admin untuk mengelola booking melalui dashboard. Booking yang dibuat oleh pengguna disimpan di database SQLite Django, sehingga dapat dikelola langsung oleh admin.

---
## 👤👤👤 Anggota Kelompok
1. Widya Nurul Sukma (2208107010054)
2. Pryta Rosela (2208107010046)
3. MIla Lestari (2208107010002)

## 🚀 Fitur Utama

### 👤 Halaman User
- **Landing Page:** Menampilkan jadwal booking (`index.html`)
- **Formulir Booking:** Memungkinkan pengguna memesan lapangan (`booking.html`)
- **Konfirmasi Booking:** Menampilkan detail booking yang berhasil dibuat (`confirmation.html`)

### 👨‍💼 Dashboard Admin
- **Autentikasi:** Login admin menggunakan Django Authentication
- **Manajemen Booking:** Operasi CRUD (Create, Read, Update, Delete) melalui Django Admin

### 🔌 API Publik
- **Endpoint Utama:** Mengelola jadwal dan booking melalui Django REST Framework  
  (`/api/bookings/`, `/api/bookings/list/`, `/api/bookings/<id>/`)
- **Proxy Opsional:** Express.js digunakan sebagai proxy untuk frontend (opsional), mendukung nilai plus penggunaan dua framework

---

## 🧱 Teknologi yang Digunakan

- **Backend:** Django (Python) untuk dashboard admin, logika utama, dan API
- **API:**
  - Django REST Framework untuk endpoint utama
  - Express.js (Node.js) sebagai proxy opsional untuk komunikasi frontend
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Database:** SQLite (Django) sebagai penyimpanan utama booking
- **Tambahan:** `django-cors-headers` untuk komunikasi lintas domain

---

## 📁 Struktur Folder

```
futsal-booking/
├── backend-django/         # Backend Django
│   ├── booking/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── futsal_app/
│   ├── manage.py
│   └── requirements.txt
├── api-express/            # API Express.js (opsional)
│   ├── index.js
│   ├── package.json
│   └── bookings.json
├── frontend/               # Frontend statis
│   ├── index.html
│   ├── booking.html
│   ├── confirmation.html
│   └── assets/
└── README.md
```

---

## ⚙️ Instalasi

### 📌 Prasyarat
- Python 3.8+
- Node.js 18+ (jika menggunakan Express.js)
- Git
- Visual Studio Code dengan ekstensi Python dan Live Server

---

### 🧩 Backend Django

```bash
cd backend-django
python -m venv venv

# Aktifkan environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

📍 Akses:
- Dashboard Admin: [http://localhost:8000/admin](http://localhost:8000/admin)
- API Endpoint:
  - POST: `http://localhost:8000/api/bookings/`
  - GET: `http://localhost:8000/api/bookings/list/`

---

### 🔁 API Express.js (Opsional)

```bash
cd api-express
npm install
npm start
```

📍 Akses: [http://localhost:3000/api/bookings](http://localhost:3000/api/bookings)

---

### 🎨 Frontend

1. Buka folder `frontend` di VSCode
2. Klik kanan pada `index.html` → **Open with Live Server**  
   (memerlukan ekstensi Live Server)

Alternatif via terminal:

```bash
cd frontend
npx http-server
```

📍 Akses: `http://127.0.0.1:5500/index.html` *(port bisa bervariasi)*

---

## 🧪 Penggunaan

### 👤 Pengguna
1. Buka `frontend/index.html` untuk melihat jadwal booking
2. Klik **Pesan Sekarang** → isi formulir booking di `booking.html`
3. Masukkan:
   - Nama pemesan
   - Lapangan
   - Tanggal
   - Jam mulai
   - Jam selesai
4. Klik **Pesan**
5. Lihat detail konfirmasi di `confirmation.html`

### 👨‍💼 Admin
1. Login ke [http://localhost:8000/admin](http://localhost:8000/admin)
2. Klik **Booking** untuk melihat/mengelola data
3. Bisa melakukan:
   - Tambah Booking
   - Edit Booking
   - Hapus Booking (centang, pilih "Delete selected bookings" → Go)

---

## 🔄 Catatan Integrasi

- Booking dari halaman user disimpan di database SQLite Django melalui endpoint:  
  `POST http://localhost:8000/api/bookings/`
- Frontend mengirim data langsung ke API Django
- Express.js dapat digunakan sebagai **proxy opsional**
- `django-cors-headers` diaktifkan untuk mendukung komunikasi frontend-backend

---

## 🎥 Video Presentasi

📎https://drive.google.com/drive/folders/1lIama9-LE2LjxV0q4UBLrOxlFLRH6pgD  

## 📄 Slide Presentasi

📎 https://www.canva.com/design/DAGpiqGVCts/7II1l5vg0TcsayozueOBNw/view?utm_content=DAGpiqGVCts&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h76c6cd0bc6 
---


## 📄 Dokumentasi Tambahan

- File `presentasi.pptx` menyertai repo ini
- Berisi:
  - Penjelasan fitur
  - Struktur folder
  - Teknologi yang digunakan
  - Screenshot halaman user & admin
  - Alur integrasi backend & frontend

---

## 🛠️ Troubleshooting

### ❌ Booking Tidak Muncul di Admin
- Pastikan Django server aktif: `python manage.py runserver`
- Cek browser DevTools untuk error: CORS / Network / JS
- Uji API via Postman:

```json
POST http://localhost:8000/api/bookings/
{
  "nama_pemesan": "Test User",
  "lapangan": "Lapangan A",
  "tanggal": "2025-06-15",
  "jam_mulai": "18:00:00",
  "jam_selesai": "19:00:00"
}
```

### 🔒 Error CORS
Pastikan di `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True
```

### 🗑️ Opsi Delete 
- Centang item di daftar booking
- Pilih **Delete selected bookings** dari dropdown `Action`
- Klik **Go**

---
