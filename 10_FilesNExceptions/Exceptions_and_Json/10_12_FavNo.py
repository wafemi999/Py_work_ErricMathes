#THIs program writes a persons fav no to memory
import json
filename = 'favorite_no_3.json'
try:
	with open (filename)as f_obj:
		favorite_number = json.load(f_obj)
		print("i know your favorite number it is,", favorite_number) 
except FileNotFoundError:
	number = input("pls whats your favorite number? ")
	with open(filename, 'w')as f_obj:
		json.dump(number, f_obj)
