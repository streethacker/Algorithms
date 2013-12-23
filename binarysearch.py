#/usr/bin/python
#-*- coding:utf-8 -*-

def BinarySearch(arr, size, target):
	low, high = 0, size-1

	while low <= high:
			mid = (low+high)/2
			if target == arr[mid]:	return mid
			elif target < arr[mid]:
					high = mid - 1
			else:
					low = mid + 1

	return -1

def AdvancedBinarySearch(arr, size, target):
	low, high = 0, size-1

	while low <= high:
			mid = (low+high)/2
			if target == arr[mid]:
					i = j = mid
					return (i, j, mid)
			elif target < arr[mid]:
					high = mid - 1
			else:
					low = mid + 1

	i = -1 if target <= arr[0] else high
	j = -1 if target >= arr[size-1] else low
	
	return (i, j, -1)

if __name__ == "__main__":
		import random 
		array = list()
		for i in range(10):
				array.append(random.randint(0, 100))

		array.sort()

		for element in array:
				print element,

		target = input("\ntarget:")

	#	position = BinarySearch(array, len(array), target)
		
		result = AdvancedBinarySearch(array, len(array), target)

	#	print "not found" if position == -1 else "Position:",position


		print "not found.\nmax:%s\nmin:%s" % (result[0], result[1]) if result[2] == -1 else "found.\nposition:%s" % result[2]
