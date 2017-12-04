import time 
from Solver import *
from Solution import *

class DepthFirst(Solver):
    def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
        super (DepthFirst, self).__init__(start, end, graph)
        self.queue = []
        self.visited = []
        self.start.setFather(State())
        maxDepth = 5

    def solve(self):
        expandedNodes = 0
        branchingSum = 0
        depth = 0
        iterations = 0
        start_time = time.time()
        self.queue.append(self.start)
        self.visited = [self.start]

        while (not self.queue == []) and (depth <= maxDepth):
            state = self.queue.pop()
            self.visited.append(state)
            if state == self.end:
                self.end = state
                break
            expandedNodes = expandedNodes + 1
            iterations = iterations + 1
            i = 0
            #acho q aqui tem problema
            for s in self.visited:
                self.queue.append(s[0])
                depth = state.getDepth() + 1
                branchingSum = branchingSum + 1
                s[0].setDepth(depth)
                s[0].setFather(state)
                s[0].increaseCostSFar(s[1])
                self.graph[s[0]][i][0].increaseCostSFar(s[1])
        i = i+1
        end_time = time.time()
        itr = self.end
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