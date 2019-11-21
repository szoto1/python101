"""
openstrretmap - api do map, free


"""

import folium

m = folium.Map(location=[45.523,-122.6750])
m.save('index.html')
