def belt_count(dictionary):
	belts = list(dictionary.values())
	for belt in set(belts):
		num = belts.count(belt)
		print(f'There are {num} {belt} belts')

#def ron_intro(dictionary):
#	for key, val in dictionary.items():
#		print(f'I am {key} and I am a {val} belt')

ron_belts = {}

while True:
	ron_name = input('enter a ron name: ')
	ron_belt = input('enter a belt color: ')
	ron_belts[ron_name] = ron_belt


	another = input('add another? (y/n)')
	if another == 'y':
		continue
	else:
		break

#ron_intro(ron_belts)	
belt_count(ron_belts)	