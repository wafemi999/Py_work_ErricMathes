print("this shows how replace() method is used")
fileName = '10_1_learningPython.txt'
with open(fileName)as file_object:
	lines = file_object.readlines()
	
	for i in lines:
		print(i.replace('python', 'C++'))
