import math

x = int(input("Küçük sayıyı giriniz: "))
y = int(input("Büyük sayıyı giriniz: "))
list = []

for i in range(x, y):
    root = math.sqrt(i)
    if root % 1 == 0:
        list.append(i)

print(list)
