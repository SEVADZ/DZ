def fact(x1):
    if (x1 == 0):
        return 1
    if (x1 == 1):
        return 1
    else:
        return x1*fact(x1-1)

def cxy(x, y):
    return (round(fact(x) / (fact(y) * fact(x - y))))
rows = int(input())
for i in range(rows):
    s = 1 + i
    st = ""
    for j in range(s):
        st = st + str(cxy(s - 1 ,j)) + " "
    print(st)
