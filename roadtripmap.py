import csv

# get file name
fname = input('Enter file name: ')
if(len(fname) < 1):
	fname = 'placestomap.csv'

# open and read file
with open(fname) as f:
	reader = csv.reader(f)
	locations = list(reader)

for each in locations:
	print(each)

print('f closed', f.closed)