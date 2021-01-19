from Unit import *


OPTIONS = {
            'tspn' : 0,
            'tbsp' : 1,
            'C' : 2,
            'pt' : 3,
            'qt' : 4,
            'gal' : 5,
            'mL' : 6,
            'L' : 7,
            'kL' : 8            
}

"""
This is a lookup table to convert distance values. 
Going in order from OPTIONS, each row is how many of that unit it takes to make one.
Example: row 3 shows 1 pint converted to each other unit in the list.
"""
CONVERSION_TABLE = [
            [1, 1/3, 1/48, 1/96, 1/192, 1/768, 5, 1/202.884, 1/202884],
            [3, 1, 1/16, 1/32, 1/64, 1/256, 15, 1/67.628, 1/67628],
            [48, 16, 1, 1/2, 1/4, 1/16, 237, 1/4.22675, 1/4226.75],
            [96, 32, 2, 1, 1/2, 1/8, 473, 1/2.11338, 1/2113.38],
            [192, 64, 4, 2, 1, 1/4, 946.353, 0.946353, 0.000946353],
            [768, 256, 16, 8, 4, 1, 3785.41, 3.78541, 1/264],
            [1/5, 1/15, 1/237, 1/473, 1/946.353, 1/3785.41, 1, 1/1000, 1/1000000],
            [202.884, 67.628, 4.22675, 2.11338, 1/0.946353, 1/3.78541, 1000, 1, 1/1000],
            [202884, 67628, 4226.75, 2113.38, 1/0.000946353, 264, 1000000, 1000, 1]
]

class Volume(Unit):
    def __init__(self, value, unit_lbl):
        super().__init__(value, unit_lbl)

    def convert(self, convertTo):
        table_row = OPTIONS.get(self.lbl)
        table_col = OPTIONS.get(convertTo)
        return Volume(self.value * CONVERSION_TABLE[table_row][table_col], convertTo)

    def getOptions(self):
        return list(OPTIONS.keys())


# Just used for testing
if __name__ == "__main__":
    v1 = Volume(100, 'L')
    print(v1)
    print(v1.convert('qt'))