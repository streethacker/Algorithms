#/usr/bin/python
#-*- coding:utf-8 -*-

def MaxSum(n, a):
	subsum, b = 0, 0
	for i in range(1, n+1):
			if b>0:	b += a[i]
			else:	b = a[i]
			if b>subsum:	subsum = b
	return subsum

if __name__ == "__main__":
		a = raw_input("please input the sequence:").split()
		n = len(a)
		a.insert(0, 0)
		a = map(int, a)
	
		print "The sequence is:", [item for item in a if item != 0]
		
		print "The max subSum of the sequence is:%s" % MaxSum(n, a)
