import time
from Solver import *
from Solution import *


class Backtracking(Solver):
    def __init__(self, start=State(), end=State(), graph=defaultdict(list)):
        super(Backtracking, self).__init__(start, end, graph=defaultdict(list))
        self.visited = []
        self.iteration = 0
        self.branchingsums = 0

    def solveAux(self, state):
        print(state)
        self.visited.append(state)
        self.iterations = self.iterations +1
        if(state == self.end):
            self.end = state
            return state
        elif(len(self.graph[state]) > 0):
            for i in range(0,len(self.graph[state])):
                self.branchingsums = self.branchingsums + 1
                self.graph[state][i][0].setFather(state)
                self.graph[state][i][0].setDepth(state.getDepth() + 1)
                st = self.solveAux(self.graph[state][i][0])
                if(st is not None):
                    return st
            return None
        else:
            return None
    def solve(self):
        #inicia sem sucesso e sem fracasso
        sucess = False
        failure = False
        state = self.start
        self.iterations = 0
        start_time = time.time()
        sol = self.solveAux(self.start)
        end_time = time.time()
        time_elapsed = end_time - start_time
        return self.setSolution(self.end, self.iterations, branchingSum/iterations, 0, self.visited, time_elapsed)

   