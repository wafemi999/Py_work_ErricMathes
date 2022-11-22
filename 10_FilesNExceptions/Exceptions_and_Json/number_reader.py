import json

with open('numbers.json')as f_obj:
	numbers = json.load(f_obj)
	print(numbers)
