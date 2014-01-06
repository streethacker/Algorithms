#/usr/bin/python
#-*- coding:utf-8 -*-

def LCSLength(x, y, m, n, c, b):
	for i in range(1, m+1):	c[i][0] = 0
	for j in range(1, n+1):	c[0][j] = 0
	for i in range(1, m+1):
			for j in range(1, n+1):
					if x[i]==y[j]:
							c[i][j] = c[i-1][j-1] + 1
							b[i][j] = 1
					elif c[i-1][j]>=c[i][j-1]:
							c[i][j] = c[i-1][j]
							b[i][j] = 2
					else:
							c[i][j] = c[i][j-1]
							b[i][j] = 3

def LCS(i, j, x, b):
	if i==0 or j==0:	return
	if b[i][j]==1:
			LCS(i-1, j-1, x, b)
			print x[i],
	elif b[i][j]==2:
			LCS(i-1, j, x, b)
	else:
			LCS(i, j-1, x, b)

if __name__ == "__main__":
		x = raw_input("please input the first sequence:")
		y = raw_input("please input the second sequence:")

		m, n = len(x), len(y)

		seqX = []
		seqY = []

		seqX.append(0)
		for item in x:
				seqX.append(item)
		seqY.append(0)
		for item in y:
				seqY.append(item)

		c = [[0 for i in range(n+1)] for i in range(m+1)]

		b = [[0 for i in range(n+1)] for i in range(m+1)]

		LCSLength(seqX, seqY, m, n, c, b)
		print "The longest length of the sequence:%s" % c[m][n]
		print "The longest common sequence:"
		LCS(m, n, seqX, b)
