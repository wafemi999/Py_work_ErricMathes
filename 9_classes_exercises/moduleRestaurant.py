print("\n 9-6 :")
class Restaurant():
	'''A simple attempt to model a restaurant:'''
	
	def __init__(self, restaurant_name, cuisine_type, number_served):
		'''simulating a restaurant info'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served	
		
	def describe_restaurant(self):
		''' this prints the restaurants name and cuisine type:'''
		print("The restaurants name is "+self.restaurant_name )
		print("their most expensive cuisine is "+ self.cuisine_type)
		
	def open_restaurant(self):
		'''This indicates the restaurant is now open:'''
		print(self.restaurant_name+ " is now open")
	
	def set_number_served(self, x):
		'''allows you to set no of customer served'''
		self.number_served = 2
		if x >= self.number_served:
			self.number_served = x
			print("space filled: ",x)
		else:
			print("vacant space")
		
	def increment_number_served(self, increased):
		'''tells the total number of customer served in a day'''
		
		if increased <1:
			print("IMPOSSIBLE")
		else:
			self.number_served += increased
			print("TOTAL: ", increased)	
