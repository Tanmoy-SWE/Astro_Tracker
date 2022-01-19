import json
import turtle
import urllib.request
import time
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result= json.loads(response.read())
print(result['number'])
people = result['people']
for p in people:
    print(p['name'])
#print Longitude and Latitude
g = geocoder.ip('me')
print(g.latlng)

#Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180, -90, 180, 90)

#Load the world map image
screen.bgpic("map.gif")
screen.register_shape('ISS.gif')
iss = turtle.Turtle()
iss.shape('ISS.gif')
iss.setheading(45)
iss.penup()
input('stop')

while True :
    #Load the current status of the ISS in real-time
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #Extract the ISS location
    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    lat = float(lat)
    lon = float(lon)
    print('\nLatitude : '+str(lat))
    print('\nLongtitude : ' + str(lon))

    iss.goto(lon, lat)

    time.sleep(5)