import time
from Solver import *
from Solution import *

class BreadthFirst(Solver):
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		super(BreadthFirst, self).__init__(start, end, graph)
		self.queue = []
		
	def solve(self):
		expandedNodes = 0
		branchingSum = 0
		iterations = 0
		start_time = time.time()
		self.queue.append(self.start)
		visited = [self.start]
		
		while self.queue:
			state = self.queue.pop()
			
			if state == self.end:
				self.end = state
				break
			
			expandedNodes = expandedNodes + 1
			iterations = iterations + 1
			
			for s in self.graph[state]: 
				if s[0] not in visited:
					self.queue.append(s[0])
					branchingSum = branchingSum + 1
					s[0].setFather(state)
					s[0].increaseCostSoFar(s[1])	
					visited.append(s[0])
					
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
				self.solution = Solution(path, cost, expandedNodes, (branchingSum/iterations), len(visited), time_elapsed)
				break
				
		return self.solution
