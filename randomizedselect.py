#/usr/bin/python
#-*- coding:utf-8 -*-

import quicksort

def RandomizedSelect(a, p, r, k):
	if p == r: return a[p]
	i = quicksort.RandomizedPartition(a, p, r)
	j = i - p + 1
	if k <= j:
			return RandomizedSelect(a, p, i, k)
	else:
			return RandomizedSelect(a, i+1, r, k)

if __name__ == "__main__":
	a = [11, 2, -8, 3, 100, 77, -3, 10, 35, 80, -2, 2]
	print RandomizedSelect(a, 0, 11, 1)		
