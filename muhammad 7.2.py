def hitung_kata_kunci(teks, kata_kunci):
    
    teks = teks.lower()
    kata_kunci = kata_kunci.lower()

    
    jumlah_kemunculan = teks.count(kata_kunci)

    return jumlah_kemunculan


teks_berita = input("Masukkan teks berita: ")
kata_kunci = input("Masukkan kata kunci yang ingin dihitung: ")


jumlah = hitung_kata_kunci(teks_berita, kata_kunci)


print(f"Kata '{kata_kunci}' muncul sebanyak {jumlah} kali dalam teks berita.")
