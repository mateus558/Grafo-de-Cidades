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
        state.setFather(None)
        state.setDepth(0)
        iterations = 0
        start_time = time.time()
        while(not failure or not sucess):
            #enquanto nao conseguir sucesso ou fracasso ele vai pegar o "operador" do objeto
            #preciso pegar um determinado elemento da lista
            iterations = iterations + 1
            if(state == self.start):
                print(state)
                print(state.getOperator())
            if(state.getOperator() < len(self.graph[state])):
                rn = self.graph[state][state.getOperator()][0]
                for a in self.visited:
                    if(rn == a):
                        if(rn.getFather() == rn.getFather):
                            rn.increaseCostSoFar(1)	
                            rn.setDepth(state.getDepth() +1)
                            if(rn not in self.visited):
                                self.visited.append(rn)
                                rn.setFather(state)
                                state = rn
                state.setOperator(state.getOperator() + 1)
                if(state == self.end):
                    sucess = True
            else:
                if(state == self.start):
                    failure = True
                else:
                    state = state.getFather()
        end_time = time.time()
        time_elapsed = end_time - start_time
        if(sucess):
            return self.setSolution(state, iterations, 0,0, self.visited, time_elapsed)
        else:
            self.solution is None