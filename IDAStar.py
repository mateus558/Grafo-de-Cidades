import time
import math
from heapq import *
from Solver import *
from Solution import *

# try:
# 	import Queue as Q
# except ImportError:
# 	import queue as Q

class IDAStar(Solver):
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		super(IDAStar, self).__init__(start, end, graph)
		self.path = []
		self.bound = -math.inf
		self.found = False
		self.f = math.inf

	def euclidean(self, stateA, stateB):
		posA = stateA.getPos()
		posB = stateB.getPos()
		
		return math.sqrt((posB[0] - posA[0])*(posB[0] - posA[0]) + (posB[1] - posA[1])*(posB[1] - posA[1]))
	
	def manhattan(self, stateA, stateB):
		posA = stateA.getPos()
		posB = stateB.getPos()
		
		return abs(posA[0] - posB[0]) + abs(posA[1] - posB[1])
	def solve(self):
		self.bound  = self.euclidean(self.start, self.end)
		self.path.append(self.start)
		success = False
		
		while True:
			self.found = False 
			t = self.search(self.path, 0, self.bound)
			if(self.found == True):
				success = True
				break
			if(t == math.inf):
				success = False
				break
			self.bound = t
		print(self.path)
		
		return self.setSolution(self.end, 0, 0, 0, [], 0)
 
	def search(self, path, g, bound):
		state = path[len(self.path)-1]
		self.f  = g + self.euclidean(state, self.end)
		if (self.f > self.bound):
			self.bound = self.f
			return self.f
		if(self.end == state):
			self.found = True
			return 
		minim = math.inf
		for s in self.graph[state]:
			if s[0] not in path:
				s[0].setCostSoFar(state.getCostSoFar() + s[1])
				path.append(s[0])
				s[0].setFather(state)
				self.found = False
				t = self.search(path,g + s[1], self.bound)
				if(self.found == True):
					self.found = True
					return 
				if (t < minim):
					minim = t
				path.pop()
		return minim


                
        
