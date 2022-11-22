#in this code traceback msg is skipped by the use of pass(this does nothing i.e no response to error)
def Count_words(filename):
	'''this function approximates no of words in a file'''
	
	try:
		with open(filename)as f_obj:
			contents = f_obj.read()
	
	except FileNotFoundError:
		pass
		#print('the file:',filename," does not exist" )
	
	else:
	#this counts the number of words in the file
		words = contents.split()
		num_words = len(words)
		print('The file:', filename, 'has', str(num_words), 'words')


file_names = ['alice.txt', 'siddharta.txt',  'mobyDick.txt' ,'LittleWomen.txt']
for filename in file_names:
	Count_words(filename)


