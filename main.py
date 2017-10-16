from Solver import *
from BreadthFirst import *

solve = BreadthFirst()
solve.read("graph.inst")
print(solve.solve())
