import time 
from Solver import *
from Solution import *

class DepthFirst(Solver):
    def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
        super (DepthFirst, self).__init__(start, end, graph)
        self.stack = []
        self.visited = []
        self.start.setFather(State())
        self.maxDepth = 10000

    def solve(self):
        expandedNodes = 0
        branchingSum = 0
        depth = 0
        iterations = 0
        start_time = time.time()
        self.stack.append(self.start)
        self.visited = [self.start]
        while (not self.stack == []) and (depth < self.maxDepth):
            state = self.stack[len(self.stack)-1] #return the top
            self.stack.pop()
            #acho q aqui tem problema
            i = 0
            iterations = iterations + 1
            for s in self.graph[state]: 
				#0 - estado; 1 - custo para chegar naquele estado 
				#Verifica se o estado nao foi visitado e o visita
                if s[0] not in self.visited:
                    self.stack.append(s[0])
                    depth = state.getDepth() + 1
                    branchingSum = branchingSum + 1
                    s[0].setDepth(depth)
                    s[0].setFather(state)
                    s[0].increaseCostSoFar(s[1])
                    self.graph[s[0]][i][0].increaseCostSoFar(s[1])
                    expandedNodes = expandedNodes + 1
                    self.visited.append(s[0])
            i = i+1

        end_time = time.time()
        itr = state
        cost = itr.getCost()
        path = []
        time_elapsed = end_time - start_time
        while True:
            if itr:
                path.append(itr)
                itr = itr.getFather()
            else:
                path.reverse()
                if iterations == 0:
                    branchFactor = 0
                else:
                    branchFactor = branchingSum/iterations
                    self.solution = Solution(path, cost, expandedNodes, branchFactor, len(self.visited), time_elapsed)
                    break
        return self.solution
        