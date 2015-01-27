from __future__ import print_function

w = [1,2,3,5] #list - values may change often
x = (1,2,3,5) #tuple - values will never change (think months of the year)

# list  | value
# ------------
# 0     | 1
# 1     | 2
# 2     | 3
# 3     | 5

# So, x[2] would equal 3.


y = {'jack':123, 'ben':345} # dictionary - key/value pair

# key  | value
# ------------
# jack | 123
# ben  | 345

# So, x['ben'] would equal 345.


# Test code

names = ["Ben", "Sally","Amy","George","Randy"]

print('Flat printing of list.')
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


# does the same thing
print('Flat printing of list (with a loop).')
for name in names:
	print(name)


# To get length
print('Length of list: ',end='')
x = len(names)
print(x)



for index in range(0,len(names)):
	print(names[index],'is found at index:',index)