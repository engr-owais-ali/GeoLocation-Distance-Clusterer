#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import folium
from geopy.distance import geodesic


# Sample JSON data
api_url = "https://api.npoint.io/f26432e9e880999eeb1b"
response = requests.get(api_url)


data = response.json()

print(data)



# In[28]:


# Calculate distances between markers
def calculate_distances(coords1, coords2):
    return geodesic(coords1, coords2).kilometers

# # Create a map centered around the first marker's coordinates
# map_center = [data['features'][0]['geometry']['coordinates'][1], data['features'][0]['geometry']['coordinates'][0]]
# mymap = folium.Map(location=map_center, zoom_start=10)



# Create a map centered around the first marker's coordinates
map_center = [data['features'][0]['geometry']['coordinates'][1], data['features'][0]['geometry']['coordinates'][0]]
mymap = folium.Map(location=map_center, zoom_start=10)

x,y,z = 3,2,3

# Add a satellite tile layer from Mapbox (replace 'YOUR_MAPBOX_ACCESS_TOKEN' with your actual token)
folium.TileLayer(
    tiles='https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYWxpYmFiYTEyZSIsImEiOiJjbGxkczgya3owY2Q4M2prYTgyYXB3bHF0In0.MUq96VamXb-6sBOOJXBM-w',
    attr='Mapbox',
    name='Satellite',
).add_to(mymap)






# Create a list to store marker locations
marker_locations = []

i = 0

# Add markers to the map and calculate distances
for feature in data['features']:
    lon, lat = feature['geometry']['coordinates']
    marker_color = 'blue'  # Default color
    current_coords = (lat, lon)
    
#     print(f"for {i}. the respective distance to {k} is : {d}")
    print(f"{i}. Current coord: {current_coords}")
    k = 0
    for feature in data['features']:
        lon2, lat2 = feature['geometry']['coordinates']
        second_coords = (lat2, lon2)
        
        if not (second_coords == current_coords):
            print(f"{k}. {second_coords}", end =" ")
            print(f". distance : {calculate_distances(current_coords, second_coords)}")
            if calculate_distances(current_coords, second_coords) < 15:
                marker_color = 'red'
        k = k + 1
#                 break
    
#     for coords in marker_locations:
#         if calculate_distances(current_coords, coords) < 5:
#             marker_color = 'red'
#             break
    
    print("Check ")
    
    # Create a marker with a popup (label)
    marker = folium.Marker(
        location=[lat, lon],
        icon=folium.Icon(color=marker_color),
        popup=f"{i}. Coordinates: {lat}, {lon}"  # Customize the popup content here
    )
    print(f"MARKING: {i}. Coordinates: {lat}, {lon}")
    mymap.add_child(marker)
    marker_locations.append(current_coords)
    
    i = i + 1
    
    

# Save the map as an HTML file
mymap.save('satt_map_with_colored_markers_and_labels.html')

marker_locations


# In[ ]:





# In[31]:


from leaflet_offline import OfflineTileDownloader



