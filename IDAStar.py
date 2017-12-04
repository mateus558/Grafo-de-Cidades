import math
import time

from Solution import *
from Solver import *

try:
    import Queue as Q
except ImportError:
    import queue as Q

class IDAStar(Solver):
    def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
        super(IDAStar, self).__init__(start, end, graph)
        self.heap = Q.PriorityQueue()

    def heuristic(self, stateA, stateB):
        posA = stateA.getPos()
        posB = stateB.getPos()
        return math.sqrt((posB[0] - posA[0])*(posB[0] - posA[0]) + (posB[1] - posA[1])*(posB[1] - posA[1]))

    def solve(self):
        failure = False
        sucess = False
        state = start
        fs = heuristic()
