print("\n ex 8-1 passing information to a function:")
def display_message():
	'''FUNCTION with python:'''
	print("i am learning FUNCTION with python")
display_message()

print("\n ex 8-2 favorite book:")
def favorite_book(title):
	'''passing arguemnts to parameter'''
	print("one of my favorite book is "+ title.upper())
	
favorite_book('alice in the wonderLand')


#ex8-3 tshirt
print("\n ex8-3 tshirts.py:")
def make_shirt(size, text):
	'''functiona call for size n text of shirts'''
	print("shirt size: ",size)
	print("text: "+text.upper(),"\n")
make_shirt(52, 'i love python')#POSITIONAL ARGUMENTS
make_shirt(size = 85 , text = 'keep calm and code. ')#KEYWORD ARGUMENTS


print("\n ex8-4 largeshirts.py:")
def make_shirt( text = ' i love python' , size='large',):
	'''functiona call for size n text of shirts'''
	print("shirt size: ",size)
	print("text: "+text.title(),"\n")

make_shirt(size = 'large ')
make_shirt(size= 'medium')
make_shirt(size= 'medium', text = 'keep calm and code')



print("\n\n 8-5 Describe_city:")
def describe_city(city, country ='iceland' ):
	''' describe city'''
	print(city.title()," is in ", country.upper())
describe_city('reykjavik')
describe_city('akureyri')
describe_city('ibadan')

print("\n\n 8-6 city_country:")
def city_country(city, country):
	'''city_country8_6'''
	print("_________________________________")
	print(city.title(),",",country.upper())
	print("_________________________________\n")

city_country('santiago', 'chile')
city_country('reyjavik', 'iceland')
city_country('lagos', 'nigeria')


print("\n\n 8-7 make_album:")
def make_album(artist_name,album_title, tracks = ''):
	'''function for make album'''
	artist_info = {'ARTIST_NAME':artist_name, 'ALBUM':album_title}
	if tracks:
		artist_info ['tracks'] = int(tracks )
	return artist_info
	
artist_1 = make_album('kendrick lamar', 'DAMN', 10)
print(artist_1)

artist_2 = make_album('j.cole', 'KOD', tracks = 23)
print(artist_2)

artist_3 = make_album('xxxtentacion', '17')
print(artist_3)



print("\n\n 8-8 user:")
def user_album(artist_name,album_title, ):
	'''make album'''
	artist_info = {'ARTIST_NAME':artist_name.title(), 'ALBUM':album_title.upper()}
	return artist_info
	
while True:
	print("\n ENTER YOUR FAVORITE ALBUM INFO: ")
	print("(ENTER q to quit:)")
	name = input("Name of artist: ")
	if name == 'q':
		break
	
	album = input("Name of album: ")
	if album == 'q':
		break
	info = user_album(name, album)
	print(info)




