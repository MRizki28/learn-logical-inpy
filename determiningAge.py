# Question: Suppose you have an age variable that stores a person's age. Create a program that determines whether a person is a child (under 12 years of age), a teenager (between 12 and 18 years of age), an adult (between 18 and 60 years of age), or an elderly person (over 60 years of age).

age = {}

for i in range(1,101):
    age[i] = i
    
personAge = int(input("Input umur anda :"))

if personAge < 12:
    print("Seorang anak")
elif 12 <= personAge <= 18:
    print("Seorang remaja")
elif 18 < personAge < 60:
    print("Seorang dewasa")
else:
    print("Seorang lansia")

