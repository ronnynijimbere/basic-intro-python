grades = ['A', 'C', 'E', 'F', 'F', 'B', 'D']

def remove_fails(grade):
	return grade != 'F'

#print(list(filter(remove_fails, grades)))

# using for loop
#filtered_grades = []
#for grade in grades:
#	if grade != 'F':
#		filtered_grades.append(grade)
#print(filtered_grades)	

#using comprehension method	
print([grade for grade in grades if grade !='F'])