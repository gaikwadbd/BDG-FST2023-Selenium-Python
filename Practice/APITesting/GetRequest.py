import requests
import json
import jsonpath

response = requests.get("https://reqres.in/api/users?page=2")

# print(response)

json_response = json.loads(response.text)
print("---------------------------Pages-----------------------")
#datax = json_response, 'data'
#print(datax)
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages)

datax = jsonpath.jsonpath(json_response, 'data')
#print(str(datax[0][0]))
json_data=dict((datax[0][0]))
print(json_data)
listarr_keys=json_data.keys()
listarr_value=json_data.values()
print(listarr_keys['id'])