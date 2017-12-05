import time
import heapq
from Solver import *
from Solution import *
try:
	import Queue as Q
except ImportError:
	import queue as Q


class OrderedSearch(Solver):
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		super(OrderedSearch, self).__init__(start, end, graph)
		self.heap = Q.PriorityQueue()
		
		return 
		
	def solve(self):
		expandedNodes = 0
		branchingSum = 0
		iterations = 0
		start_time = time.time()
		self.start.setPriority(0)
		self.heap.put(self.start)
		visited = [self.start]
			
		while not self.heap.queue == []:
			state = self.heap.get()
			visited.append(state)
				
			if state == self.end:
				self.end = state
				break
			
			iterations = iterations + 1
			
			i = 0
			for s in self.graph[state]: 
				#0 - estado; 1 - custo para chegar naquele estado 
				#Verifica se o estado nao foi visitado e o visita
				if s[0] not in visited:
					depth = state.getDepth() + 1
					branchingSum = branchingSum + 1
					expandedNodes = expandedNodes + 1
				
					s[0].setDepth(depth)
					s[0].setFather(state)
					s[0].setCostSoFar(state.getCostSoFar() + s[1])
					s[0].setPriority(state.getCostSoFar());
	
					self.heap.put(s[0])
					#self.graph[s[0]][i][0].setCostSoFar(state.getCostSoFar() + s[1])
				i = i + 1
		end_time = time.time()
		time_elapsed = end_time - start_time
			
		return self.setSolution(self.end, iterations, branchingSum, expandedNodes, visited, time_elapsed)
	
	
