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
        currentState = start;
        start_time = time.time()
        while(!failure or !sucess):
            # pega os filhos
            if(len(operators) != 0 and !operators[i].isVisited()):
                for i in range(0, len(operators) - 1):
                    if(!operators[i].isVisited()):
                        operators[i].setFather(currentState)
                        currentState = operators[i]
                if(currentState == end):
                    sucess = True
            else:
                if(currentState == start):
                    failure = True
                else:
                    currentState = currentState.getFather()
        end_time = time.time()
        if(sucess):
            itr = currentState
            cost = itr.getCost()
		    path = []
            time_elapsed = end_time - start_time
            while True:
			if itr:
				path.append(itr)
				itr = itr.getFather()
			else:
				path.reverse()
				self.solution = Solution(path, cost, time_elapsed)
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