x = int(input())
y = int(input())
st = input()
def ariph(x1,y1,op):
    if (op == "+"):
        return x1 + y1
    if (op == "-"):
        return x1 - y1
    if (op == "*"):
        return x1 * y1
    if (op == "/"):
        if ( y1 != 0 ):
            return x1 / y1
        else:
            return(print('Nе delu na 0'))
print(ariph(x,y,st))
