def konversi_suhu(nilai, dari, ke):

    # Normalisasi input agar tidak case-sensitive
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan input
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan hanya boleh 'C', 'F', atau 'K'."

    # Validasi nilai suhu untuk Kelvin
    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."

    # Jika satuan asal dan tujuan sama, kembalikan nilai aslinya
    if dari == ke:
        return nilai

    # Konversi suhu
    hasil = None
    if dari == "c":
        if ke == "f":
            hasil = (nilai * 9/5) + 32
        elif ke == "k":
            hasil = nilai + 273.15

    elif dari == "f":
        if ke == "c":
            hasil = (nilai - 32) * 5/9
        elif ke == "k":
            hasil = (nilai - 32) * 5/9 + 273.15

    elif dari == "k":
        if ke == "c":
            hasil = nilai - 273.15
        elif ke == "f":
            hasil = (nilai - 273.15) * 9/5 + 32

    return hasil