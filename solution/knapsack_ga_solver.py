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
import statistics


# Classes
@dataclass
class Knapsack:
    """Knapsack Class
    Data class holding initial, optimal solution and memory of all solutions.
    """
    optimal_solution: list[int] = field(default_factory=list)
    # Do not print population field when printing class
    population: list[list[int]] = field(
        default_factory=lambda: [[]], repr=False)
    optimal_value: float = 0    # Optimal utility value
    optimal_weight: float = 0   # Optimal weight value

    def solution_weight(self, iteration):
        """Provide a weight information for a specific solution"""
        specific_solution = self.population[iteration]
        return sum([x[0] for x in specific_solution])

    def solution_value(self, iteration):
        """Provide a utility value of specific solution"""
        specific_solution = self.population[iteration]
        return sum([x[1] for x in specific_solution])

    def __repr__(self) -> str:
        pop_size = len(self.population)
        med_items = statistics.median(
            [len(x) for x in self.population])
        return "Genetic Knapsack: population size: {0:,}; average knapsack size: {1:.0f}.".format(pop_size, med_items)


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


def generate_population(items, solution_generator, population_size, capacity):
    """Generate population using provided solution generator"""
    population = []
    while (len(population) < population_size):
        population.append(solution_generator(items=items, capacity=capacity))
    return population


# Tests
random.seed(123)
# Generate some data for tests, first is utility, second is weight
items_w_weights = [
    [random.randint(1, 100), random.randint(1, 100)] for _ in range(100)]
# Assume some arbitrary capacity for the Knapsack
CAPCITY: Final[int] = 30
POPULATION_SIZE: Final[int] = 1000
# Instantiate Knapsack class
genetic_knapsack = Knapsack(population=generate_population(items=items_w_weights, population_size=POPULATION_SIZE,
                                                           capacity=CAPCITY, solution_generator=generate_random_solution))
print(genetic_knapsack)
