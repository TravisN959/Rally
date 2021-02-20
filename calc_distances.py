import getAPI
import requests
import googlemaps
from boto.s3.connection import S3Connection
key = S3Connection(os.environ['GOOGLE_KEY'])
distance_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
directions_url = 'https://maps.googleapis.com/maps/api/directions/json?'

def travel_time(loc_a, loc_b):
    
    r = requests.get(distance_url + "origins=" + loc_a + "&destinations=" + loc_b + "&key=" + key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    
    return time


def get_directions(loc_a, loc_b):
    r = requests.get(directions_url + "origin=" + loc_a + "&destination=" + loc_b + "&key=" + key) 
    directions = r.json()['routes'][0]['legs'][0]['steps']
    steps_str = ""
    for i in range(len(directions)):
        steps_str += directions[i]['html_instructions'] + "\n"
    return steps_str


def get_distance(loc_a, loc_b):
    r = requests.get(distance_url + "origins=" + loc_a + "&destinations=" + loc_b + "&key=" + key)
    distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
    return distance

# distStr = get_distance('los angeles', '4199 Campus Dr')
# value = float(distStr[:-2])
# print(distStr[:-1])
# print(distStr[:-2])
# print(value)
# print(type(value))