def hapus_spasi_ganda(teks):
    
    return " ".join(teks.split())


teks = input("Masukkan teks dengan spasi ganda: ")
hasil = hapus_spasi_ganda(teks)


print(f"Teks setelah menghapus spasi ganda: '{hasil}'")
