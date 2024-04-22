x = input('Input kata:')

palindrom = True

panjang_x = len(x)

for i in range(panjang_x//2):
    if(x[i] != x[panjang_x-i-1]):
        palindrom = False
        break
    
if palindrom:
    print(x, 'Adalah palindrom')
else:
    print(x, 'Bukan palindrom')