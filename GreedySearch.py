import time
import math
from Solver import *
from Solution import *
try:
	import Queue as Q
except ImportError:
	import queue as Q


class GreedySearch(Solver):
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		super(GreedySearch, self).__init__(start, end, graph)
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
		self.start.setPriority(0.0)
		self.heap.put(self.start)
		visited = [self.start]
		ancester = State()
		
		while not self.heap.empty():
			state = self.heap.get()
			if state == self.end:
				self.end = state
				break
			
			iterations = iterations + 1
			
			for s in self.graph[state]: 
				if s[0] not in visited and s[0] != ancester:
					expandedNodes = expandedNodes + 1
					depth = state.getDepth() + 1
					branchingSum = branchingSum + 1
					h = self.heuristic(s[0], self.end)
					
					s[0].setDepth(depth)
					s[0].setFather(state)
					s[0].setCostSoFar(state.getCostSoFar() + s[1])
					s[0].setPriority(h)	
					
					self.heap.put(s[0])
			visited.append(state)
			ancester = state
		end_time = time.time()
		
		itr = self.end
		time_elapsed = end_time - start_time
				
		return self.setSolution(self.end, iterations, branchingSum, expandedNodes, visited, time_elapsed)

