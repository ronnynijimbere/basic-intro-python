def crook_dec(func):

	def func_wrapper():
		#code before functioon
		print('*crook*')
		func()
		#code after function
		print('*crook*')

	return func_wrapper	

@crook_dec
def question():
	print('can you rob a bank on my behalf?')

@crook_dec
def answer():
	print('screw you ronny')	

question()
answer()	