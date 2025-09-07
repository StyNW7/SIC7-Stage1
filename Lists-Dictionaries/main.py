# 1. Buat list nama siswa
siswa = ["Andi", "Budi", "Citra", "Dewi", "Eka"]

# 2. Buat dictionary nilai siswa
nilai_siswa = {
    "Andi": 85,
    "Budi": 90,
    "Citra": 78,
    "Dewi": 88,
    "Eka": 92
}

print("=== DATA AWAL ===")
print("List siswa:", siswa)
print("Dictionary nilai siswa:", nilai_siswa)

# 3. Tugas:
print("\n=== TUGAS ===")

# a) Tambahkan satu nama siswa baru ke akhir list siswa
siswa.append("Fajar")
print("Setelah menambah Fajar:", siswa)

# Hapus satu siswa tertentu dari list
siswa.remove("Citra")
print("Setelah menghapus Citra:", siswa)

# b) Cetak nama siswa pertama dan terakhir dari list, lalu cetak 3 siswa terakhir dengan slicing
print("Siswa pertama:", siswa[0])
print("Siswa terakhir:", siswa[-1])
print("3 siswa terakhir:", siswa[-3:])

# c) Gunakan for loop untuk mencetak index dan nama siswa
print("\nDaftar siswa dengan index:")
for i, nama in enumerate(siswa):
    print(f"{i}: {nama}")

# d) Ubah nilai ujian salah satu siswa di dictionary
nilai_siswa["Andi"] = 95
print("\nSetelah mengubah nilai Andi:", nilai_siswa)

# Hapus data nilai siswa lain menggunakan pop()
nilai_siswa.pop("Citra", None)  # pakai None agar tidak error jika sudah dihapus dari list
print("Setelah menghapus nilai Citra:", nilai_siswa)

# e) Ganti key nama siswa tertentu di dictionary
# Misalnya ganti "Budi" menjadi "Bagus"
nilai_siswa["Bagus"] = nilai_siswa.pop("Budi")
print("Setelah mengganti key Budi -> Bagus:", nilai_siswa)