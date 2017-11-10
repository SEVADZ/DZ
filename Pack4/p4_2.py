def xx(st):
    if (st[len(st) - 1] != "x"):
        l = st.split("x^")
        if (len(l) > 1):
            if (int(l[1]) != 2):
                return str(int(l[0]) * int(l[1])) + "x^" + str(int(l[1]) - 1)
            else:
                return str(int(l[0]))
        else:
            return "0"
    else:
        return st.split("x")[0]
print("Введите полином одной переменной x в порядке убывания степеней (без знака умножения, без пробелов,  ^ - знак степени)")
st = input()
i = 1
l = []
l1 = []
l.append(st[0])
j = 0
ss = set("+-")
while (len(st) > i):
    if (st[i] in ss):
        j += 1
        l1.append(st[i])
        l.append(st[i+1])
        i += 2
    else:
        l[j] += st[i]
        i += 1
k = ""
for i in range(len(l1)):
    k += l[i] + l1[i]
k += l[len(l1)]
rez = ""

for i in range(len(l) - 1):
    rez += xx(l[i])
    if (i == len(l) - 2):
        pass
    else:
        rez += l1[i]
print(rez)