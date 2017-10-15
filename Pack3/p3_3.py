class Ploshad(object):
    def __init__(self,vid):
        self.vid = vid
        
    def pl_kr(self):
        print('введите радиус')
        radius = int(input())
        return radius * radius * 3.14
    def pl_ch(self):
        print('введите длину')
        dl = int(input())
        print('введите ширину')
        sh = int(input())
        return dl * sh
    def plosh(self):
        if (self.vid == 'krug'):
            print(Ploshad.pl_kr(Ploshad))
        else:
            print(Ploshad.pl_ch(Ploshad))
st = str(input())
x = Ploshad(st)
x.plosh()
