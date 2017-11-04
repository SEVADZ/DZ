import random
class animal():
    def __init__(self, t):
        self.t = t
class fish(animal):
    def __init__(self):
        self.t = 2
    def __str__(self):
        return 'FISH'
class bear(animal):
    def __init__(self):
        self.food = 0
        self.t = 1
    def __str__(self):
        return 'BEAR'
class none(animal):
    def __init__(self):
        self.t = 0
    def __str__(self):
        return 'NONE'
class reka(list):
    def __init__(self, n, time, f, b, dd):
        random.seed(version = 2)
        self.length = n
        self.lq = []
        self.new1 = []
        self.new2 = []
        self.time = time
        self.aa = 0
        self.none = set()
        self.dd = dd
        self.extend([none()]* n)
        for i in range(self.length):
            self.none.add(i)
            self.new1.append(none())
            self.new2.append(none())
        for i in range(f):
            self.life(fish())
        for i in range(b):
            self.life(bear())
    def viv(self):
        for i in range(self.length):
            print(" " + str(self[i]) + ":" + str(i))
            print("|    |")
    def life(self, x):
        if (len(self.none) > 0):
            ls = []
            i = 0
            while(len(self.none) > 0):
                ls.append(self.none.pop())
            random.shuffle(ls)
            while(len(ls) > i):
                self.none.add(ls[i])
                i += 1
            kk = ls.pop()
            self.none.discard(kk)
            self[kk] = x
        else:
            return print("НЕТ МЕСТА ДЛЯ НОВОЙ ЖИЗНИ")
    def check(self, x):
        if (x.food >= self.dd):
            return True
        else:
            return False
    def hod(self):
        self.lq = []
        for i in range(self.length):
            self.none.add(i)
            self.new1[i] = none()
            self.new2[i] = none()
        for i in range(self.length):
            self.hod_otd(i)
        for i in range(self.length):
            if(str(self.new1[i]) != "NONE"):
                if (str(self.new2[i]) != "NONE"):
                    if ( str(self.new2[i]) == str(self.new1[i])):
                        if (self.new1[i].t == 1):
                            self.new1[i].food += 1
                            self.new2[i].food += 1
                            if (self.check(self.new1[i])):
                                if(self.check( self.new2[i])):
                                    self.none.add(i)
                                    self[i] = none()
                                else:
                                    self[i] = self.new2[i]
                            else:
                                if(self.check(self.new2[i])):
                                    self[i] = self.new1[i]
                                else:
                                    self.none.add(i)
                                    self[i] = none()
                                    self.lq.append(i)
                        if (self.new1[i].t == 2):
                            self.none.add(i)
                            self[i] = none()
                            self.lq.append(i)
                    else:
                        if(self.new1[i].t == 1):
                            self[i] = self.new1[i]
                            self[i].food = 0
                        else:
                            self[i] = self.new2[i]
                            self[i].food = 0
                else:
                    if(self.new1[i].t == 1):
                        self.new1[i].food += 1
                        if (self.check(self.new1[i])):
                            self.none.add(i)
                            self[i] = none()
                        else:
                            self[i] = self.new1[i]
                    else:
                        self[i] = self.new1[i]
            else:
                self[i] = none()
        while (self.lq != []):
            self.aa = self.lq.pop()
            self.life(self.new1[self.aa])
            self.life(self.new2[self.aa])
            if(self.new1[self.aa].t == 1):
                self.life(bear())
            else:
                self.life(fish())
                    
    def h_v(self):
        self.hod()
        self.viv()
    def hod_otd(self, i):
        if (str(self[i]) != "NONE"):
            random.seed(version = 2)
            k = random.randint(-1,1)
            if (i == 0):
                k = (k+1)//2
            if (i == self.length - 1):
                k = (k+1)//2 - 1
            if(str(self.new1[i+k]) == "NONE"):
                self.new1[i+k] = self[i]
                self.none.discard(i+k)
            else:
                if(str(self.new2[i+k]) == "NONE"):
                    self.new2[i+k] = self[i]
                else:
                    self.hod_otd(i)
    def jiza(self):
        print("ИЗНАЧАЛЬНЫЙ ВИД РЕКИ")
        print("\n")
        self.viv()
        for i in range(self.time):
            print("\n")
            self.h_v()
        
a = []
print("введите длину реки")
n = int(input())
print("ВВЕДИТЕ КОЛИЧЕСТВО РЫБ")
n1 = int(input())
print("ВВЕДИТЕ КОЛИЧЕСТВО МЕДВЕДЕЙ")
n2 = int(input())
print("время жизни реки")
time = int(input())
print("дни без еды для смерти")
dd = int(input())
c = reka(n, time, n1, n2, dd)
c.jiza()

