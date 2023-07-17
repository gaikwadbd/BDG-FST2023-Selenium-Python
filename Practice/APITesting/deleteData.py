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

post_Response_id = post_Response.json()['place_id']
print(post_Response.json()['place_id'])
print("------------------------------->Delete the place id ---------------->")

del_response = requests.delete("https://rahulshettyacademy.com/maps/api/place/add/json", params={'key': 'qaclick123'},
                               headers={"Content-Type": "application/json"}, json={
        "place_id": post_Response_id
    }
                               )
print("Deleted the placed id :------------------>", del_response.status_code)

print("------------------------------->Get the status of deleted post_response id ---------------->")
response_Get = requests.get("https://rahulshettyacademy.com/maps/api/place/get/json",
                            params={'key': 'qaclick123', 'place_id': post_Response_id})

print("Deleted the placed id :------------------>", response_Get.json())






"""C:\Python39\python.exe D:/pythonProject/API-Backend-Automation/API_Calls/DELETECALL_03.py
b7ed07cd8bb90e99812b5d5478073eba
------------------------------->Delete the place id ---------------->
Deleted the placed id :------------------> 200
------------------------------->Get the status of deleted post_response id ---------------->
Deleted the placed id :------------------> {'location': {'latitude': '-38.383494', 'longitude': '33.427362'}, 'accuracy': '50', 'name': 'Frontline house', 'phone_number': '(+91) 983 893 3937', 'address': '29, side layout, cohen 09', 'types': 'shoe park,shop', 'website': 'http://google.com', 'language': 'French-IN'}
Process finished with exit code 0
"""