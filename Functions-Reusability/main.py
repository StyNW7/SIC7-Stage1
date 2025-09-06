from utils import konversi_suhu

print("=== KONVERSI SUHU ===")

try:
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ").strip()
    ke = input("Ke satuan (C/F/K): ").strip()

    hasil = konversi_suhu(nilai, dari, ke)

    # Cek jika hasil berupa error string
    if isinstance(hasil, str):
        print(hasil)
    else:
        print(f"Hasil: {nilai}°{dari.upper()} = {hasil:.1f}°{ke.upper()}")

except ValueError:
    print("Error: Nilai suhu harus berupa angka.")