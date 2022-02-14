"""Simple test for the Knapsack GA solver"""

import unittest
import random

from knapsack_ga_solver import *


class TestGeneratingRandomSolution(unittest.TestCase):

    def setUp(self):
        random.seed(123)
        self.items_weight_value = [
            [random.randint(1, 100), random.randint(100, 1000)] for _ in range(100)]
        self.CAPACITY = 30
        self.solution = generate_random_solution(
            self.items_weight_value, self.CAPACITY)

    def test_function_output(self):
        """Test if the function returns a list of items"""
        # Check if the solution is a list
        self.assertIsInstance(self.solution, list)
        # Check if the solution is not empty
        self.assertTrue(len(self.solution) > 0)


class TestGeneratingPopulation(TestGeneratingRandomSolution):

    def setUp(self):
        super(TestGeneratingPopulation, self).setUp()
        # Generate population
        self.population = generate_population(items=self.items_weight_value, capacity=self.CAPACITY,
                                              population_size=10, solution_generator=generate_random_solution)

    def test_function_output(self):
        """Test if the function returns a list of solutions"""
        # Check if the population is a list
        self.assertIsInstance(self.population, list)
        # Check if the population is not empty
        self.assertEqual(len(self.population), 10)
        # Check if the population is a list of lists
        for solution in self.population:
            self.assertIsInstance(solution, list)
        # Check if the population is a list of lists
        for solution in self.population:
            self.assertTrue(len(solution) > 0)
        # Check if the population is a list of lists
        for solution in self.population:
            self.assertIsInstance(solution, list)
        # Check if the population is a list of lists
        for solution in self.population:
            self.assertTrue(len(solution) > 0)
        # Check if the population is a list of lists
        for solution in self.population:
            self.assertIsInstance(solution, list)
        # Check if the population is a list of lists
        for solution in self.population:
            self.assertTrue(len(solution) > 0)


class TestUtilityCalculations(TestGeneratingRandomSolution):

    def setUp(self):
        return super().setUp()

    def test_utility_calculation(self):
        """Test if the function returns a list of solutions"""
        # Calculate utility
        utility = calculate_utility(self.solution)
        self.assertIsInstance(utility, int)
        self.assertGreater(utility, 100)


class TestGeneratingKnapsackObject(TestGeneratingRandomSolution):

    def setUp(self):
        super(TestGeneratingKnapsackObject, self).setUp()
        # Create sample knapsack object
        self.knapsack = Knapsack(population=generate_population(items=self.items_weight_value, population_size=1000,
                                                                capacity=self.CAPACITY, solution_generator=generate_random_solution))

    def test_knapsack_class(self):
        self.assertIsInstance(self.knapsack, Knapsack)


class TestGeneticFunctions(TestGeneratingKnapsackObject):

    def setUp(self):
        super(TestGeneticFunctions, self).setUp()

    def test_selection(self):
        """Test if the selection function returns a list of solutions"""
        # Select solutions
        selected_solutions = selection(self.knapsack, fitness_rank=None)
        # Check if the selected solutions is a list
        self.assertIsInstance(selected_solutions, list)
        # Check if the selected solutions is not empty
        self.assertTrue(len(selected_solutions) > 0)
        # Check if the selected solutions is a list of lists
        for solution in selected_solutions:
            self.assertIsInstance(solution, int)
        # Check if the selected solutions is a list of lists
        for solution in selected_solutions:
            self.assertIsNotNone(solution)

    def test_mutation(self):
        """Test if mutation returns a solution"""
        mutated_solution = mutation(knapsack_solution=self.knapsack, items=self.items_weight_value)
        self.assertIsInstance(mutated_solution, list)
        self.assertGreaterEqual(len(mutated_solution), 1)       

    def test_crossover(self):
        """Test if crossover returns a solution"""
        crossover_solution = crossover(self.knapsack, 1, 2, 0.5)
        self.assertIsInstance(crossover_solution, list)
        self.assertGreaterEqual(len(crossover_solution), 1)


