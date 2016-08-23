import csv
import math
import folium

# get file name
fname = input('Enter file name: ')
if(len(fname) < 1):
    fname = 'placestomap.csv'

# open and read file
with open(fname) as f:
    reader = csv.reader(f)
    locations = list(reader)

n = len(locations) 
middle = math.floor(n/2)

tripmap = folium.Map(location=[locations[middle][5], locations[middle][6]],
                   zoom_start=5,
                   tiles='Stamen Terrain')

for i in range(1, n):
    folium.Marker([locations[i][5], locations[i][6]],
              popup=locations[i][4],
             ).add_to(tripmap)

tripmap.save('roadtripmap.html')


