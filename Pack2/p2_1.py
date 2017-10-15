import time
def rf1(x):
    if (x < 2 and x >= 0):
        return 1
    else:
        if (x > 0):
            return x*rf1(x-1)
        else:
            return 'нельзя'
def rf(x):
    vr1 = time.time()
    print(rf1(x))
    vr2 = time.time()
    print('время выполнения рекурентной',vr2 - vr1)
    ''' это 1 а не l(L)'''
def nrf(x):
    vr1 = time.time()
    s = 1
    for i in range(1,x+1):
        s = s * i
    print(s)
    vr2 = time.time()
    print('время выполнения нерекурентной',vr2 - vr1)
