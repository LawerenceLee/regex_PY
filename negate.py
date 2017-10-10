import re

string = 'a1234567890'

good_numbers = re.findall(r'''
    [^5-7]
''', string, re.X)

print(good_numbers)