import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")

print(response.status_code)


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.status_code)
print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.content.decode("utf-8"))




# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)

# Headers is a dictionary
print(response.headers)

# Get the content-type from the dictionary.
print(response.headers["content-type"])



# Finding the number of people in Space
# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# 9 people are currently in space.
print(data["number"])
print(data)

