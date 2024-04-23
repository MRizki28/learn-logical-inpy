def huruf_terbanyak(kalimat):
    frekuensi = {}
    
    for huruf in kalimat:
        if huruf in frekuensi:
            frekuensi[huruf] += 1
        else:
            frekuensi[huruf] = 1
    
    huruf_terbanyak = max(frekuensi, key=frekuensi.get)
    
    return huruf_terbanyak


kalimat = input('INput kalimat anda: ')
print(huruf_terbanyak(kalimat))