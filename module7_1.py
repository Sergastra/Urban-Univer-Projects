from pprint import pprint

name = 'text.txt'
file = open(name, 'r')
pprint(file.read())
file.close()
