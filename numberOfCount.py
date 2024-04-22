# Question: You are given an array containing a number of integers. Write a program to count the number of positive, negative and zero numbers in the array.
# try to explain this too along with an example of the output

# sample array
arr = [-2,0,2,5,6,12,10,4]

positif = 0
negatif = 0
nol = 0

for num in arr:
    if num > 0:
        positif += 1
    elif num < 0:
        negatif += 1
    else:
        nol += 1

print("Jumlah bilangan positif:", positif)
print("Jumlah bilangan negatif:", negatif)
print("Jumlah nol:", nol)