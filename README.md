# 📘 Finance App (Python)

Aplikasi manajemen keuangan sederhana berbasis Python yang digunakan untuk mencatat pemasukan, pengeluaran, menampilkan laporan transaksi, serta menyimpan data ke file JSON. Cocok untuk belajar CLI App & file-based storage.

---

## 🚀 Fitur Utama
- Tambah pemasukan  
- Tambah pengeluaran  
- Lihat semua transaksi  
- Filter transaksi berdasarkan tipe  
- Total saldo otomatis  
- Penyimpanan ke `data.json`  
- CLI interaktif  

---

## 📦 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/USERNAME/finance-app.git
cd finance-app
```

---

### 2. (Opsional) Buat Virtual Environment
```bash
python -m venv venv
```

#### Aktifkan Virtual Environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

Jika project memiliki file `requirements.txt`, jalankan:

```bash
pip install -r requirements.txt
```

Jika belum ada, berikut minimal library yang digunakan:

```bash
pip install tabulate colorama
```

---

### 4. Jalankan Aplikasi
```bash
python main.py
```

---

## 📂 Struktur Folder
```
finance-app/
│── main.py            # File utama aplikasi
│── data.json          # Penyimpanan transaksi
│── requirements.txt   # Daftar library
└── screenshots/       # Screenshot aplikasi
```

---

## 📸 Screenshots

### Tampilan Menu Utama
![main menu](screenshots/finance.png)

---

---

## 🔧 Teknologi
- Python 3.x
- JSON Storage
- CLI (Command Line Interface)

---

## 🧑‍💻 Kontribusi
Pull request selalu dipersilakan!

---

## 📜 Lisensi
Proyek ini menggunakan lisensi **MIT**.
