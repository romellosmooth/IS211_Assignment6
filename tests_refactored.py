# tests_refactored.py

import unittest
from conversions_refactored import convert, ConversionNotPossible

class TestGeneralConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        # Celsius to Fahrenheit and Kelvin
        self.assertAlmostEqual(convert('celsius', 'fahrenheit', 0), 32.0, places=2)
        self.assertAlmostEqual(convert('celsius', 'kelvin', 100), 373.15, places=2)

        # Fahrenheit to Celsius and Kelvin
        self.assertAlmostEqual(convert('fahrenheit', 'celsius', 32), 0.0, places=2)
        self.assertAlmostEqual(convert('fahrenheit', 'kelvin', 212), 373.15, places=2)

        # Kelvin to Celsius and Fahrenheit
        self.assertAlmostEqual(convert('kelvin', 'celsius', 273.15), 0.0, places=2)
        self.assertAlmostEqual(convert('kelvin', 'fahrenheit', 373.15), 212.0, places=2)

    def test_distance_conversions(self):
        # Miles to Meters and Yards
        self.assertAlmostEqual(convert('miles', 'meters', 1), 1609.34, places=2)
        self.assertAlmostEqual(convert('miles', 'yards', 1), 1760, places=2)

        # Meters to Miles and Yards
        self.assertAlmostEqual(convert('meters', 'miles', 1609.34), 1, places=2)
        self.assertAlmostEqual(convert('meters', 'yards', 1), 1.09361, places=5)

        # Yards to Miles and Meters
        self.assertAlmostEqual(convert('yards', 'miles', 1760), 1, places=2)
        self.assertAlmostEqual(convert('yards', 'meters', 1), 0.9144, places=4)

    def test_same_unit_conversion(self):
        self.assertEqual(convert('celsius', 'celsius', 100), 100)
        self.assertEqual(convert('fahrenheit', 'fahrenheit', 32), 32)
        self.assertEqual(convert('kelvin', 'kelvin', 273.15), 273.15)
        self.assertEqual(convert('miles', 'miles', 1), 1)
        self.assertEqual(convert('meters', 'meters', 1000), 1000)
        self.assertEqual(convert('yards', 'yards', 1), 1)

    def test_incompatible_units(self):
        with self.assertRaises(ConversionNotPossible):
            convert('celsius', 'meters', 100)
        with self.assertRaises(ConversionNotPossible):
            convert('miles', 'kelvin', 1)

if __name__ == '__main__':
    unittest.main()

