import dlb
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
l = dlb.PositionalList()
print('Введите числа через пробел')
s = input().split()
for i in s:
    l.add_last(int(i))
print('Введите v ')
v = int(input())  
def summ(x):
    i = l._header._next
    j = l._trailer._prev
    while j != i:
        if i._element + j._element == x:
            return [i._element,j._element]
        if i._element + j._element > x:
            j = j._prev
        if i._element + j._element < x:
            i = i._next
    return None
n = summ(v)
if not n:
    print(n)
else:
    print(n[0] - 1, n[1] - 1)
