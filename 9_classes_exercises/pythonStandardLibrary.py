from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['remy'] = 'c'
favorite_languages['sarah'] = 'ruby'
favorite_languages['edward'] = 'c#'
favorite_languages['phil'] = 'python'

for names,languages in favorite_languages.items():
	print(names.upper(),"'s favorite language is", languages.title() + ".")
