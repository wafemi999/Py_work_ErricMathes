
#permanent sorting
print("list of cars alphabetically:")
cars = ["bmw", "audi", "toyota","subaru" ]
cars.sort()
print(cars)
print("\n","list of cars alphebetically in a reverse order:")
cars.sort(reverse = True)
print(cars)
print("\n")
#temporary sorting sorted()
cars = ["bmw", "audi", "toyota","subaru" ]
print("here is the original list:") 
print("\n\t",cars)
print("\n")
print("here is the sorted list:")
print("\n\t",sorted(cars))
print("\n")
print("Here is the original list again:")
print("\n\t",cars)
print("\n")
print("here is the reverse order temporarirly:")
cars.reverse()
print(cars)
print("\n")
print("here is the original list again:")
cars.reverse() 
print("\n\t",cars)
print("\n")
#length of a list len()
print("the number cars in the store is:")
print(len(cars))

#exercise 3-8
print("\t places i will  visit:")
Dream_places = ['japan', 'new jersey', 'italy', 'australia', 'canada']
print("\t",Dream_places)
print("\n\t""sorted dream paces:","\n\t",sorted(Dream_places))
print("\n\t""original list of  places again: ")
print("\t",Dream_places)
print("\n\t","The list of places in reverse alphabetically")
print("\t",sorted(Dream_places,reverse=True))
print("\n")
print("\n\toriginal list of  places again: ")
print(Dream_places)
Dream_places.reverse()
print("\n")
print("\nList of  places in reverse order: ")
print("\t",Dream_places)
print("\n List of places in original order again")
Dream_places.reverse()
print("\t",Dream_places)
print("\n  peramanently sorted  places:")
Dream_places.sort()
print("\t",Dream_places)
print("\n")
Dream_places.sort(reverse=True)
print("peramanently sorted  places in alphabetically reversed order:")
print("\t",Dream_places)


#exercise  3-10
mountains = ['kilimanjaro', 'mount kenya','mount elgon', 'cameroon mountain', 'ras dashen']
rivers = ['nile', 'amazon', 'yangzte', 'mississippi','lena', ]
languages = ['chinese', 'arabic', 'spanish', 'hindi', 'bengali']
print("\n")
print("\n", "here are the origina lists:")
print("\n\t", "Mountains:")
print("\n\t", mountains)
print("\n\t", "rivers:")
print("\n\t", rivers)
print("\n\t", "languages:")
print("\n\t", languages)

print("\n", "here are the  lists temporarily sorted alphabetically :")
print("\n\t", "Mountains:")
print("\n\t", sorted(mountains))
print("\n\t", "rivers:")
print("\n\t", sorted(rivers))
print("\n\t", "languages:")
print("\n\t", sorted(languages))

print("\n", "here is the  lists temporarily sorted alphabetically(reverse) :")
print("\n\t", "Mountains:")
print("\n\t", sorted(mountains, reverse = True))
print("\n\t", "rivers:")
print("\n\t", sorted(rivers, reverse = True))
print("\n\t", "languages:")
print("\n\t", sorted(languages, reverse = True))

print("\n", "here is the original lists again:")
print("\n\t", "Mountains:")
print("\n\t", mountains)
print("\n\t", "rivers:")
print("\n\t", rivers)
print("\n\t", "languages:")
print("\n\t", languages)


print("\n", "here is the original lists in reverse order(not alphabetically):")
print("\n\t", "Mountains:")
mountains.reverse()
print("\n\t", mountains)
print("\n\t", "rivers:")
rivers.reverse()
print("\n\t", rivers)
print("\n\t", "languages:")
languages.reverse()
print("\n\t", languages)


print("\n", "Permanent sorting of the mountains,rivers and languagues(irreversible):")
print("\n\t", "Mountains:")
mountains.sort()
print("\n\t", mountains)
print("\n\t", "rivers:")
rivers.sort()
print("\n\t", rivers)
print("\n\t", "languages:")
languages.sort()
print("\n\t", languages)



print("\n", "Permanent reverse(unalphabetically) of the mountains,rivers and languagues(irreversible):")
print("\n\t", "Mountains:")
mountains.sort(reverse = True)
print("\n\t", mountains)
print("\n\t", "rivers:")
rivers.sort(reverse = True)
print("\n\t", rivers)
print("\n\t", "languages:")
languages.sort(reverse = True)
print("\n\t", languages)







