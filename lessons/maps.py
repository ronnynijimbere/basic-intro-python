#map(function, data)
from random import shuffle

def jam(word):
	anagram = list(word)
	shuffle(anagram)
	return ''.join(anagram)


words = ['never', 'give', 'up']
anagrams = []


#comprehension method
print([jam(word) for word in words])

#map function
#print(list(map(jam, words)))


#for loop method
#for word in words:
#	anagrams.append(jam(word))
#print(anagrams)	

