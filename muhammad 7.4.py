def cari_kata_terpendek_dan_terpanjang(kalimat):
    
    kata_kata = kalimat.split()

    
    kata_terpendek = min(kata_kata, key=len)
    kata_terpanjang = max(kata_kata, key=len)

    return kata_terpendek, kata_terpanjang


kalimat = input("Masukkan sebuah kalimat: ")
kata_terpendek, kata_terpanjang = cari_kata_terpendek_dan_terpanjang(kalimat)


print(f"Kata terpendek: {kata_terpendek}")
print(f"Kata terpanjang: {kata_terpanjang}")
