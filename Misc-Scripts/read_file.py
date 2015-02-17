from __future__ import print_function

infile = "Firewall Request-for-Changes (RFC) Log - Sheet1.csv"

## Open the file with read only permit
f = open(infile, "r")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.readlines()

## close the file after reading the lines.
f.close()

## If the file is not empty keep reading line one at a time
## till the file is empty


# While loop
#while lines:
#    print (lines[0],end='')
#    #lines = f.readline()


# For loop
for index in range(0,len(lines)):
	print(lines[index],end='')
