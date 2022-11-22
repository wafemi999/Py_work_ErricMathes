from collections import OrderedDict
py_glossary = OrderedDict()


py_glossary = {
	'list':'python mutable feature',
	'tuples':'python immutable feature',
	'upper()':'method for a string data',
	'dictionary':'collection of key-value pairs',
	'rstrip':'method for eliminating white spaces of a string data',
	'sorted()':'used in temporary sorting of items ina list',
	'sort()':'used for permanent sorting in a list',
	'set()':'make each item in a list unique(no reppetition)',
	'reverse()':'used in sorted() to print the opposite order of a list or  reversed alphabetically',
	'title()':'prints the 1st character of string in upper case ',
	}
	
for term, meaning in py_glossary.items():
	print("\n TERM:", term)
	print(" MEANING:", meaning)
