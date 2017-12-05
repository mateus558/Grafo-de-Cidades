import time
import math
from heapq import *
from Solver import *
from Solution import *

try:
	import Queue as Q
except ImportError:
	import queue as Q

class AStar(Solver):
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		super(AStar, self).__init__(start, end, graph)
		self.heap = Q.PriorityQueue()
	
	def heuristic(self, stateA, stateB):
		posA = stateA.getPos()
		posB = stateB.getPos()
		
		return math.sqrt((posB[0] - posA[0])*(posB[0] - posA[0]) + (posB[1] - posA[1])*(posB[1] - posA[1]))
	
	def solve(self):
		expandedNodes = 0
		branchingSum = 0
		iterations = 0
		start_time = time.time()
		self.start.setPriority(0)
		self.heap.put(self.start)
		visited = [self.start]
		
		while not self.heap == []:
			state = self.heap.get()
			
			if state == self.end:
				self.end = state
				break
			
			iterations = iterations + 1		
			
			i = 0
			for s in self.graph[state]:
				expandedNodes = expandedNodes + 1
				depth = state.getDepth() + 1
				
				if s[0] not in visited:
					branchingSum = branchingSum + 1
					cost = s[1] + self.heuristic(state, s[0])

					s[0].setDepth(depth)
					s[0].setFather(state)
					s[0].increaseCostSoFar(s[1])
					s[0].setPriority(cost)
					self.heap.put(s[0])
				i = i+1
			visited.append(state)
		end_time = time.time()
		time_elapsed = end_time - start_time
		
		return self.setSolution(self.end, iterations, branchingSum, expandedNodes, visited, time_elapsed)

