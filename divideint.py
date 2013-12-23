#/usr/bin/python
#-*- coding:utf-8 -*-

def DivideInteger(n, m):
	if n<1 or m<1:	return 0
	if n==1 or m==1:	return 1
	if n<m:	return DivideInteger(n,n)
	if n==m:	return DivideInteger(n, n-1)+1
	return DivideInteger(n, m-1) + DivideInteger(n-m, m)

if __name__ == "__main__":
		n, m = input("n:"), input("m:")

		print "n=%s, m=%s:\n" % (n, m)
		print DivideInteger(n, m)
