import csv
f = open('201703_Taiwan.csv','r')

sensor = ''
count = 0

for row in csv.reader(f):
	if row[2] != sensor:
#		print sensor + " " + str(count)
		count = 0
		sensor = row[2]
#		print sensor
	else:
		count = count + 1
	if row[2] == '28C2DDDD4774':
		print row

