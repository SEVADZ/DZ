a = []
n = int(input())
if (n < 1):
	break
for i in range(n):
    a.append(input())
a1 = []
a1.append(a.pop())
for i in range(n-1):
    a1.append(a[i])
print(a1)
