# You have three variables each storing the length of a triangle's side. Write a program that determines whether a triangle with these side lengths is equilateral, isosceles, or any triangle

x = input("Sisi1:")
y = input("Sisi2:")
z = input("Sisi3:")

if x == y == z:
    print("Segitiga sama sisi")
elif x == y or x == z or y == z:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")