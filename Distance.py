"""
Distance is a class for any length of measurement.
"""

from Unit import *

"""
OPTIONS dictionary maps units with array indices for the conversion table.
"""
OPTIONS = {
            'in' : 0,
            'ft' : 1,
            'yd' : 2,
            'mi' : 3,
            'cm' : 4,
            'm'  : 5,
            'km' : 6
}

"""
This is a lookup table to convert distance values. 
Going in order from OPTIONS, each row is how many of that unit it takes to make one.
Example: row 3 shows 1 yard converted to each other unit in the list.
"""
CONVERSION_TABLE = [
            [1, 1/12, 1/36, 1/63360, 2.54, 1/39.37, 1/39370],
            [12, 1, 1/3, 1/5280, 30.48, 1/3.281, 1/3281],
            [36, 3, 1, 1/1760, 91.44, 1/1.094, 1/1094],
            [63360, 5280, 1760, 1, 160934.4, 1609.344, 1.609],
            [1/2.54, 1/30.48, 1/91.44, 1/160934, 1, 1/100, 1/100000],
            [39.3701, 3.28084, 1.09361, 1/1609, 100, 1, 1/1000],
            [39370.1, 3280.84, 1093.61, 1/1.609, 100000, 1000, 1]
]


class Distance(Unit):
    def __init__(self, value, unit_lbl):
        super().__init__(value, unit_lbl)
    

    # Converts the value and returns it as a new distance object with the proper label
    def convert(self, convertTo):
        table_row = OPTIONS.get(self.lbl)
        table_col = OPTIONS.get(convertTo)
        return Distance(self.value * CONVERSION_TABLE[table_row][table_col], convertTo)

    
    def getOptions(self):
        return list(OPTIONS.keys())


# Just used for testing rn.
if __name__ == "__main__":
    d = "131.6666666 ft"
    ds = parseStringToUnit(d)
    print(ds[0] + ds[1])