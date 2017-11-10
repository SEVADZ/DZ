import math
class analiz(list):
	def __init__(self, y):
		self.cmax = [0, 0]
		self.cc = 0
		self.k = set(str(y))
	def rez(self):
		l1 = str(self.cmax[1] // 10000000) + "." + str((self.cmax[1] // 1000) % 100) + "." + str((self.cmax[1] // 100000) % 100) + "." + str(self.cmax[1] % 1000)
		l2 = str(self.cmax[1] // 10000000) + "." + str((self.cmax[1] // 1000) % 100) + "." + str((self.cmax[1] // 100000) % 100 + 1) + "." + str(self.cmax[1] % 1000)
		print(l1, "to", l2)
	def ob(self, x):d
		#self.k.add(x.ex)
		if(x.ex in self.k):
			self.append(x)
			self.cc += 1#x.kol
			while (self[0].time + 1000 <= x.time):
				self.cc -= 1 #self[0].kol
				del self[0]
			if (self.cc > self.cmax[0]):
				self.cmax[0] = int(self.cc)
				self.cmax[1] = int(self[0].time)

class sdelka():
	def __init__(self, line):
		l = line.split(",")
		self.line = line
		self.time = int(str(line[0:2]) + str(line[3:5]) + str(line[6:8]) + str(line[9:12]))
		self.cost = round(float(l[2]) * 100)
		self.ex = l[3][0]
		self.kol = int(l[2])
print("ВВЕДИТЕ ВСЕ РАССМАТРИВАЕМЫЕ БИРЖИ ОДНОЙ СТРОКОЙ БЕЗ ПРОБЕЛОВ")
st = input()
with open("TRD2.csv") as f:
	l = analiz(st)
	f.readline()
	for line in f.readlines():
		l.ob(sdelka(line))
	l.rez()



