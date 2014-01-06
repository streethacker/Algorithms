#!/usr/bin/python
#-*- coding:utf-8 -*-

MAXINT, INF = 65535, 65535
def Prim(n, c):
	lowcost = [None for i in range(MAXINT)]
	closest = [None for i in range(MAXINT)]
	s = [None for i in range(MAXINT)]

	s[1] = True

	for i in range(2, n+1):
			lowcost[i] = c[1][i]
			closest[i] = 1
			s[i] = False

	for i in range(1, n):
			min = INF
			j = 1
			for k in range(2, n+1):
					if lowcost[k]<min and not s[k]:
							min, j = lowcost[k], k
			print j, closest[j]

			s[j] = True

			for k in range(2, n+1):
					if c[j][k] < lowcost[k] and not s[k]:
							lowcost[k], closest[k] = c[j][k], j

if __name__ == "__main__":
		n = 6
		c = [[INF for i in range(n+1)] for j in range(n+1)]

		c[1][2] = c[2][1] = 6
		c[1][3] = c[3][1] = 1
		c[1][4] = c[4][1] = 5
		c[2][3] = c[3][2] = 5
		c[2][5] = c[5][2] = 3
		c[3][4] = c[4][3] = 5
		c[3][5] = c[5][3] = 6
		c[3][6] = c[6][3] = 4
		c[4][6] = c[6][4] = 2
		c[5][6] = c[6][5] = 6
		c[1][1] = c[2][2] = c[3][3] = c[4][4] = c[5][5] = c[6][6] = 0

		Prim(n, c)
