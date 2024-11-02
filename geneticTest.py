import unittest
import random
from genetic import *

class TestGeneticAlgorithm(unittest.TestCase):
    
    def test_population(self):
        jumlahPopulasi = 8  # Population size
        pop, prob = population(jumlahPopulasi)
        
        # Test if population size matches jumlahPopulasi
        self.assertEqual(len(pop), jumlahPopulasi)
        
        # Test if probability list size matches jumlahPopulasi
        self.assertEqual(len(prob), jumlahPopulasi)
        
        # Test if all individuals have the expected length (125)
        for individu in pop:
            self.assertEqual(len(individu), 125)
        
        # Test if the probability values sum up to approximately 1.0
        self.assertAlmostEqual(sum(prob), 1.0, places=2)

    def test_selection(self):
        jumlahPopulasi = 8  # Population size
        jumlahParent = 4    # Number of parents to select
        pop, prob = population(jumlahPopulasi)
        
        # Run selection
        parents = selection(jumlahParent, pop, prob)
        
        # Test if the number of selected parents matches jumlahParent
        self.assertEqual(len(parents), jumlahParent)
        
        # Test if each selected parent is in the original population
        for parent in parents:
            self.assertIn(parent, pop)

    def test_crossover(self):
        # Generate two parent individuals
        parent1 = initial()
        parent2 = initial()[::-1]  # Reverse order for diversity
        
        # Perform crossover
        offspring1, offspring2 = crossover(parent1, parent2)
        
        # Test if offspring lengths match parent lengths
        self.assertEqual(len(offspring1), len(parent1))
        self.assertEqual(len(offspring2), len(parent2))
        
        # Test if offspring are combinations of parents
        # Offspring should not be identical to any parent (because of crossover)
        self.assertNotEqual(offspring1, parent1)
        self.assertNotEqual(offspring2, parent2)

    def test_mutation(self):
        # Generate an individual with duplicate values for mutation testing
        offspring = [i if i <= 60 else 60 for i in range(1, 126)]
        
        # Apply mutation
        mutated_offspring = mutation(offspring)
        
        # Test if mutated_offspring has no duplicates (values should be unique from 1 to 125)
        self.assertEqual(len(set(mutated_offspring)), 125)
        
        # Test if mutated_offspring contains all numbers from 1 to 125
        self.assertTrue(all(x in mutated_offspring for x in range(1, 126)))

if __name__ == '__main__':
    unittest.main()
