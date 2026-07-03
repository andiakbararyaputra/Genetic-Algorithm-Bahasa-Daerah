# Genetic Algorithm Bahasa Daerah (Aceh)

Universitas Muhammadiyah Makassar  
Program Studi Teknik Informatika  
Tugas Rekayasa Komputasional  
Nama: Andi Akbar Arya Putra  
NIM: 105841117924  
Kelas: 4-F

## Deskripsi Singkat
Proyek ini adalah aplikasi console/CLI untuk simulasi **Algoritma Genetika (Genetic Algorithm)** dalam pencarian kata pada kamus bahasa daerah Aceh.

Program menyediakan menu interaktif untuk menampilkan kamus, mencari kata, dan menjalankan proses GA satu generasi penuh (fitness, roulette selection, crossover, mutasi, lalu evaluasi populasi baru).

## Struktur Proyek
- `ga_kamus_aceh.py` : aplikasi utama CLI dan logika Genetic Algorithm.
- `README.md` : dokumentasi proyek.

## Dataset Kamus Bahasa Aceh
Dataset disimpan langsung di kode sebagai list sederhana berisi pasangan kata **Aceh -> Indonesia**.

Contoh entri:
- peugah = berkata
- jak = pergi
- pue = apa
- soe = siapa
- rumoh = rumah
- bu = nasi
- ie = air
- sira = garam
- manok = ayam
- kupi = kopi
- droeneuh = kamu
- lon = saya

Total: **12 kata** (lebih dari syarat minimal 10 kata).

## Cara Menjalankan
Pastikan Python 3 tersedia.

```bash
cd Genetic-Algorithm-Bahasa-Daerah
python3 ga_kamus_aceh.py
```

## Menu Program
Saat dijalankan, program menampilkan menu:
1. Tampilkan Kamus
2. Cari Kata
3. Jalankan Algoritma Genetika
4. Tampilkan Populasi
5. Nilai Fitness
6. Seleksi Roulette
7. Cross Over
8. Mutasi
9. Generasi Baru
10. Keluar

## Cara Kerja Algoritma Genetika (1 Generasi)
Untuk target kata Aceh yang dipilih:
1. **Inisialisasi Populasi**: membangkitkan individu string acak dengan panjang sama seperti target.
2. **Hitung Fitness**: skor berdasarkan jumlah karakter yang cocok pada posisi yang sama.
3. **Seleksi Roulette**: memilih individu berdasarkan peluang proporsional nilai fitness (dengan penyesuaian +1 agar tidak nol).
4. **Crossover**: pasangan parent ditukar sebagian gennya di titik potong acak.
5. **Mutasi**: gen pada anak diubah acak sesuai mutation rate.
6. **Generasi Baru + Evaluasi**: menampilkan populasi baru dan nilai fitness-nya.

## Contoh Alur Penggunaan
1. Pilih menu `1` untuk melihat kamus.
2. Pilih menu `2`, masukkan kata (misal: `kopi`) agar target menjadi kata Aceh `kupi`.
3. Pilih menu `3` untuk menjalankan GA satu generasi penuh.
4. Gunakan menu `4` sampai `9` untuk melihat detail setiap tahap.
5. Pilih menu `10` untuk keluar.
