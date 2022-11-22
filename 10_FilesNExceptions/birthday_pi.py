fileName = 'py_digit_2.txt'
with open(fileName)as file_object:
	lines = file_object.readlines()
	
piString = ''
for line in lines:
	piString += line.strip()


birthday = input("enter your birthday, in the form of mmddyy: ")
if birthday in piString:
	print("your birthday appears in the first million digits of pi")
else:
	print("your birthday does not appear in the first million digits of pi")
