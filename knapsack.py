#!/usr/bin/env python3

from __future__ import print_function
from ortools.algorithms import pywrapknapsack_solver

import sys

def main(filename):

    f = open(filename, 'r')
    first_line = f.readline().split(' ')
    second_line = [int(c) for c in f.readline().split(' ')]

    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    values = second_line
    weights = [second_line]
    capacities = [int(first_line[0])]

    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)

    fout = open(filename+'.txt', 'w')
    fout.write(str(len(packed_items))+'\n')
    fout.write(' '.join([str(i) for i in packed_items])+'\n')
    fout.close()




if __name__ == '__main__':
    main(sys.argv[1])
