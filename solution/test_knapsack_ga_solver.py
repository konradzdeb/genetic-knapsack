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

    def test_function_output(self):
        """Test if the function returns a list of solutions"""
        # Calculate utility
        utility = calculate_utility(self.solution)
        self.assertIsInstance(utility, int)
        self.assertGreater(utility, 100)
