import random

angka = {}

for i in range(1, 101):
    angka[i] = i
    

angka_acak = random.choice(list(angka.keys()))
print(angka_acak)


while True:
    x = int(input("Tebak angka antara 1 sampai 100: "))
    if x < angka_acak:
        print("Terlalu kecil")
    elif x > angka_acak:
        print("Terlalu Besar")
    else:
        print("Yess Tebakan anda benar" , angka_acak)
        break