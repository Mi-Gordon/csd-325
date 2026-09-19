# Michael Gordon
# CSD-325
# Assignment 7.2

import unittest
from city_functions import city_country


class LocationTestCase(unittest.TestCase):
    """Tests for 'city_country.py"""

    def test_city_country(self):
        formatted_location = city_country('Peoria', 'USA')
        self.assertEqual(formatted_location, '\nPeoria, USA\n')

    def test_city_country_population(self):
        formatted_location = city_country('Santiago', 'Chile', 5000)
        self.assertEqual(formatted_location,
                         '\nSantiago, Chile - population 5000\n')

    def test_city_country_population_language(self):
        formatted_location = city_country('Santiago', 'Chile', 5000, 'Spanish')
        self.assertEqual(formatted_location,
                         '\nSantiago, Chile - population 5000, Spanish\n')


if __name__ == '__main__':
    unittest.main()
