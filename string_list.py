def string_to_list(string):
    list = []
    num = len(string)
    i = 0
    a = 0
    while i < num:
        if string[i] == " ":
            word = string[a:i]
            list.append(word)
            a = i + 1
        elif i == num - 1:
            word = string[a : i + 1]
            list.append(word)
            a = i + 1
        i += 1
    print(list)


string_to_list("merhaba sky lab'e hoşgeldin")
