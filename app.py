mahasiswa = []

def tambah(nama, nilai):
    """Menambah data mahasiswa"""
    mahasiswa.append({"nama": nama, "nilai": nilai})

def tampilkan():
    """Menampilkan semua data mahasiswa"""
    if not mahasiswa:
        print("Belum ada data.")
        return
    print("\nDaftar Nilai Mahasiswa:")
    for mhs in mahasiswa:
        print(f"- {mhs['nama']} : {mhs['nilai']}")

def hapus(nama):
    """Menghapus data berdasarkan nama"""
    for mhs in mahasiswa:
        if mhs["nama"].lower() == nama.lower():
            mahasiswa.remove(mhs)
            print(f"{nama} berhasil dihapus.")
            return
    print("Nama tidak ditemukan.")

def ubah(nama, nama_baru=None, nilai_baru=None):
    """Mengubah data berdasarkan nama"""
    for mhs in mahasiswa:
        if mhs["nama"].lower() == nama.lower():
            if nama_baru:
                mhs["nama"] = nama_baru
            if nilai_baru is not None:
                mhs["nilai"] = nilai_baru
            print("Data berhasil diubah.")
            return
    print("Nama tidak ditemukan.")

# Contoh penggunaan program
tambah("Dimas", 90)
tambah("Siti", 85)
tampilkan()
ubah("Siti", nilai_baru=95)
hapus("Dimas")
tampilkan()