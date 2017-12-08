import time
import math
from heapq import *
from Solver import *
from Solution import *

try:
    import Queue as Q
except ImportError:
    import queue as Q

class IDAStar(Solver):
    def __init__(self, start = State(), end = State, graph = defaultdict(list)):
        super(IDAStar, self).__init__(start, end, graph)
        self.heap = Q.PriorityQueue()
        self.patamar = 0
        self.novoPatamar = 0
    
    def euclidean(self, stateA, stateB):
        posA = stateA.getPos()
        posB = stateB.getPos()
        return math.sqrt((posB[0] - posA[0]) * (posB[0] - posA[0]) + (posB[1] - posA[1]) * (posB[1] - posA[1]))
    
    def manhattan(self, stateA, stateB):
        posA = stateA.getPos()
        posB = stateB.getPos()
        return abs(posA[0] - posB[0]) + abs(posA[1] - posB[1])
    def solve(self):
        expandedNodes = 0
        branchingSum = 0
        iterations = 0
        start_time = time.time()
        self.patamar = self.euclidean(self.start, self.end)
        self.novoPatamar = math.inf
        self.start.setPriority(0)
        self.heap.put(self.start)
        visited = [self.start]
        ancester = State()
        
        while True:
            state = self.heap.get()
            print(self.patamar)
            if state == self.end:
                self.end = state
                break
            iterations = iterations + 1
            for s in self.graph[state]:
                depth = state.getDepth() + 1
                s[0].setDepth(depth)
                s[0].setFather(state)
                if s[0] not in visited and s[0] != ancester:
                    expandedNodes = expandedNodes + 1
                    branchingSum = branchingSum + 1
                    cost = state.getCostSoFar() + s[1] + self.manhattan(s[0], self.end)
                    s[0].setCostSoFar(state.getCostSoFar() + s[1])
                    if(cost <= self.patamar):
                        s[0].setPriority(cost)
                        self.heap.put(s[0])
                    else:
                        if(cost < self.novoPatamar):
                            self.novoPatamar = cost
            ancester = state
            visited.append(state)
            if(self.heap.queue == []):
                self.patamar = self.novoPatamar
                self.heap.put(self.start)
        end_time = time.time()
        time_elapsed = end_time - start_time
        return self.setSolution(self.end, iterations, branchingSum, expandedNodes, visited, time_elapsed)

