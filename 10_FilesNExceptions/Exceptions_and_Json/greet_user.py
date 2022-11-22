import json
filename = 'username.json'
with open(filename)as f_obj:
	username = json.load(f_obj)
	print('welcome back',username)
