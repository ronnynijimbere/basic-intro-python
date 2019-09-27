#ganstas = ['tupac', 'biggie', 'snoop dog', '50 cent']

#for gansta in ganstas:
#	print(gansta)

#for gansta in ganstas[1:3]:
#	print(gansta)

#for gansta in ganstas:
#	if gansta == 'snoop dog':
#	   print(f'{gansta} - real nigga')
#	   break
#	else:
#	   print(gansta)	

age = 25
num = 0

while num < age:
	if num == 0:
		num += 1
		continue
	if num % 2 == 0:
		print(num)
	if num > 10:
		break	
	num += 1	
