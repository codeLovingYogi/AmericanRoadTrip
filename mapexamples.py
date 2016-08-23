import folium

# create base map using default OpenStreetMap tiles
map_osm = folium.Map(location=[45.5236, -122.6750])
map_osm.save('osm.html')

# using Stamen Terrain, Toner, Mapbox Bright, Control room tiles
stamen = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner',
                    zoom_start=13)
stamen.save('stamen_toner.html')

# for passing Leaflet.js compatible custom tileset
folium.Map(location=[45.372, -121.6972],
           zoom_start=12,
           tiles='http://{s}.tiles.yourtiles.com/{z}/{x}/{y}.png',
           attr='My Data Attribution')

# plotting with Leaflet style location marker with popup text
map_1 = folium.Map(location=[45.372, -121.6972],
                   zoom_start=12,
                   tiles='Stamen Terrain')
folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows').add_to(map_1)
folium.Marker([45.3311, -121.7113], popup='Timberline Lodge').add_to(map_1)
map_1

# plotting colors and marker icon types (from bootstrap)
map_1 = folium.Map(location=[45.372, -121.6972],
                   zoom_start=12,
                   tiles='Stamen Terrain')
folium.Marker([45.3288, -121.6625],
              popup='Mt. Hood Meadows',
              icon=folium.Icon(icon='cloud')
             ).add_to(map_1)
folium.Marker([45.3311, -121.7113],
              popup='Timberline Lodge',
              icon=folium.Icon(color='green')
             ).add_to(map_1)
folium.Marker([45.3300, -121.6823],
              popup='Some Other Location',
              icon=folium.Icon(color='red',icon='info-sign')
              ).add_to(map_1)
map_1

map_1.save('markers.html')

# plotting circle-style markers, with custom size and color
map_2 = folium.Map(location=[45.5236, -122.6750],
                   tiles='Stamen Toner',
                   zoom_start=13)
folium.Marker([45.5244, -122.6699],
              popup='The Waterfront'
             ).add_to(map_2)
folium.CircleMarker([45.5215, -122.6261],
                    radius=500,
                    popup='Laurelhurst Park',
                    color='#3186cc',
                    fill_color='#3186cc',
                   ).add_to(map_2)
map_2

map_2.save('custommarkers.html')
