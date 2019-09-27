#def greet():
#	print('hello world')

#greet()

#def greet(name, time):
#	print(f"Good {time} {name}, hope you are well")

#greet("ronny", "evening")	

#def greet(name, time):
#	print(f"Good {time} {name}, hope you are well")

#name = input('enter your name: ')
#time = input('enter the time of the day: ')

#greet(name, time)	

def area(radius):
	return 3.142 * radius * radius

def vol(area, length):	
	print(area * length)

radius = int(input('enter a radius: '))
length = int(input('enter a length: '))

#area_calc = area(radius)
vol(area(radius), length)	