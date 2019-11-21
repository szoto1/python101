"""
openstrretmap - api do map, free

https://github.com/python-visualization/folium
"""

import folium

m = folium.Map(location=[45.523,-122.6750])


popup = "Rower mevo"
tooltip = "Kliknij"

rowery = [
[45.523,-122.6750], #to moze byc dict{majacym lokalizacje geo i np naladowanie  baterii itp}
[44.523,-122.6750]
]

for rower in rowery:
    marker = folium.Marker(rower, popup=popup, tooltip=tooltip)
    marker.add_to(m)

m.save('index.html')