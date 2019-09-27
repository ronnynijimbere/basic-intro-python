from space.planet import Planet
from space.calc import planet_mass, planet_vol

mars = Planet('Mars', 300000, 8, 'Mars System')

mars_mass = planet_mass(mars.gravity, mars.radius)
mars_vol = planet_vol(mars.radius)

print(f'{mars.name} has a mass of {mars_mass} and a volume of {mars_vol}')	






'''
class Planet:

	shape = 'round' #class level attr

	def __init__(self, name, radius, gravity, system):
		self.name = name #instance attr
		self.radius = radius #instance attr
		self.gravity = gravity #instance attr
		self.system = system #instance attr

	def orbit(self): #instance method
		return f'{self.name} is orbiting in the {self.system}'

	#class method: common for all our planets (class level attr)	
	@classmethod
	def commons(cls):
		return f'All planets are {cls.shape} because of gravity'

	#static method: has no to class level attr,only has access to parameters we pass individually
	@staticmethod
	def spin(speed = '2000 miles per hour'):
		return f'The planet spins and spins at {speed}'			

#new object based on the above class
#hoth = Planet('Hoth', 200000, 5.5, 'Hoth system')
#print(f'Name is: {hoth.name}')	
#print(f'Radius is: {hoth.radius}')
#print(f'the gravity is: {hoth.gravity}')	
#print(hoth.orbit())	

mars = Planet('Mars', 300000, 8, 'Mars System')	
#print(f'Name: {mars.name}')
#print(f'Radius: {mars.radius}')
#print(f'Gravity: {mars.gravity}')
#print(mars.orbit())
#print(Planet.shape)
#print(Planet.commons())
#print(Planet.spin())
print(mars.spin('a very high speed'))
'''