#This the regular expressions library
import re


#names file is a pointer to location of the file in the file system
names_file = open("names.txt", encoding='utf-8')
#Reads file and saves it to data
data = names_file.read() 
#closes file and takes it of memory
names_file.close()


last_name = r'Love'
first_name = r'Kenneth'
#r tells python that string is a raw string
#print(re.match(last_name, data))
#match looks to match at the beginning of the string
#print(re.search(first_name, data))
#search looks to match at any part of the string
#print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
#re.search only searches one line. re.findall searches entire document
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
#print(re.search(r'\w+, \w+', data))
#print(re.findall(r'\w*, \w+', data))
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))
#print(re.findall(r'''
#   \b@[-\w\d.]* #First a word boundary, an @, and then any number of characters
#    [^gov\t]+  # Ignore  1+ instances of letters 'g', 'o', 'v' and a tab.
#    \b # Match another word boundary
#''', data, re.VERBOSE|re.I))
#print(re.findall(r'''
#    \b[-\w]*,  # Find a word boundary, 1+ hyphens or characters, and a comma
#    \s # Find 1 whitespace
#    [-\w]+  # 1+ hyphens and characters and explicit spaces
#    [^\t\n]  # Ignore tabs and newlines
#''', data, re.X))
#line = re.search(r'''
#    ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # Last and first names
#    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
#    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
#    (?P<job>[\w\s]+,\s[\w\s.]+)\t?   # Job and Company
#    (?P<twitter>@[\w\d]+)?$  # Twitter
#''', data, re.X|re.MULTILINE)
#print(line)
#print(line.groupdict())

# Code Challenge
# Create a variable names that is an re.match() against string. The pattern should provide two groups, one for a last name match and one for a first name match. The name parts are separated by a comma and a space.

#import re
#string = 'Perotto, Pier Giorgio'
#names = re.match(r'([-\w]+),\s([-\w ]+)', string)

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?   # Job and Company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', re.X|re.MULTILINE)
#print(re.search(line, data).groupdict())
# This also works.  line could be any pattern
#print(line.search(data).groupdict())
for match in line.finditer(data):
    #print(match.group('name'))
    print('{first} {last} <{email}>'.format(**match.groupdict()))


