fileNames = ['cats.txt', 'dogs.txt', 'goats.txt']
for fileName in fileNames: 
	try:
		with open(fileName)as file_obj:
			contents = file_obj.read()
	
	except FileNotFoundError:
		print('sorry', fileName, 'not found in this directory')
	else:
		print("\n", fileName,":\n",contents, "\n")
