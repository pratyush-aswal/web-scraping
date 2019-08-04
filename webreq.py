import requests

url="http://maps.googleapis.com/maps/api/geocode/json"
addr={'address':'1600 Amphitheatre Parkway, Mountain View, CA'}
response = requests.get(url,addr)
print(response.text)