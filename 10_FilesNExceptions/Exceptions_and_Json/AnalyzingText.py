filename = 'alice.txt'
try:
	with open(filename)as f_obj:
		contents = f_obj.read()
	
except FileNotFoundError:
	print('the file:',filename," does not exist" )
	
else:
	#this counts the number of words in the file
	words = contents.split()
	num_words = len(words)
	print('The file:', filename, 'has', str(num_words), 'words')
