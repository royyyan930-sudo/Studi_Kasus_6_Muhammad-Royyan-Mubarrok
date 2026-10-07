# Studi_Kasus_6_Muhammad-Royyan-Mubarrok

## 👤 Identitas Pembuat
- **Nama** : Muhammad Royyan Mubarrok
- **NIM**  : 2609116005
- **Prodi** : Sistem Informasi

# Sistem Pencatatan Nilai Mahasiswa (JSON)

Repositori ini dibuat untuk memenuhi tugas praktikum mata kuliah Dasar-Dasar Pemrograman. Program ini dirancang untuk merekap, melihat, dan menyimpan riwayat nilai ujian mahasiswa secara dinamis menggunakan file eksternal.

---

## Fitur Program
1. **Membaca Data (with open)**: Membaca riwayat data nilai mahasiswa secara otomatis dari file penyimpanan.
2. **Menampilkan Data**: Menyajikan rekapitulasi nilai mahasiswa ke dalam format tabel yang rapi di terminal.
3. **Menambahkan Data Baru (Append)**: Memasukkan data nilai mahasiswa baru yang langsung tersimpan secara permanen ke dalam file.
4. **Perulangan Interaktif (while loop)**: Program berjalan terus-menerus hingga pengguna memilih opsi untuk keluar.

---

## Penjelasan Kode Program
Berikut adalah penjelasan singkat mengenai fungsi-fungsi utama yang digunakan dalam program:
- **with open(...)**: Digunakan untuk membuka file secara aman (baik dalam mode baca 'r' maupun mode tambah/append 'a'). File akan otomatis tertutup dengan benar setelah blok kode selesai dieksekusi.
- **while True**: Membuat menu utama berjalan secara interaktif berulang-ulang sampai pengguna memilih menu keluar (break).
- **Penyimpanan Permanen**: Memastikan setiap data baru yang diinput oleh pengguna langsung diperbarui ke dalam file sehingga tidak hilang meskipun program ditutup.

---

## Dokumentasi / Screenshot

### 1. Tampilan Saat Program Dijalankan & Menampilkan Data
<img width="462" height="194" alt="image" src="https://github.com/user-attachments/assets/2b4694be-d1ae-4324-8b71-fe6899425508" />


### 2. Tampilan Saat Menambahkan Data Baru
<img width="458" height="176" alt="image" src="https://github.com/user-attachments/assets/24a5afc0-b129-4bd7-a054-1acda97c8ca6" />

### 3. Data sudah Tersimpan Pas kembali ke menu 1
<img width="482" height="377" alt="image" src="https://github.com/user-attachments/assets/c2557b0b-1e1e-4cbe-8adc-527e039fe721" />

### 4. Bukti Data Tetap Tersimpan secara permanen Setelah Program Dijalankan Kembali
<img width="899" height="326" alt="image" src="https://github.com/user-attachments/assets/5a6dafdd-9277-499f-bcbb-4fe991578222" />

