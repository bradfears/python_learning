from __future__ import print_function

sum = 0
add = -1

while add != 0:
	print('The current sum is:',sum)
	print('How much would you like to add?',end='')
	raw_add = raw_input('(Type 0 to end program): ')
	add = int(raw_add)
	sum = sum + add