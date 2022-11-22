''' FileNotFoundError
filename = 'alice.txt'
with open('filename')as f_obj:
	contents = f_obj.read()
	print(contents)
	'''
	
filename = 'alice.txt'
try:
	with open(filename)as f_obj:
		contents = f_obj.read()
	
except FileNotFoundError:
	print('the file:',filename," does not exist" )
	
else:
	print(contents)
