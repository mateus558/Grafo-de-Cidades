import time
import math
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
		res = (posB[0] - posA[0]) + (posB[1] - posA[1])
		if res < 0: res = res * -1
		return math.sqrt(res)
	
	def solve(self):
		expandedNodes = 0
		branchingSum = 0
		iterations = 0
		start_time = time.time()
		self.start.setPriority(0)
		self.heap.put(self.start)
		visited = [self.start]
		
		while not self.heap.empty():
			state = self.heap.get()
			visited.append(state)
			
			if state == self.end:
				self.end = state
				break
			
			expandedNodes = expandedNodes + 1
			iterations = iterations + 1

			i = 0
			for s in self.graph[state]: 
				if s[0] not in visited:
					cost = s[1] + self.heuristic(state, s[0])
					
					depth = state.getDepth() + 1
					branchingSum = branchingSum + 1

					s[0].setDepth(depth)
					s[0].setFather(state)
					s[0].increaseCostSoFar(s[1])
					s[0].setPriority(cost)
					self.heap.put(s[0])
					self.graph[s[0]][i][0].increaseCostSoFar(s[1])
					
			i = i+1
		
		end_time = time.time()
		itr = self.end
		cost = itr.getCost()
		path = []
		time_elapsed = end_time - start_time
		
		while True:
			if itr:
				path.append(itr)
				itr = itr.getFather()
			else:
				path.reverse()
				if iterations == 0:
					branchFactor = 0
				else:
					branchFactor = branchingSum/iterations
				self.solution = Solution(path, cost, expandedNodes, branchFactor, len(visited), time_elapsed)
				break
		
		return self.solution

