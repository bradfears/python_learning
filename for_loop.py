from __future__ import print_function

num = 18 # a number greater than 2 and less than 10
prime = True

for test in range(2,num):
	if num % test == 0 and num != test:
		print(num,'equals',test, '*', num/test)
		prime = False
		break

if prime:
	print(num,'is a prime number.')
else:
	print(num,'is not a prime number.')
