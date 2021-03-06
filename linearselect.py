#/usr/bin/python
#-*- coding:utf-8 -*-

import random

def InsertionSort(a, p, r):
	for i in range(1, r):
			val = a[i]
			pos = i
	while pos > 0 and val < a[pos-1]:
			a[pos] = a[pos-1]
			pos -= 1

	a[pos] = val

def partition(a, p, r, x):
	i, j = p, r
	while i < j:
			if a[i] > x:
					while i < j and a[j] > x:
							j -= 1
					if i != j:
							a[i], a[j] = a[j], a[i]
							j -= 1
			i += 1
	return i-1

def LinearSelect(a, p, r, k):
	if r-p < 75:
			InsertionSort(a, p, r)
			return a[p+k-1]
	for i in range((r-p-4)/5+1):
			s, t = p+5*i, p+5*i+4
			InsertionSort(a, s, t)
			a[p+i], a[s+2] = a[s+2], a[p+i]
	
	x = LinearSelect(a, p, p+(r-p-4)/5, (r-p-4)/10)
	
	i = partition(a, p, r, x)
	j = i - p + 1
	
	if k<j:
			return LinearSelect(a, p, i, k)
	elif k==j:
			return a[j]
	else:
			return LinearSelect(a, i+1, r, k-j)

	

if __name__ == "__main__":
		array = list()
		for i in range(500):
				if i % 10 == 0:	print
				array.append(random.randint(0,1000))
				print array[i], "\t",

		print
		print
		
		k = input("Please input the rank k:")

		print "The %s(st,nd,rd or th) smallest number is: " % k, LinearSelect(array, 0, 499, k)

		
