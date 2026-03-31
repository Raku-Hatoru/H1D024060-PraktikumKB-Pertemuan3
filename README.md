# Program Fuzzy Logic

Repository ini berisi 2 program sederhana berbasis **Fuzzy Logic** menggunakan library `scikit-fuzzy` di Python. Kedua program dibuat untuk membantu pengambilan keputusan berdasarkan beberapa variabel input yang nilainya tidak selalu pasti.

## 1. Pelayanan Masyarakat

File: `PelayananMasyarakat.py`

Program ini digunakan untuk menilai **tingkat kepuasan pelayanan masyarakat** berdasarkan beberapa faktor, yaitu:
- keamanan informasi (`ki`)
- kepuasan pelayanan (`kp`)
- kemampuan petugas (`kps`)
- ketersediaan sarana prasarana (`ks`)

Output dari program ini adalah nilai **kepuasan pelayanan** (`kpn`) dengan kategori seperti:
- tidak memuaskan
- kurang memuaskan
- cukup memuaskan
- memuaskan
- sangat memuaskan

Secara singkat, program ini memanfaatkan aturan fuzzy untuk mengubah beberapa penilaian input menjadi hasil akhir tingkat kepuasan pelayanan.

## 2. Toko Hewan

File: `TokoHewan.py`

Program ini digunakan untuk menentukan **jumlah stok makanan** pada toko hewan berdasarkan beberapa variabel:
- barang terjual
- permintaan
- harga per item
- profit

Output dari program ini adalah rekomendasi **stok makanan** dengan kategori:
- sedang
- banyak

Secara singkat, program ini membantu pemilik toko mengambil keputusan stok dengan pendekatan fuzzy agar lebih fleksibel terhadap kondisi penjualan dan permintaan.

## Cara Menjalankan

Pastikan Python sudah terpasang, lalu install dependensi berikut:

```bash
pip install numpy scikit-fuzzy matplotlib
```

Jalankan program dengan perintah:

```bash
python PelayananMasyarakat.py
python TokoHewan.py
```

Setelah dijalankan, program akan menampilkan hasil perhitungan fuzzy dan grafik visualisasi output.
