# tests.py

import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit


class TestConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        print("Testing convertCelsiusToKelvin...")
        self.assertAlmostEqual(convertCelsiusToKelvin(300.0), 573.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(0.0), 273.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0.0, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(100.0), 373.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(25.0), 298.15, places=2)

    def test_convertCelsiusToFahrenheit(self):
        print("Testing convertCelsiusToFahrenheit...")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300.0), 572.0, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0.0), 32.0, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-273.15), -459.67, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100.0), 212.0, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(25.0), 77.0, places=2)


if __name__ == '__main__':
    unittest.main()
# tests.py

import unittest
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)


class TestConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        print("Testing convertCelsiusToKelvin...")
        self.assertAlmostEqual(convertCelsiusToKelvin(300.0), 573.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(0.0), 273.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0.0, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(100.0), 373.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(25.0), 298.15, places=2)

    def test_convertCelsiusToFahrenheit(self):
        print("Testing convertCelsiusToFahrenheit...")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300.0), 572.0, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0.0), 32.0, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-273.15), -459.67, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100.0), 212.0, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(25.0), 77.0, places=2)

    def test_convertFahrenheitToCelsius(self):
        print("Testing convertFahrenheitToCelsius...")
        self.assertAlmostEqual(convertFahrenheitToCelsius(572.0), 300.0, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(32.0), 0.0, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(-459.67), -273.15, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(212.0), 100.0, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(77.0), 25.0, places=2)

    def test_convertFahrenheitToKelvin(self):
        print("Testing convertFahrenheitToKelvin...")
        self.assertAlmostEqual(convertFahrenheitToKelvin(572.0), 573.15, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(32.0), 273.15, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(-459.67), 0.0, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(212.0), 373.15, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(77.0), 298.15, places=2)

    def test_convertKelvinToCelsius(self):
        print("Testing convertKelvinToCelsius...")
        self.assertAlmostEqual(convertKelvinToCelsius(573.15), 300.0, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(273.15), 0.0, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(0.0), -273.15, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(373.15), 100.0, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(298.15), 25.0, places=2)

    def test_convertKelvinToFahrenheit(self):
        print("Testing convertKelvinToFahrenheit...")
        self.assertAlmostEqual(convertKelvinToFahrenheit(573.15), 572.0, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(273.15), 32.0, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(0.0), -459.67, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(373.15), 212.0, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(298.15), 77.0, places=2)


if __name__ == '__main__':
    unittest.main()

