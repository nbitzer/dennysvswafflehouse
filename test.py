import googlemaps
from onepassword import OnePassword
import json
from datetime import datetime

op = OnePassword()

gmaps_client_key = op.get_item(uuid="p3qnn34pdvkizi5u6m5xlf34p4", fields="value")
print(gmaps_client_key)

# gmaps = googlemaps.Client(key=gmaps_client_key)

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# print(geocode_result)
