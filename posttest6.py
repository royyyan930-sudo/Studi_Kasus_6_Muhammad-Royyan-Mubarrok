import json
import os

nama_file = "nilai_mahasiswa.json"

def muat_data():
    if not os.path.exists(nama_file):
        return []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def simpan_data(data):
    with open(nama_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def tampilkan_data(data):
    if not data:
        print("\nBelum ada data rekap nilai mahasiswa.")
        return
    
    print("\n" + "="*60)
    print(f"{'REKAP NILAI MAHASISWA':^60}")
    print("="*60)
    print(f"{'No':<4} | {'Nama Mahasiswa':<20} | {'NIM':<12} | {'Mata Kuliah':<20} | {'Nilai':<5}")
    print("-"*60)
    
    for i, mhs in enumerate(data, start=1):
        print(f"{i:<4} | {mhs['nama']:<20} | {mhs['nim']:<12} | {mhs['mata_kuliah']:<20} | {mhs['nilai']:<5}")
    print("="*60)

def tambah_data(data):
    print("\n--- Tambah Data Rekap Nilai Baru ---")
    nama = input("Masukkan Nama Mahasiswa : ")
    nim = input("Masukkan NIM Mahasiswa  : ")
    mata_kuliah = input("Masukkan Mata Kuliah    : ")
    
    try:
        nilai = float(input("Masukkan Nilai (0-100)  : "))
    except ValueError:
        print("Error: Nilai harus berupa angka!")
        return

    data_baru = {
        "nama": nama,
        "nim": nim,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai
    }
    
    # Menambahkan data baru ke dalam list data
    data.append(data_baru)
    
    # Menyimpan kembali ke file JSON
    simpan_data(data)
    print("Sukses Data nilai mahasiswa berhasil ditambahkan dan disimpan")

def main():
    data_mahasiswa = muat_data()
    
    while True:
        print("\n--- SISTEM PENCATATAN NILAI MAHASISWA ---")
        print("1. Lihat Daftar Nilai Mahasiswa")
        print("2. Tambah Rekap Nilai Baru")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            tampilkan_data(data_mahasiswa)
        elif pilihan == "2":
            tambah_data(data_mahasiswa)
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan program ini. Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-3")

if __name__ == "__main__":
    main()
