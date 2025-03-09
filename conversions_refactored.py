# conversions_refactored.py

class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    conversions = {
        'celsius': {
            'fahrenheit': lambda x: (x * 9 / 5) + 32,
            'kelvin': lambda x: x + 273.15,
            'celsius': lambda x: x
        },
        'fahrenheit': {
            'celsius': lambda x: (x - 32) * 5 / 9,
            'kelvin': lambda x: (x + 459.67) * 5 / 9,
            'fahrenheit': lambda x: x
        },
        'kelvin': {
            'celsius': lambda x: x - 273.15,
            'fahrenheit': lambda x: (x * 9 / 5) - 459.67,
            'kelvin': lambda x: x
        },
        'miles': {
            'meters': lambda x: x * 1609.34,
            'yards': lambda x: x * 1760,
            'miles': lambda x: x
        },
        'meters': {
            'miles': lambda x: x / 1609.34,
            'yards': lambda x: x * 1.09361,
            'meters': lambda x: x
        },
        'yards': {
            'miles': lambda x: x / 1760,
            'meters': lambda x: x / 1.09361,
            'yards': lambda x: x
        }
    }

    if fromUnit not in conversions or toUnit not in conversions[fromUnit]:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible")

    return conversions[fromUnit][toUnit](value)

