data_mahasiswa = {}

def tambah():
    print("\n--- Tambah Data ---")
    nama = input("Nama      : ")
    nilai = float(input("Nilai     : "))
    data_mahasiswa[nama] = nilai
    print("Data berhasil ditambah!")

def tampilkan():
    print("\n--- Daftar Nilai Mahasiswa ---")
    if not data_mahasiswa:
        print("Belum ada data.")
    else:
        for nama, nilai in data_mahasiswa.items():
            print(f"{nama} : {nilai}")

def hapus(nama):
    print("\n--- Hapus Data ---")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus!")
    else:
        print("Nama tidak ditemukan.")

def ubah(nama):
    print("\n--- Ubah Data ---")
    if nama in data_mahasiswa:
        nilai_baru = float(input("Masukkan nilai baru: "))
        data_mahasiswa[nama] = nilai_baru
        print(f"Data '{nama}' berhasil diubah.")
    else:
        print("Nama tidak ditemukan.")

while True:
    print("\n=== MENU ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Nama yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Nama yang akan diubah: ")
        ubah(nama)
    elif pilihan == "5":
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid!")