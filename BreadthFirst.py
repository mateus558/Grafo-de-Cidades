from Solver import *

class BreadthFirst(Solver):
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		Solver.__init__(start, end, graph)
		self.list = []
	
	def solve(self):
		return
