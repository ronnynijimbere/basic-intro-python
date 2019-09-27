my_name = "ronny" #global variable

def print_name():
	global my_name #this will override the above global variable
	my_name = "nijimbere" #local variable
	print('the name inside the function', my_name)

print_name()
print('outside the function the name is', my_name)	