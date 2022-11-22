print("this prints the the file as list of lines")
fileName = '10_1_learningPython.txt'
with open(fileName)as file_object:
	lines = file_object.readlines()
	for i in lines:
		print(i)
	
	
print("\n reads this file and prints it thrice")
with open('10_1_learningPython.txt')as file_object:
	content = file_object.read()
	print(content)
	print("\n",content)
	print("\n",content)
	
	
print("\n\n this reads the entire content: ")
with open('10_1_learningPython.txt')as file_object:
	content = file_object.read()
	print(content)

print("this prints the content by looping over the file_object:")	
with open('10_1_learningPython.txt')as file_object:
	for i in file_object:
		print(i)

'''
piString = ''
for x in lines:
	piString += x.strip()
	print(piString)
'''
