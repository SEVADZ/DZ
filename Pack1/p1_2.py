def viv(n):
    for i in range(2,n+1):
                   if (n % i == 0):
                       print(i)
    
def kol(n):
    c = 1
    for i in range(2,n+1):
                   if (n % i == 0):
                       c =c + 1
    return c
                       
