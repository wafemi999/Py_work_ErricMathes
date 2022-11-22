filenames = ['alice.txt', 'mobyDick.txt', 'littlewomen.txt', 'siddharta.txt',]
for filename in filenames:
	try:
		with open(filename)as f_obj:
			contents = f_obj.read()
	
	except FileNotFoundError:
		print('the file:',filename," does not exist" )
	
	else:
		#this counts the number of a specific word in the file
		words = contents.lower().count('the')
		print(filename,"no of times  word 'the', appears:", words, "\n")
		#num_words = len(words)
		#print('The file:', filename, 'has', str(num_words), 'words')

