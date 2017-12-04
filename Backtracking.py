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
            if(not self.graph[state][state.getOperator()] is None):
                rn = self.graph[state][state.getOperator()]
                rn.increaseCostSoFar(rn[1])	
                state.setOperator(state.getOperator() + 1)
                visited.append(rn)
                rn.setFather(state)
                state = rn
                if(state == end):
                    sucess = True
            if(state == self.start):
                failure = True
            else:
                state = state.getFather()
            iterations = iterations + 1
        end_time = time.time()
        if(sucess):
            itr = state
            cost = itr.getCost()
            self.path = []
            time_elapsed = end_time - start_time
            while True:
                if itr:
                    path.append(itr)
                    itr = itr.getFather()
                else:
                    path.reverse()
                    self.solution = Solution(path, cost, expandedNodes, branchFactor, visited, time_elapsed)
                    break
        else:
            self.solution is None
        return self.solution