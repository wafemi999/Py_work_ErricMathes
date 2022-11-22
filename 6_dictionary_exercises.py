#ex 6-1 person:
my_pesin = {'first_name':'lexin', 'last_name':'manuel', 'age': 25, 'city':'new jersey',}

print(my_pesin)

print("my person's name is ", my_pesin['first_name'],my_pesin['last_name'],".")
print(my_pesin['first_name'],my_pesin['last_name'],"age is", my_pesin['age'])
print(my_pesin['first_name'],my_pesin['last_name'], "resides in", my_pesin['city'])

#ex 6-2
print("\n favourite numbers:")
favorite_numbers = {
	'mike': 15,
	'seun': 114,
	'femi': 4,
	'felix': 18,
	'goke': 16,
	}
	
print("mike", "favourite number is", favorite_numbers['mike'])
print("seun", "favourite number is", favorite_numbers['seun'])
print("femi", "favourite number is", favorite_numbers['femi'])
print("felix", "favourite number is", favorite_numbers['felix'])
print("goke", "favourite number is", favorite_numbers['goke'])

print("\n")
#ex6-3 glossary 
py_glossary = {
	'list':'python mutable feature',
	'tuples':'python immutable feature',
	'upper()':'method for a string data',
	'dictionary':'collection of key-value pairs',
	'rstrip':'method for eliminating white spaces of a string data',
	}
	
print(py_glossary)
print('\n some python programming words and meaning:')
print("list",": \n",py_glossary['list'],"\n")
print("tuples",": \n",py_glossary['tuples'],"\n")
print("upper()",": \n",py_glossary['upper()'],"\n")
print("dictionary",": \n",py_glossary['dictionary'],"\n")
print("rstrip",": \n",py_glossary['rstrip'],"\n")
