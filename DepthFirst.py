import time 
from Solver import *
from Solution import *

class DepthFirst(Solver):
    def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
        super (DepthFirst, self).__init__(start, end, graph)
        self.stack = []
        self.visited = []
        self.maxDepth = 5

    def solve(self):
        expandedNodes = 0
        branchingSum = 0
        depth = 0
        iterations = 0
        start_time = time.time()
        self.stack.append(self.start)
        self.visited = [self.start]
        
        while (not self.stack == []):
            state = self.stack[len(self.stack)-1] #return the top
            self.stack.pop()
            
            if state == self.end:
                self.end = state
                break                        
           
            
            #acho q aqui tem problema
            iterations = iterations + 1
            for s in self.graph[state]: 
                depth = state.getDepth() + 1
                #0 - estado; 1 - custo para chegar naquele estado 
                #Verifica se o estado nao foi visitado e o visita
                if s[0] not in self.visited and depth < self.maxDepth:
                    branchingSum = branchingSum + 1
                    
                    s[0].setDepth(depth)
                    s[0].setFather(state)
                    s[0].setCostSoFar(state.getCostSoFar() + s[1])
                    
                    self.stack.append(s[0])
                    expandedNodes = expandedNodes + 1
            self.visited.append(state)

        end_time = time.time()
        time_elapsed = end_time - start_time

        return self.setSolution(self.end, iterations, branchingSum, expandedNodes, self.visited, time_elapsed)
        
