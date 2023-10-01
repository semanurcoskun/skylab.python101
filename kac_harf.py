def kacharf(string1, string2):
    num1 = len(string1)
    num2 = len(string2)
    mylist = []
    for i in range(0, num1):
        kac = 0
        for j in range(0, num2):
            if string1[i] == string2[j]:
                kac += 1
        if kac != 0:
            mylist.append(string1[i] + "," + str(kac))
        kac = 0
    list2 = list(set(mylist))
    print(list2)


string1 = "araba"
string2 = "anahtar"
kacharf(string2, string1)
