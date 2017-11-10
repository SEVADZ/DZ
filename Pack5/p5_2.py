import random
import math
random.seed(version = 2)
def raz():
    for i in range(5):
        k = random.randint(1,100)
        if (k <= 11):
            return 1
    k = random.randint(1,100)
    if (k <= 11):
        return 2
    return 0
def stat(x):
    counter = [0, 0, 0]
    for i in range(x):
        counter[raz()] += 1
    for i in range(3):
        counter[i] = round(counter[i] / x,2)
    return counter
print("колво тестов")
kol = int(input())
c = stat(kol)

with open("results_2.txt", "a") as f:
    sl = "Кол-во тестов - " + str(kol) + "\n"
    f.write(sl)
    sl = "ни с кем не встретится - " + str(c[0]) + "\n"
    f.write(sl)
    sl = "с Клавдией - " + str(c[1]) + "\n"
    f.write(sl)
    sl = "с Иннокентием - " + str(c[2]) + "\n"
    f.write(sl)
    sl = "\n"
    f.write(sl)