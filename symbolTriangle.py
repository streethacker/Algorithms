#!/usr/bin/python
#-*- coding:utf-8 -*-

__metaclass__ = type
class Triangle:
	def __init__(self):
		self.n = None	#第一行的符号个数
		self.half = None  #n*(n+1)/4
		self.count = None	#当前'+'号个数
		self.p = None	#符号三角形矩阵
		self.sum = None	  #已经找到的符号三角形数

	def Backtrack(self, t):
		if self.count > self.half or t*(t-1)/2-self.count > self.half: return
		if t > self.n:
				self.sum += 1
		else:
				for i in range(2):
						self.p[1][t] = i
						self.count += i
						for j in range(2, t+1):
								self.p[j][t-j+1] = self.p[j-1][t-j+1]^self.p[j-1][t-j+2]
								self.count += self.p[j][t-j+1]
						self.Backtrack(t+1)
						for j in range(2, t+1):
								self.count -= self.p[j][t-j+1]
						self.count -= i

def Compute(n):
	x = Triangle()
	x.n = n
	x.count = 0
	x.sum = 0
	x.half = n*(n+1)/2
	if x.half%2 == 1:
			return 0
	x.half = x.half/2
	x.p = [[0 for i in range(n+1)] for j in range(n+1)]

	x.Backtrack(1)
	return x.sum

if __name__ == "__main__":
		print "Total:%s" % Compute(8)

