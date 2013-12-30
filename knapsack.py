#/usr/bin/python
#-*- coding:utf-8 -*-

def Knapsack(v, w, c, n, m):
	jMax = min(w[n]-1, c)
	for j in range(jMax+1):	m[n][j] = 0
	for j in range(w[n], c+1):	m[n][j] = v[n]

	for i in range(n-1, 1, -1):
			jMax = min(w[i]-1, c)
			for j in range(jMax+1):	m[i][j] = m[i+1][j]
			for j in range(w[i], c+1):	m[i][j] = max(m[i+1][j], m[i+1][j-w[i]]+v[i])

	m[1][c] = m[2][c]

	if c>=w[1]:	m[1][c] = max(m[1][c], m[2][c-w[1]]+v[1])

def TraceBack(m, w, c, n, x):
	for i in range(1, n):
			if m[i][c] == m[i+1][c]:	x[i] = 0
			else:
					x[i] = 1
					c -= w[i]
	x[n] = 1 if m[n][c] else 0

if __name__ == "__main__":
		n, c = 5, 10
		w = [0, 2, 2, 6, 5, 4]
		v = [0, 6, 3, 5, 4, 6]

		m = [[0 for i in range(n)] for i in range(c+1)]

		x = [0 for i in range(n+1)]

		Knapsack(v, w, c, n, m)

		TraceBack(m, w, c, n, x)

		for item in x:
				print item,
