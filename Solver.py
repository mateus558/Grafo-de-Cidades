from State import *
from collections import defaultdict

class Solver:
	
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		self.start = start
		self.end = end
		self.graph = graph
		self.solution = None		
		return
			
	def read(self, file):
		f = open(file, "r")
		
		while True:
			line = f.readline()
			if not line: break
		
			res = list(map(float, line.split()))
			from_state = State(float(res[0]), float(res[1]))
			to_state = State(float(res[2]), float(res[3]))
			self.graph[from_state].append([to_state, res[4]])
		
		return self.graph
	
	
