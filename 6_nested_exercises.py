#ex6-7 people

pesin_1 = {
	'first_name':'lexin',
	'last name':'manuel',
	'age': 25,
	'city':'new jersey',
	}
	
pesin_2 = {
	'first_name':'bote',
	'last name':'diane',
	'age': 28,
	'city':'new york',
	}
	
pesin_3 = {
	'first_name':'kalu',
	'last name':'sewa',
	'age': 23,
	'city':'DC',
	}
	
	
print(pesin_1,"\n" ,pesin_2,"\n", pesin_3)
people = [pesin_1, pesin_2, pesin_3]
print("\n looping through the dictionary in list showing infos:")


for p in people:
		print("\n ","FIRST NAME:"+p['first_name'],"LAST NAME:"+p['last name'],"AGE:",p['age'],"location:"+
		p['city'])



#ex6-8 pets
print("\n PETS:")
bingo = {
	'name':'bingo',
	'kind':'dog',
	'owner':'erad',
	}


rapid = {
	'name':'rapid',
	'kind':'bird',
	'owner':'tola',
	}
	
danger = {
	'name':'danger',
	'kind':'hamster',
	'owner':'janie',
	}
	

pets = [bingo, rapid, danger,]

for p in pets:
	print("\n name:"+p['name'],"kind:"+p['kind'],"Owner:"+p['owner'])



#ex 6-9 favorite places:
print("\n favorite places:")
favorite_places = {
	'jen':['italy',],
	'kate':['coliseum','kano','ikare',],
	'armani':['abuja', 'china',],
	'bola':['USA','canada','japan',],
	'lilian':['mexico',],
	}
	
	
for name, favs in sorted(favorite_places.items()):
	if len(favs) > 1:
		print("\n Name:"+name.upper()+"'s Favourite places are:")
	for fav in favs:
		if len(favs) > 1:
			print("\t",fav.title())
			
		elif len(favs) == 1:
			print("\n Name:"+name.upper()+"'s Favourite place is:"+fav.title())
				
	
	

#ex6-10 favorite numbers:
print("\n favorute numbers 2:")

favorite_numbers = {
	'mike': ['15','45',],
	'seun': ['114','82',],
	'femi': ['4','444',],
	'felix':['18','888'],
	'goke': ['16','666',],
	}

for pesin, fav_no in sorted(favorite_numbers.items()):
	print("\n "+pesin,"'s Favorite Numbers are:")
	
	for f in fav_no:
		print("\t",f)




#ex6-11 cities:
print("\n dictionaries of city:")

cities = {
	'nairobi':{
	'country':'Kenya',
	'population':'1.8m',
	'fact':'also known as massai-place of cool waters'
	},
	
	'sao paulo':{
	'country':'Brazil',
	'population':'18m',
	'fact':'largest city in Brazil',
	},
	
	'moscow':{
	'country':'Russia',
	'population':'11m',
	'fact':'has one of the oldest ballet companies',
	},
	}
	
for city, info in cities.items():
	print('\n CITY NAME:'+city)
	print("\t COUNTRY:"+info['country'])
	print("\t POPULATION:"+info['population'])
	print("\t FACT:"+info['fact'])



#ex6-12 extentions:
print('\n Extentions of many_users.py:')


users = {
	'aeinstein':{
	'first':'albert',
	'last':'einstein',
	'age':'24',
	'location':'princeton',
	'marital status':'single',
	},
	
	'mcurie':{
	'first':'marie',
	'last':'curie',
	'age':'24',
	'location':'paris',
	'marital status':'single',
	},
	'janie007':{
	'first':'jeniiffer',
	'last':'Aniston',
	'age':'29',
	'location':'new ark',
	'marital status':'married',
	},
	
	'mickey15':{
	'first':'michael',
	'last':'hill',
	'age':'26',
	'location':'colorado',
	'marital status':'married',
	},
	}
print("ALL USERS INFO:")
for username, user_info in users.items():
	print("\n USERNAME:"+ username)
	full_name 	= user_info['first'] +" "+ user_info['last']
	location 	= user_info['location']
	status 		= user_info['marital status']
	age 		= user_info['age'] 
	print("\t FULLNAME:"+ full_name)
	print("\t LOCATION:"+location)
	print("\t AGE:"+age)
	print("\t MARITAL STATUS:"+status)
	


print("connecting  users:")
for username, user_info in users.items():
	status 		= user_info['marital status']
	age 		= user_info['age']
	if status == 'married':
		print("\n\nMARRIED user:")
		print("USERNAME:"+username)
	elif status == 'single':
		print("\n\nsingles:")
		print(" USERNAME:"+username)
		print(" AGE:"+age)
