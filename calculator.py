list = []
a = int(input("1. sayıyı giriniz: "))
list.append(a)
b = int(input("2. sayıyı giriniz: "))
list.append(b)
c = input("4 işlemden birini giriniz: ")
list.append(c)
print(list)

number = None
if c == "+":
    number = a + b
    print(number)
elif c == "-":
    number = a - b
    print(number)
elif c == "*":
    number = a * b
    print(number)
elif c == "/":
    number = a / b
    print(number)
else:
    print("Operator not supported.")
