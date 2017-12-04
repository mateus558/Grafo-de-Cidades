from sys import platform
import os
import argparse

from Solver import *
from Backtracking import *
from BreadthFirst import *
from DepthFirst import *
from OrderedSearch import *
from AStar import *
from GreedySearch import *

parser = argparse.ArgumentParser()
parser.add_argument('--instance', help='Instance of the city graph to be solved.')
parser.add_argument('--method', help='Method to solve the problem.')
parser.add_argument('--x', help='')
parser.add_argument('--y', help='')
parser.add_argument('--x1', help='')
parser.add_argument('--y1', help='')
args = parser.parse_args()

start = None
end = None

def wait():
    input("\nPress enter to continue...")

def clear():
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "darwin":
		os.system('clear')
	elif platform == "win32":
		os.system('cls')
	return 

def enterObjective():
	x, y = map(float, input("Enter the initial state: ").split())
	start = State(x, y)

	x1, y1 = map(float, input("Enter the terminal state: ").split())
	end = State(x1, y1)
	print(end)
	return 
	
def selectMethod(solver):
	print("1 - Backtracking")
	print("2 - Breadth First Search")
	print("3 - Depth First Search (limited)")
	print("4 - Ordered Search")
	print("5 - Greed Search")
	print("6 - A* Search")
	print("7 - IDA* Search")
	
	o = int(input("> "))
	enterObjective()
	if o == 1:
		solver = Backtracking(start, end)
	if o == 2:
		solver = Solver() #BreadthFirst(start, end)
	if o == 3:
		solver = DepthFirst(start, end)
	if o == 4:
		solver = OrderedSearch(start, end)
	if o == 5:
		solver = GreedySearch(start, end)
	if o == 6:
		solver = AStar(start, end)
	if o == 7:
		solver = Solver()
		
	return solver

def printStatistics(solution):
	path = solution.getPath()
	
	print(path)
	#for state in path:
	#	print (state.__str__() + str(" -> "))
	#print ("END\n")
	
	print ("Branching Factor: " + str(solution.getBranchFactor()))
	print ("Number of expanded nodes: " + str(solution.getExpandedNodes()))
	print ("Number of visited nodes: " + str(solution.getNumberVisited()))
	print ("Number of iterations: " + str(solution.getNumberOfIterations()))
	print ("Solution depth: " + str(solution.getDepth()))
	print ("Solution Cost: " + str(solution.getCost()))
	print ("Time elapsed: " + str(solution.getTimeElapsed()))

	return
	
def mainLoop(solver, solution, fileName):
	clear()	
	
	while True:
		print("1 - Load an instance")
		print("2 - Select a method to use")
		print("3 - Come with the litle problem")
		print("4 - Statistics")
		print("5 - Exit")
		
		o = int(input('> '))
		
		clear()
		
		if o == 1:
			fileName = input("Instance file: ")
		elif o == 2:
			solver = selectMethod(solver)	
		elif o == 3:
			solver.read(fileName)
			solution = solver.solve()
			print("Little Problem solved...")
		elif o == 4:
			printStatistics(solution)
		elif o == 5:
			return 
			break
		
		wait()
		clear()

def main():
	solver = None
	solution = None
	hasArgs = True
	fileName = args.instance

	if args.x != None:
		x = float(args.x)
		y = float(args.y)
		x1 = float(args.x1)
		y1 = float(args.y1)

	if fileName == None or args.method == None:
		hasFlags = False
		mainLoop(solver, solution, fileName)
	elif args.method == "BTCK": #Backtracking
		solver = Solver()
	elif args.method == "BFS":	#Breadth First Search
		solver = BreadthFirst(State(x, y), State(x1, y1))
	elif args.method == "DFSL":	#Depth First Search limited
		solver = BreadthFirst(State(x, y), State(x1, y1))
	elif args.method == "OS":	#Ordered Search
		solver = OrderedSearch(State(x, y), State(x1, y1))
	elif args.method == "GS":	#Greedy Search
		solver = GreedySearch(State(x, y), State(x1, y1))
	elif args.method == "AS":	#A* search
		solver = AStar(State(x, y), State(x1, y1))
	elif args.method == "IDAS": #IDA* search
		solver = BreadthFirst(State(x, y), State(x1, y1))
		
	if hasArgs:
		solver.read(fileName)
		solution = solver.solve()
		printStatistics(solution)
	
	return
	
main()
	
