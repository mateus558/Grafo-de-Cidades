from State import *
from collections import defaultdict

class Solver:
	
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		self.start = start
		self.end = end
		self.graph = graph
		
		return
			
	def read(self, file):
		f = open(file, "r")
		
		while True:
			line = f.readline()
			if not line: break
		
			res = list(map(float, line.split()))
			from_state = State(res[0], res[1])
			to_state = State(res[2], res[3])
			self.graph[from_state].append([to_state, res[4]])
		
		return self.graph
	
	def solve(self):
		return self.graph
