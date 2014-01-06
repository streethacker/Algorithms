#!/usr/bin/python
#-*- coding:utf-8 -*-

from heapq import *

__metaclass__ = type
class JobNode:
	def __init__(self):
		self.ID = None
		self.time = None

	def __lt__(self, other):
		return self.time < other.time
	def __gt__(self, other):
		return self.time > other.time

	def __le__(self, other):
		return self.time <= other.time
	def __ge__(self, other):
		return self.time >= other.time

	def __eq__(self, other):
		return self.time == other.time

__metaclass__ = type
class MachineNode:
	def __init__(self):
		self.ID = None
		self.avail = None

	def __lt__(self, other):
		return self.avail < other.avail
	def __gt__(self, other):
		return self.avail > other.avail

	def __le__(self, other):
		return self.avail <= other.avail
	def __ge__(self, other):
		return self.avail >= other.avail

	def __eq__(self, other):
		return self.avail == other.avail

def Greedy(a, n, m):
	if n <= m:
			print "为每个作业分配一台机器。"
			return
	
	jobnode = a.pop(0)
	a.sort()
	a.insert(0, jobnode)

	MachHeap = []
	heapify(MachHeap)
	for i in range(1, m+1):
			x = MachineNode()
			x.avail = 0
			x.ID = i
			heappush(MachHeap, x)

	for i in range(n, 0, -1):
			x = heappop(MachHeap)
			print "将机器", x.ID, "从", x.avail, "到", (x.avail + a[i].time), "的时间段分配给作业", a[i].ID
			x.avail += a[i].time
			heappush(MachHeap, x)


if __name__ == "__main__":
		a = [JobNode() for i in range(6)]
		for i in range(1, len(a)):
				a[i].ID = i

		a[1].time, a[2].time, a[3].time, a[4].time, a[5].time = 300, 120, 55, 70, 90

		Greedy(a, 5, 3)
