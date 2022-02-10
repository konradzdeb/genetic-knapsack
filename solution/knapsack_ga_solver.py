#!/usr/bin/env python3
"""Knapsack Genetic Algorithm solver.
The following implementation provides a simple genetic algorithm solver approach
to the Knapsack Problem

Konrad Zdeb, 2021
"""

# Imports
from dataclasses import dataclass, field
import random
from typing import Final


# Classes
@dataclass
class Knapsack:
    """Knapsack Class
    Data class holding initial, optimal solution and memory of all solutions.
    """    
    initial_solution: list[int] = field(default_factory=list)
    optimal_solution: list[int] = field(default_factory=list)
    population: list[list[int]] = field(default_factory=lambda: [[]])
    optimal_value: float = 0    # Optimal utility value
    optimal_weight: float = 0   # Optimal weight value

    def initial_weight(self):
        """Calculate initial weight from the initial solution"""
        return sum([x[0] for x in self.initial_solution])

    def initial_value(self):
        """Calculate value for the initial solution"""
        return sum([x[1] for x in self.initial_solution])

    def solution_weight(self, iteration):
        """Provide a weight information for a specific solution"""
        specific_solution = self.memory[iteration]
        return sum([x[0] for x in specific_solution])

    def solution_value(self, iteration):
        """Provide a utility value of specific solution"""
        specific_solution = self.memory[iteration]
        return sum([x[1] for x in specific_solution])


# Functions
def generate_random_solution(items, capacity):
    """Generate initial solution"""
    current_weight = 0
    random_solution = []
    while current_weight < capacity:
        # Select random item
        random_item = random.sample(items, 1)[0]
        # Check if item fits in the knapsack
        if current_weight + random_item[1] <= capacity:
            # Add item to solution
            random_solution.append(random_item)
            current_weight += random_item[1]
    # Returned packed knapsack
    return random_solution
        
    
# Tests
random.seed(123)
# Generate some data for tests, first is utility, second is weight
items_w_weights = []
utility_weight_pair = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(100)]
# Assume some arbitrary capacity for the Knapsack
CAPCITY: Final[int] = 30
# Instantiate Knapsack class
genetic_knapsack = Knapsack(initial_solution=generate_random_solution(items_w_weights, 30))