class Skobka():
    def __init__(self, skob):
        self.skob = skob
    def check(self):
        t = True
        s = []
        while (self.skob != ''):
            if (self.skob[0] == '[' or self.skob[0] == '{' or self.skob[0] == '('):
                 s.append(self.skob[0])
                 if(len(self.skob) > 1):
                           self.skob = self.skob[1:len(self.skob)]
                 else:
                        t = False
                        break
            else:
                 if(s != []):
                           x = s.pop()
                 else:
                        t = False
        
                        break
                 if(x + self.skob[0] == '{}' or x + self.skob[0] == '()' or x + self.skob[0] == '[]'):
                       if(len(self.skob) > 1):
                           self.skob = self.skob[1:len(self.skob)]
                       else:
                           break
                 else:
                       t = False;
                       break
        if (t and s == []):
            print('norm')
        else:
            print('ploxo')

