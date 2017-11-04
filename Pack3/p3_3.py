class Ploshad():
    def plosh(self, x, y, st):
        if (st == "krug"):
            print(x*y*3.14)
        if (st == "pryam"):
            print(x*y)
class krug(Ploshad):
    def __init__(self, rad):
        self.rad = rad
    def __str__(self):
        return "krug"
class pryam(Ploshad):
    def __init__(self, length, width):
        self.l = length
        self.w = width
    def __str__(self):
        return "pryam"
print("круг или прямоугольник? (k / p)")
st = str(input())
if (st == "p"):
    print("Введите длину и ширину")
    s = pryam(int(input()),int(input()))
    s.plosh(s.l, s.w, str(s))
if (st == "k"):
    print("введите радиус")
    s = krug(int(input()))
    s.plosh(s.rad, s.rad, str(s))
