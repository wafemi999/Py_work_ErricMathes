#ex6-4 glossary 2
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
	
for term, meaning in sorted(py_glossary.items()):
	print("\n TERM:", term)
	print(" MEANING:", meaning)


#ex6-5 RIvers:
print("\n Rivers:")
rivers = {'nile':'Egypt', 'mississippi': 'USA', 'benue':'Nigeria'}
for R_name, R_location in set(rivers.items()):
	print("the",R_name.upper()," river runs through", R_location.upper())

print("\n list of rivers:")	
for R_name in sorted(rivers.keys()):
	print(R_name.upper())


print("\n location of the  rivers:")
for R_location in sorted(rivers.values()):
	print(R_location)	


#ex6-6 polling
print("\n polling:")
favorite_languages = {
	'jen':'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}

eligibles = ['jen', 'sarah','femi','edward','phil','tola','bolu',]
''' manuel scan the quest very well for which item to compare against'''
for i in eligibles:
	if i in favorite_languages:
		print(i.title(), "thank you for voting")
	else:
		print(i.title(),"we invite you to vote")

	
