from sys import platform
import os
import argparse

from Solver import *
from BreadthFirst import *
from OrderedSearch import *
from AStar import *
from GreedySearch import *

parser = argparse.ArgumentParser()
parser.add_argument('--inst', help='Instance of the city graph to be solved.')
parser.add_argument('--method', help='Method to solve the problem.')
args = parser.parse_args()

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

def selectMethod(solver):
	print("1 - Backtracking")
	print("2 - Breadth First Search")
	print("3 - Depth First Search (limited)")
	print("4 - Ordered Search")
	print("5 - Greed Search")
	print("6 - A* Search")
	print("7 - IDA* Search")
	
	o = int(input("> "))
	if o == 1:
		solver = Solver()
	if o == 2:
		solver = BreadthFirst()
	if o == 3:
		solver = Solver()
	if o == 4:
		solver = OrderedSearch()
	if o == 5:
		solver = GreedySearch()
	if o == 6:
		solver = AStar()
	if o == 7:
		solver = Solver()
	return solver

def printStatistics(solution):
	path = solution.getPath()
	
	for state in path:
		print (state.__str__() + str(" -> "))
	print ("END\n")
	
	print ("Branching Factor: " + str(solution.getBranchFactor()))
	print ("Number of expanded nodes: " + str(solution.getExpandedNodes()))
	print ("Number of visited nodes: " + str(solution.getNumberVisited()))
	print ("Solution depth: " + str(solution.getDepth()))
	print ("Solution Cost: " + str(solution.getCost()))
	print ("Time elapsed: " + str(solution.getTimeElapsed()))

	return
	
def mainLoop():
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
	fileName = args.inst
	
	if fileName == None or args.method == None:
		mainLoop()
	elif args.method == "BTCK": #Backtracking
		solver = Solver()
	elif args.method == "BFS":	#Breadth First Search
		solver = BreadthFirst()
	elif args.method == "DFSL":	#Depth First Search limited
		solver = BreadthFirst()
	elif args.method == "OS":	#Ordered Search
		solver = OrderedSearch()
	elif args.method == "GS":	#Greedy Search
		solver = GreedySearch()
	elif args.method == "AS":	#A* search
		solver = AStar()
	elif args.method == "IDAS": #IDA* search
		solver = BreadthFirst()
		
	solver.read(fileName)
	solution = solver.solve()
	printStatistics(solution)
	
	return
	
main()
	
