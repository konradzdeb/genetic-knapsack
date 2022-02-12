#!/usr/bin/env python3
"""Knapsack Genetic Algorithm solver.
The following implementation provides a simple genetic algorithm solver approach
to the Knapsack Problem

Konrad Zdeb, 2021
"""

# Imports
from dataclasses import dataclass, field
from operator import le
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
    mutated_items_index: list[int] = field(default_factory=list)
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

    def solutions_rank(self):
        """Provide a utility rank of all solutions"""
        solution_values = [self.solution_value(x) for x in range(len(self.population))]
        return sorted(range(len(solution_values)), key=solution_values.__getitem__)

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
        if current_weight + random_item[0] <= capacity:
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


# TODO: Implement crossover
def calculate_utility(solution):
    """Calculate solution utility
    This is equivalent to pulling solution value from the Knapsack class but is implemented separately for clarity.
    Args:
        solution ([[int, int]]): List of items in the solution

    Returns:
        int: Utility value as an integer
    """
    return sum([x[1] for x in solution])


def selection(knapsack_object, fitness_rank=None):
    """Select objects from Knapsack that are of defined fitness
    
    If fitness is provided, objects above the threshold are selected for situation
    where fitness is not provided the top half of objects is selected. Fitness 
    corresponds to minimum rank value.
    Args:
        knapsack_object (Knapsack): Object of a Knapsack class with provided population
        fitness (int, optional): If provided minimum rank value to include. Defaults to None.

    Returns:
        [int]: Index of solutions from population that were selected
    """
    solutions_rank = knapsack_object.solutions_rank()
    if fitness_rank is None:
        threshold = statistics.median(knapsack_object.solutions_rank())
    else:
        threshold = fitness_rank
    index_selected = [x for x in range(len(solutions_rank)) if solutions_rank[x] < threshold]
    return index_selected


def mutation(knapsack_solution, items, pop_item=None):
    """Mutate object from knapsack

    Select object from Knapsack population and mutate.
    
    Args:
        knapsack_object (Knapsack): Object of a Knapsack
    """
    # Select object from population
    if pop_item is None:
        pop_solution = random.sample(knapsack_solution.population, 1)[0]
    else:
        # TODO: Check if this needs unnesting
        pop_solution = knapsack_solution.population[pop_item]
    # Randomly mutate an object by replacing one item with the item from the
    # available items. The mutation can produce adverse effect (utility decreases)
    # or beneficial effect (utility increases). Try limited number of items and
    # if continuous failing return the same thing.
    # Obtain a list of remaining items to choose from
    remaining_items = [x for x in items if x not in pop_solution]
    # Get population weight
    pop_weight = knapsack_solution.solution_weight(pop_item)
    for _ in range(10):
        # Select random item from available items
        random_new_item = random.sample(remaining_items, 1)[0]
        random_sol_item = random.sample(pop_solution, 1)[0]
        # Check if replacing item in knapsack is acceptable
        if pop_weight + random_new_item[0] - random_sol_item[0] <= knapsack_solution.capacity:
            # Replace item in solution
            pop_solution.remove(random_sol_item)
            pop_solution.append(random_new_item)
    # Return mutated solution
    return pop_solution


# Tests
random.seed(123)
# Generate some data for tests, first is utility, second is weight
items_w_weights = [
    [random.randint(1, 100), random.randint(1000, 10000)] for _ in range(100)]
# Assume some arbitrary capacity for the Knapsack
CAPCITY: Final[int] = 30
POPULATION_SIZE: Final[int] = 1000
# Instantiate Knapsack class
genetic_knapsack = Knapsack(population=generate_population(items=items_w_weights, population_size=POPULATION_SIZE,
                                                           capacity=CAPCITY, solution_generator=generate_random_solution))
desired_fitness = 10
res_selection = selection(genetic_knapsack, fitness_rank=desired_fitness)
res_selection

# TODO: Implement gentic algorithm functions