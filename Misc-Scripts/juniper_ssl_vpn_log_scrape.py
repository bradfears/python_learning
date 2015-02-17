from __future__ import print_function

infile = "C:\\Users\\bfears\\Downloads\\juniper_ssl_vpn.log"

## Open the file with read only permit
f = open(infile, "r")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.readlines()

## close the file after reading the lines.
f.close()

## If the file is not empty keep reading line one at a time
## till the file is empty


import re
for index in range(0,len(lines)):
	regex = '[0-9]+(?:\.[0-9]+){3}](.+?)\(MSU Net\)'
	userName = re.findall(regex, lines[index])		
	print(userName[0])
	