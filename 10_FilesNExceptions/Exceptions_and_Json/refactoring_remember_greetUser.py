import json
def GreetUser():
	'''greet the user by name'''
	filename = 'username_2.json'
	try:
		with open(filename)as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input('pls enter your name: ')
		with open(filename, 'w')as f_obj:
			json.dump(username, f_obj)
			print('we will remember you when you are back', username)
	else:
		print('welcome back', username)

GreetUser()
