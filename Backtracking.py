import time
from Solver import *
from Solution import *


class Backtracking(Solver):
    def __init__(self, start=State(), end=State(), graph=defaultdict(list)):
        super(Backtracking, self).__init__(
            self, start, end, graph=defaultdict(list))

    def solve(self):
        self.operators = []
        sucess = False
        failure = False
        expandedNodes = 0
        branchingSum = 0
        depth = 0
        iterations = 0
        currentState = start;
        start_time = time.time()
        while(not failure or not sucess):
            # pega os filhos
            currentState.setDepth(depth)
            operators = graph[currentState]
            iterations = iterations + 1
            if(len(operators) != 0 and not operators[i].isVisited()):
                for i in range(0, len(operators) - 1):
                    if(not operators[i].isVisited()):
                        operators[i].setFather(currentState)
                        currentState = operators[i]
                        depth = depth + 1
                        expandedNodes = expandedNodes + 1
                if(currentState == end):
                    sucess = True
            else:
                if(currentState == start):
                    failure = True
                else:
                    currentState.setVisited(true)
                    currentState = currentState.getFather()
                    depth = currentState.getDepth()
        end_time = time.time()
        if(sucess):
            itr = currentState
            cost = itr.getCost()
            self.path = []
            time_elapsed = end_time - start_time
            while True:
                if itr:
                    path.append(itr)
                    itr = itr.getFather()
                else:
                    path.reverse()
                    self.solution = Solution(path, cost, expandedNodes, branchFactor, numberVisited, time_elapsed)
                    break
        else:
            self.solution = NULL
        return self.solution

    def insertionSort(self,array):
        for i in range (1, len(array)-1):
            key = array[i]
            j = i-1
            while(j>=0 and array[j].getPos()[0] > key.getPos()[0]):
                array[j+1] = array[j]
                j = j-1
            array[j+1] = key
        return array
