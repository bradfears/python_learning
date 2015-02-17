from __future__ import print_function

# juniper_ssl_vpn_log_scrape_user_counts.py
# 2015.02.16 - Brad Fears

# This is a handy tool...
# pythex - Python regular expression tester
# http://pythex.org

# I wrote this.
# Me.  Brad!?  Yeah, that guy.

infile = "C:\\Users\\bfears\\Downloads\\juniper.cc-prd.access.20150213-a.log"

## Open the file with read only permit.
f = open(infile, "r")

## Use readlines to read all lines in the file.
## The variable "lines" is a list containing all lines.
lines = f.readlines()

## Close the file after reading the lines.
f.close()

ipList = []
nameList = []


## If the file is not empty, keep reading lines one at a time
## until the file is empty.

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
			

## Now I have a list (array) of usernames and a list (array) of their IPs.
## That was act 1.  I hope you enjoyed it.
## I need a banana.

## Other stuff I need now:
## 1. Identify the unique usernames
## 2. Run a counter on the names

# I'm missing the obvious.
# But I found the not-so-obvious.

from collections import Counter

uniqueTotals = Counter(nameList).most_common()
# I want to find the MOFO who wrote this and have his baby.
# "Don't be shy...you know you so sexy."
# I will conceed that my harvesting of IPs was unnecessary, but good learning.

for index in range(0,len(uniqueTotals)):	
	print(uniqueTotals[index])

