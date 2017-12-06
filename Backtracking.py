import time
from Solver import *
from Solution import *


class Backtracking(Solver):
    def __init__(self, start=State(), end=State(), graph=defaultdict(list)):
        super(Backtracking, self).__init__(start, end, graph=defaultdict(list))
        self.visited = []
    def solve(self):
        #inicia sem sucesso e sem fracasso
        sucess = False
        failure = False
        state = self.start
        iterations = 0
        start_time = time.time()
        sol = solveAux(state, self.end, iterarions)
        end_time = time.time()
        s = sol
        while(s is not None):
            self.visited.append(s)
            s = s.getFather()
        if(sol is not None):
            return self.setSolution(self.end, iterations, 0, 0, self.visited, time_elapsed)

    def solveAux(state, end, iterations):
        iterations = iterations + 1
        if(state == end):
            return state;
        elif(len(self.graph[state]) > 0):
            for s in self.graph[state]:
                s.setFather(state)
                s.setDepth(state.getDepth() + 1)
                n = solveAux(s)
                if(n is not None):
                    return n
        else:
            return None