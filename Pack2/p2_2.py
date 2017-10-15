def perf(x):
    s = 0;
    for i in range(1,x+1):
        if (x % i == 0):
            s = s + i
    return s
k = int(input())
if (perf(k) == k * 2):
    print("perfect")
else:
    print("not perfect")

