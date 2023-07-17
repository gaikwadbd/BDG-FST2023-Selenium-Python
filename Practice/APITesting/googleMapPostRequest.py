import requests

post_Response = requests.post("https://rahulshettyacademy.com/maps/api/place/add/json", params={'key': 'qaclick123'},
                              json={
                                  "location": {
                                      "lat": -38.383494,
                                      "lng": 33.427362
                                  },
                                  "accuracy": 50,
                                  "name": "Frontline house",
                                  "phone_number": "(+91) 983 893 3937",
                                  "address": "29, side layout, cohen 09",
                                  "types": [
                                      "shoe park",
                                      "shop"
                                  ],
                                  "website": "http://google.com",
                                  "language": "French-IN"
                              }, headers={"Content-Type": "application/json"})

print("------------------------------->by using then text---------------->")
print(post_Response.text)
print(post_Response.status_code)
print(post_Response.headers)

print("------------------------------->by using then JSON---------------->")
print(post_Response.json())

print("------------------------------->print on place id ---------------->")
post_Response_id = post_Response.json()['place_id']
print(post_Response.json()['place_id'])