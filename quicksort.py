#/usr/bin/python
#-*- coding:utf-8 -*-

from random import randint

def RandomizedPartition(a, p, r):
	i = randint(p, r)
	a[i], a[p] = a[p], a[i]
	return Partition(a, p, r)

def Partition(a, p, r):
	i, j, x = p+1, r, a[p]

	while True:
			while a[i] < x and i < r:
					i += 1
			while a[j] > x:
					j -= 1
			if i >= j:	break
			a[i], a[j] = a[j], a[i]

	a[p] = a[j]
	a[j] = x

	return j

def RandomizedQuickSort(a, p, r):
	if p < r:
			q = RandomizedPartition(a, p, r)
			RandomizedQuickSort(a, p, q-1)
			RandomizedQuickSort(a, q+1, r)

if __name__ == "__main__":
		a = [11, 2, 7, 9, 4, 33, 10]
		RandomizedQuickSort(a, 0, 6)

		for item in a:
				print item,

