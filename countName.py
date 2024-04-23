def hitung_jumlah_kata(kalimat):
    kata_kalimat = kalimat.split()
    jumlah_kata = len(kata_kalimat)
    return jumlah_kata

kalimat = input("Inputkan nama anda: ")
hasil = hitung_jumlah_kata(kalimat)
print("Jumlah kata dalam kalimat adalah:", hasil)
