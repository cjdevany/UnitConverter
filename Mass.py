from Unit import *


OPTIONS = {
            'oz' : 0,
            'lb' : 1,
            'mg' : 2,
            'g' : 3,
            'kg' : 4
}

"""
This is a lookup table to convert distance values. 
Going in order from OPTIONS, each row is how many of that unit it takes to make one.
Example: row 3 shows 1 gram (g) converted to each other unit in the list.
"""
CONVERSION_TABLE = [
            [1, 1/16, 28349.523, 28.35, 1/35.274],
            [16, 1, 453592.37, 453.592, 1/2.205],
            [1/28350, 1/453592, 1, 1/1000, 1/1000000],
            [1/28.35, 1/454, 1000, 1, 1/1000],
            [35.274, 2.205, 1000000, 1000, 1]
]


class Mass(Unit):
    def __init__(self, value, unit_lbl):
        super().__init__(value, unit_lbl)

    
    # Converts the value and returns a new Mass object with the proper label
    def convert(self, convertTo):
        table_row = OPTIONS.get(self.lbl)
        table_col = OPTIONS.get(convertTo)
        return Mass(self.value * CONVERSION_TABLE[table_row][table_col], convertTo)

    def getOptions(self):
        return list(OPTIONS.keys())


# Just used for testing
if __name__ == "__main__":
    m1 = Mass(100, 'g')
    print(m1)
    print(m1.convert('oz'))