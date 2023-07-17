import json

import requests

response = requests.get("https://rahulshettyacademy.com/maps/api/place/get/json",
                        params={'key': 'qaclick123', 'place_id': 'd92177d8aa3a1ce05155b434e59d7f45'})

# print(response.text) # print all response content
# print(response.status_code) # print the status code
# print(type(response.text)) # print the type of response
response_str = response.text
print(type(response_str))  # print the type of response
dict_response = json.loads(response_str)  # convert string to json format
print(type(dict_response))  # type of response
print("This is output name is ", dict_response['name'])  # print the dict name

json_response = response.json()  # by using this method we can convert any file.
print(json_response)  # print all response content
print(type(json_response))
print(json_response['phone_number'])
print("This is json parse with 2 dict type or complex type :", json_response['location']['longitude'])

print("------------------------------------Header from response----------->")
dict_Header = response.headers
print(dict_Header)
print(type(dict_Header))
print("this is Content-Type :------>", dict_Header['Content-Type'])


for loc in json_response:
    if json_response['location']['longitude'] == '33.427362':
        print("if condition is ok :--->", json_response['location'])
        break

expected_Result = {'latitude': '-38.383494', 'longitude': '33.427362'}

assert json_response['location'] == expected_Result

"""C:\Python39\python.exe D:/pythonProject/API-Backend-Automation/API_Calls/GETCALL_001.py
<class 'str'>
<class 'dict'>
This is output name is  Frontline house
{'location': {'latitude': '-38.383494', 'longitude': '33.427362'}, 'accuracy': '50', 'name': 'Frontline house', 'phone_number': '(+91) 983 893 3937', 'address': '29, side layout, cohen 09', 'types': 'shoe park,shop', 'website': 'http://google.com', 'language': 'French-IN'}
<class 'dict'>
(+91) 983 893 3937
This is json parse with 2 dict type or complex type : 33.427362
------------------------------------Header from response----------->
{'Date': 'Wed, 26 Oct 2022 10:43:41 GMT', 'Server': 'Apache/2.4.41 (Ubuntu)', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST', 'Access-Control-Max-Age': '3600', 'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With', 'Content-Length': '257', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'application/json;charset=UTF-8'}
<class 'requests.structures.CaseInsensitiveDict'>
this is Content-Type :------> application/json;charset=UTF-8
if condition is ok :---> {'latitude': '-38.383494', 'longitude': '33.427362'}
Process finished with exit code 0
"""