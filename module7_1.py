from pprint import pprint

name = 'text.txt'
with open(name) as file:
    for line in file:
        print(line, end='')
