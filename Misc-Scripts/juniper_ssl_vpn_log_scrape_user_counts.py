from __future__ import print_function

# pythex - Python regular expression tester
# http://pythex.org

infile = "C:\\Users\\bfears\\Downloads\\juniper.cc-prd.access.20150213-a.log"

## Open the file with read only permit
f = open(infile, "r")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.readlines()

## close the file after reading the lines.
f.close()

ipList = []
nameList = []


## If the file is not empty keep reading line one at a time
## till the file is empty

import re
for index in range(0,len(lines)):
	regex_ip = '\[[0-9]+(?:\.[0-9]+){3}\]'
	regex_username = '\[[0-9]+(?:\.[0-9]+){3}](.+?)\(MSU Net\)\[_MSUNet.users]'

	user_outside_IP = re.findall(regex_ip, lines[index])
	if user_outside_IP[0]:
		raw_outside_IP = user_outside_IP[0]
		raw_outside_IP = raw_outside_IP.replace('[', '')
		raw_outside_IP = raw_outside_IP.replace(']', '')
		ipList.append(raw_outside_IP)

	if raw_outside_IP:
		userName = re.findall(regex_username, lines[index])		

		if len(userName) == 0:
			userName_stripped = "NOBODY"			
		else:
			userName_stripped = userName[0]
			
		userName_stripped = userName_stripped.replace('[','')
		userName_stripped = userName_stripped.replace(']','')
		userName_stripped = userName_stripped.replace(' ','')
		
		nameList.append(userName_stripped)
			

for index in range(0,len(nameList)):
	if nameList[index] == "NOBODY":		
		continue;
	else:
		print("Username: " + nameList[index])
		print("Outside IP: " + ipList[index])
			
	