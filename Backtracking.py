import time
from Solver import *
from Solution import *

class Backtracking(Solver):
    def __init__(self, start=State(), end=State(), graph=defaultdict(list)):
        super(Backtracking, self).__init__(
            self, start, end, graph=defaultdict(list))
        self.queue = []
        self.sucess = False
        self.failure = False

    def solve(self):
        start_time = time.time()
        self.queue.append(self.start)  # add the initial state to the queue
        while (!self.failure or !self.sucess):
            state = self.queue.pop()
            self.queue.append(state)
            if(self.queue): 
                # choose a operator
                father = state
                state =  # new state
                #preciso verificar a operacao do estado
                # se n tiver mais operacoes remover esse estado
                if(state == end):
                    self.sucess = True
                else:
                # self.queue.append()
            else:
                self.failure = True
        end_time = time.time()
        if(self.sucess):
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
				self.solution = Solution(path, cost, time_elapsed)
				break
		else:
            self.solution = NULL
		 return self.solution

                

