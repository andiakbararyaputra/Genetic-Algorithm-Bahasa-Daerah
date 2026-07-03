# Genetic Algorithm Bahasa Daerah (Aceh)

Universitas Muhammadiyah Makassar  
Program Studi Teknik Informatika  
Tugas Rekayasa Komputasional  
Nama: Andi Akbar Arya Putra  
NIM: 105841117924  
Kelas: 4-F

## Tujuan Proyek
Membangun aplikasi **console/CLI** untuk simulasi **Algoritma Genetika (Genetic Algorithm)** dalam pencarian kata pada kamus bahasa daerah **Aceh**.

## Fitur Utama
- Dataset kamus Aceh (kata + arti Indonesia) lebih dari 10 entri.
- Pencarian kata (Aceh maupun Indonesia).
- Simulasi GA string untuk mendekati kata target dari kamus.
- Tampilan detail setiap tahap GA: populasi, fitness, roulette selection, crossover, mutasi, dan generasi baru.
- Menu interaktif 1–10 sesuai kebutuhan tugas.

## Struktur Proyek
- `ga_kamus_aceh.py` — aplikasi utama CLI dan logika Genetic Algorithm.
- `README.md` — dokumentasi proyek.

## Dataset Kamus Bahasa Aceh
Dataset disimpan langsung di kode sebagai pasangan kata **Aceh -> Indonesia**:
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

## Prasyarat
- Python 3.x

## Cara Menjalankan Program
```bash
cd Genetic-Algorithm-Bahasa-Daerah
python3 ga_kamus_aceh.py
```

## Daftar Menu CLI
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

## Alur Genetic Algorithm (1 Generasi Penuh)
Untuk target kata Aceh yang dipilih, proses berjalan sebagai berikut:
1. **Inisialisasi Populasi**  
   Membuat beberapa individu string acak dengan panjang sama seperti target.
2. **Hitung Fitness**  
   Fitness dihitung dari jumlah karakter yang cocok pada posisi yang sama.
3. **Seleksi Roulette**  
   Pemilihan individu berdasarkan probabilitas proporsional fitness.
4. **Crossover**  
   Dua parent ditukar sebagian gennya di titik potong acak untuk menghasilkan anak.
5. **Mutasi**  
   Karakter pada anak dapat berubah acak sesuai mutation rate.
6. **Generasi Baru & Evaluasi**  
   Populasi baru ditampilkan, lalu dihitung kembali nilai fitness-nya.

## Contoh Alur Demo Penggunaan
1. Pilih menu `1` untuk melihat kamus.
2. Pilih menu `2`, lalu masukkan kata (contoh: `kopi`) agar target menjadi `kupi`.
3. Pilih menu `3` untuk menjalankan GA satu generasi lengkap.
4. Pilih menu `4`–`9` untuk melihat rincian tiap tahap.
5. Pilih menu `10` untuk keluar program.

## Catatan Presentasi
Saat demo, tampilkan urutan:
1) pemilihan target kata,  
2) proses satu generasi GA,  
3) evaluasi fitness populasi baru.  
Urutan ini menunjukkan semua komponen wajib tugas sudah terpenuhi.
