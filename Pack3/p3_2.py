
class Perevod(int):

    def rta(self, x):
        tbl = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
        rt = ''
        i = 0;
        while (x > 0):
            if (x - tbl[i][0] >= 0):
                rt = rt + tbl[i][1]
                x = x - tbl[i][0]
            else:
                i = i + 1
        return rt
    def atr(self, rt):
        x = 0
        i = 0
        tbl={'I':'1','IV':'4','V':'5','IX':'9','X':'10','XL':'40','L':'50','XC':'90','C':'100','CD':'400','D':'500','M':'1000'}
        while (i < len(rt) - 1):
            if(int(tbl[rt[i]]) < int(tbl[rt[i+1]])):
                x = x + int(tbl[rt[i] + rt[i+1]])
                i = i + 2
            else:
                x = x + int(tbl[rt[i]])
                i = i + 1
        if (i == len(rt) - 1):
            x = x + int(tbl[rt[i]])
        return x
    
