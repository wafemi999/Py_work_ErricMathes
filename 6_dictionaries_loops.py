print("\n looping through all key-values in a dictionary")

user_0 = {
	'username':'efermi',
	'last':'enrico',
	'first':'fermi',
	}

for k, v in user_0.items():
	print("\n key: ", k)
	print(" value: ", v)


print("\n looping throuugh all key_value pairs favourite languages:")
favorite_languages = {
	'jen':'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}


for name, languages in favorite_languages.items():
	print("\n",name.title(),"'s favourite programming language is ", languages.upper())




print("\n looping throuugh all keys in a dictionary:")
print("people who took part in the poll of favourite progamming language:")
for name in favorite_languages.keys():
	print(name.title(),"")


print("\n looping throuugh specific keys-values in a dictionary:")

friends = ['sarah', 'phil']

for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" hi", name.title()," i see your favourite programming language is:",
		favorite_languages[name].upper(), "!")
		
		

print("\n use the keys() method to find out if a particular person, wasnt part of the poll:")
if 'erin' not in favorite_languages.keys():
	print("ERIN please take your poll")
	
	
	
	
print("\nlooping in a sorted order:")	
for name in sorted(favorite_languages.keys()):
	print(name.upper()," thank you for taking the poll.")


print("\n looping through values of a dictionary:")
print("\n progamming languages mentioned during the poll are:")
for language in favorite_languages.values():
	print(language.upper())


print("\n use of set() to list values uniquely(without repetition):")
for language in set(favorite_languages.values()):
	print(language.upper())



