import time
from Solver import *
from Solution import *
import math
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
		
		return math.sqrt((posB[0] - posA[0]) + (posB[1] - posA[1]))
	
	def solve():
		
		return self.solution

