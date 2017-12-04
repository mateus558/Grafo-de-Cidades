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
		self.heap = []
		
		return 
		
	def solve(self):
		expandedNodes = 0
		branchingSum = 0
		iterations = 0
		start_time = time.time()
		self.start.setPriority(0)
		heapq.heappush(self.heap, (self.start, 0.0))
		visited = [self.start]
		
		for k, d in self.graph.items():
			for i in range(0, len(d)):
				d[i][0].setCostSoFar(100000000)
				d[i][0].setPriority(100000000)
		
		while not self.heap == []:
			state = heapq.heappop(self.heap)
			visited.append(state[0])
			#print(state[0])
			if state[0] == self.end:
				self.end = state[0]
				break
			
			iterations = iterations + 1
			
			if len(self.graph[state]) > 0:
				expandedNodes = expandedNodes + 1
			
			i = 0
			for s in self.graph[state[0]]: 
				#0 - estado; 1 - custo para chegar naquele estado 
				#Verifica se o estado nao foi visitado e o visita
				if s[0] not in visited:
					#print(s[0].getCostSoFar())
					depth = state[0].getDepth() + 1
					branchingSum = branchingSum + 1
					if state[0].getCostSoFar() + s[1] < s[0].getCostSoFar():
						#print(s)
						#print(state[0].getCostSoFar() + s[1])
						#print(s[0].getCostSoFar())
						s[0].setDepth(depth)
						s[0].setFather(state[0])
						s[0].setCostSoFar(state[0].getCostSoFar() + s[1])
						s[0].setPriority(state[0].getCostSoFar() + s[1]);
						heapq.heappush(self.heap, (s[0], state[0].getCostSoFar() + s[1]))
						self.graph[s[0]][i][0].setCostSoFar(state[0].getCostSoFar() + s[1])
				
			i = i + 1
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
				self.solution = Solution(path, cost, expandedNodes, branchFactor, len(visited), time_elapsed, iterations)
				break	
	
		return self.solution
	
