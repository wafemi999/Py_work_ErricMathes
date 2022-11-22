#THIs program writes a persons fav no to memory
import json
number = input("pls whats your favorite number? ")

with open('favorite_no.json', 'w')as f_obj:
	json.dump(number, f_obj)


#this program reads the above code from memory
filename = 'favorite_no.json'

with open (filename)as f_obj:
	favorite_number = json.load(f_obj)
	print("i know your favorite number it is,", favorite_number) 
