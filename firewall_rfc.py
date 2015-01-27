# Test script to read variables from a spreadsheet.

from __future__ import print_function


infile = "Firewall Request-for-Changes (RFC) Log - Sheet1.csv"

## Open the file with read only permit
f = open(infile, "r")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.readlines()[7:]

## close the file after reading the lines.
f.close()


# Loop over each line in the file.
for line in lines:
	# Note: Need a static data marker for future use.
	#line.split("--BRADBREAK--")
	#parts = line.split("--BRADBREAK--")
	#for part in parts:
	#	print(" ", part)

	#parts2 = [part]
		#parts2.split(",")
	#print("parts2: \n\n")
	#print(parts2)
	#break

	line = line.split(",")
	#print(line)

	
	xITSD = line[0]
	xFirewall = line[1]
	xRFC = line[2]
	xBAU = line[3]
	xSchedDate = line[4]
	xSchedTime = line[5]
	xImplementer = line[6]
	xCompleted = line[7]

	print('ITSD: ',xITSD)
	print('Firewall: ',xFirewall)
	print('RFC: ',xRFC)
	print('BAU: ',xBAU)
	print('Scheduled change date: ',xSchedDate)
	print('Scheduled change time: ',xSchedTime)
	print('Change Implementer: ',xImplementer)
	print('Completed (yes/no): ',xCompleted)
	print('\n\n')









#for line in lines:
	#line = line.split(",")

#	xITSD = line[0]
#	xRFC = line[1]
#	xBAU = line[2]
#	xSchedDate = line[3]
#	xSchedTime = line[4]
#	xImplementer = line[5]
#	xCompleted = line[6]

#	print('ITSD: ',xITSD)
#	print('RFC: ',xRFC)
#	print('BAU: ',xBAU)
#	print('Scheduled change date: ',xSchedDate)
#	print('Scheduled change time: ',xSchedTime)
#	print('Change Implementer: ',xImplementer)
#	print('Completed (yes/no): ',xCompleted)
#	print('\n\n')
# end

