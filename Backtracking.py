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

        while(not failure or not sucess):
            #enquanto nao conseguir sucesso ou fracasso ele vai pegar o "operador" do objeto
            #preciso pegar um determinado elemento da lista
            if(state.getOperator() < len(self.graph[state])):
                rn = self.graph[state][state.getOperator()][0]
                rn.increaseCostSoFar(1)	
                state.setOperator(state.getOperator() + 1)
                self.visited.append(rn)
                rn.setFather(state)
                state = rn
                if(state == self.end):
                    sucess = True
            else:
                if(state == self.start):
                    failure = True
                else:
                    state = state.getFather()
                iterations = iterations + 1
        end_time = time.time()
        if(sucess):
            itr = state
            cost = itr.getCost()
            path = []
            time_elapsed = end_time - start_time
            while itr != self.start:
                path.append(itr)
                itr = itr.getFather()            
            path.append(self.start)
            path.reverse()
            self.solution = Solution(path, cost, 0, 0, self.visited, time_elapsed)
        else:
            self.solution is None
        return self.solution