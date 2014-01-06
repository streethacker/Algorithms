#!/usr/bin/python
#-*- coding:utf-8 -*-


__metaclass__ = type
class Object:
	def __init__(self):
		self.ID = None
		self.d = None

	def __le__(self, other):
		return self.d <= other.d

__metaclass__ = type
class Knap:
	def __init__(self):
		self.c = None	#背包容量
		self.n = None	#物品数目
		self.w = None	#物品数量数组
		self.p = None		#物品价值数组
		self.cw = None		#当前重量
		self.cp = None			#当前价值
		self.bestp = None		#当前最优价值

	def Bound(self, i):
		cleft = self.c - self.cw	#剩余容量
		b = self.cp
		#以物品单位重量价值递减序装入物品
		while i<=self.n and self.w[i] < cleft:
				cleft -= self.w[i]
				b += self.p[i]
				i += 1
		#装满背包
		if i <= self.n:
				b += self.p[i] * cleft/self.w[i]
		return b

	def Backtrack(self, i):
		if i > self.n:		#到达叶节点
				self.bestp = self.cp
				return
		if self.cw + self.w[i] <= self.c:	#进入左子树
				self.cw += self.w[i]
				self.cp += self.p[i]
				self.Backtrack(i+1)
				self.cw -= self.w[i]
				self.cp -= self.p[i]
		if self.Bound(i+1) > self.bestp:	#进入右子树
				self.Backtrack(i+1)


def Knapsack(p, w, c, n):
	W, P = 0, 0
	Q = [Object() for i in range(n)]

	for i in range(1, n+1):
			Q[i-1].ID = i
			Q[i-1].d = 1.0 * p[i]/w[i]
			P += p[i]
			W += w[i]

	if W <= c: return P
	
	Q.sort()

	K = Knap()
	K.p = [p[Q[i-1].ID] for i in range(n+1)]
	K.w = [w[Q[i-1].ID] for i in range(n+1)]
	
	K.cp, K.cw, K.c, K.n, K.bestp = 0, 0, c, n, 0

	K.Backtrack(1)

	return K.bestp

if __name__ == "__main__":
		p = [0, 9, 10, 7, 4]
		w = [0, 3, 5, 2, 1]
		n, c = 4, 7

		print "Value:%s" % Knapsack(p, w, c, n)
