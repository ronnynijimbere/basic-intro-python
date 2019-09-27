from random import randint

ron_words = [
	'Bayou', 'Exks', 'Ziso', 'Zeco','Thibaut','Bobbo', 'Simon', 'Voetsek',
	'Lollo', 'Lucia', 'Haibo', 'Kiki', 'Trevs', 'Danny', 'Makelele'
]

def ronnyboy(word):
	random_pos = randint(0, len(ron_words) -1)
	return f'{word} {ron_words[random_pos]}'


paragraphs = int(input('How paragraphs of ron ipsum: '))

with open('ipsum.txt') as ipsum_original:
	items = ipsum_original.read().split()

	for n in range(paragraphs):
		ron_text = list(map(ronnyboy, items))
		with open('ron_ipsum.txt', 'a') as ipsum_ron:
			ipsum_ron.write(' '.join(ron_text) + '\n\n')