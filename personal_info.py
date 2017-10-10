# make a class for a person defined by the data (names, email, phone, etc)


import re

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?   # Job and Company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', re.X|re.MULTILINE)

for match in line.finditer(data):
    #print(match.group('name'))
    print('{first} {last} <{email}>'.format(**match.groupdict()))

class Person:
    