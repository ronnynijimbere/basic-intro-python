with open('files/write.txt', 'w') as write_file:
	write_file.write('python is great to learn')
	#write_file.write('\nstop being a cow and learn python')

with open('files/write.txt', 'a') as write_file:
	write_file.write('\nstop being a cow and learn python') 

quotes = [
	'\nI remember when i started to learn to code',
	'\nThose days were tough and sucked',
	'\nBut today things are going well but there is still much to learn'
]	

with open('files/write.txt', 'a') as write_file:
	write_file.writelines(quotes)