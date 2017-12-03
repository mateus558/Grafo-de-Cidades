import time
from Solver import *
from Solution import *

class BreadthFirst(Solver):
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		super(BreadthFirst, self).__init__(start, end, graph)
		#A busca em largura usa uma fila
		self.queue = []	
		self.visited = []
		self.start.setFather(State())
		
	def solve(self):
		#inicializa variaveis
		expandedNodes = 0
		branchingSum = 0
		iterations = 0
		start_time = time.time()

		#Coloca o estado inicial para ser visitado
		self.queue.append(self.start)
		self.visited = [self.start]

		#Enquanto a fila não estiver vazia
		while not self.queue == []:
			#Pega o estado na frente da fila
			state = self.queue.pop(0)
			self.visited.append(state)
			
			#Verifica se não eh o estado terminal
			if state == self.end:
				self.end = state
				break
			
			#Atualiza o numero de estados espandidos e o numero de iteracoes
			expandedNodes = expandedNodes + 1
			iterations = iterations + 1
			
			#Para cada estado no grafo de estados
			i = 0
			for s in self.graph[state]: 
				#0 - estado; 1 - custo para chegar naquele estado 
				#Verifica se o estado nao foi visitado e o visita
				if s[0] not in self.visited:
					self.queue.insert(0, s[0])
					depth = state.getDepth() + 1
					branchingSum = branchingSum + 1
		
					s[0].setDepth(depth)
					s[0].setFather(state)
					s[0].increaseCostSoFar(s[1])	
					self.graph[s[0]][i][0].increaseCostSoFar(s[1])

			i = i + 1
		#END WHILE
					
		end_time = time.time()
		
		#Computa o caminho e prepara a solucao
		itr = self.end
		cost = itr.getCost()
		path = []
		time_elapsed = end_time - start_time
		
		while True:
			if itr:
				#Adiciona os estados no caminho a partir do estado terminal
				path.append(itr)
				itr = itr.getFather()
			else:
				path.reverse()
				
				#Verificacao para nao ocorrer divisao por 0
				if iterations == 0:
					branchFactor = 0
				else:
					branchFactor = branchingSum/iterations
				
				#Inicializa estrutura com as informacoes da solucao
				self.solution = Solution(path, cost, expandedNodes, branchFactor, len(self.visited), time_elapsed)
				break
				
		return self.solution
