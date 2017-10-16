import abc
from State import *

class Solver:
	
	def __init__(self, start = State(), end = State(), graph = []):
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
			
		
		return self.graph

g = Solver()
g.read("graph.inst")
