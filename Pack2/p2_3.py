def fact(x1):
    if (x1 == 0):
        return 1
    if (x1 == 1):
        return 1
    else:
        return x1*fact(x1-1)
def sos(q):
        return round(fact(2 * q) / (fact(q) * fact(q)))
def ots(n, m):
        o = rows // 2
        k = str(sos(o))
        
        k = k + " "
        j = len(k) - len(str(cxy(n,m)))
        if (m != 0):
            return str(cxy(n,m)) + (j) * " "
        else:
            return (" " * (((len(k) + 1 )// 2) * ((rows - 1) - n)) + str(cxy(n,m)) + (j) * " ")
def cxy(x, y):
    return (round(fact(x) / (fact(y) * fact(x - y))))
rows = int(input())
for i in range(rows):
    s = 1 + i
    st = ""
    for j in range(s):
        skk = str(ots(s - 1, j))
        st = st + skk
    print(st)
