x = int(input("bir sayi giriniz: "))
y = int(input("bir sayi giriniz: "))
z = int(input("bir sayi giriniz: "))

if (x == y) and (x == z):
    print("eşkenar üçgen")
elif (x == y) or (x == z):
    print("ikizkenar üçgen")
else:
    print("çeşitkenar üçgen")
