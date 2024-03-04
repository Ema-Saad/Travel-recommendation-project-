import unittest
import pandas as pd
from recommend_cities import recommend_cities


class TestRecommendCities(unittest.TestCase):
    def setUp(self):
        self.flights = pd.DataFrame({'from': ['A', 'B', 'C', 'A', 'D'],
                                     'to': ['B', 'C', 'D', 'E', 'E'],
                                     'price': [100, 200, 150, 50, 80]})
        self.hotels = pd.DataFrame({'place': ['A', 'B', 'C', 'D', 'E'],
                                    'price': [50, 70, 60, 40, 30]})

    def test_small_budget_few_cities(self):
        budget = 300
        num_cities = 3
        result = recommend_cities(budget, num_cities, self.flights, self.hotels)
        self.assertEqual(result, ['A', 'D'])

    def test_large_budget_many_cities(self):
        budget = 5000
        num_cities = 5
        result = recommend_cities(budget, num_cities, self.flights)