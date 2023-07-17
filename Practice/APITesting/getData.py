import requests
import json


response = requests.get("https://reqres.in/api/users?page=2")

print(response)
print("-----------------------response.content---------------")

print(response.content)

print("-------------------------response.headers------------")
print(response.headers)
print("-------------------------response.status code------------")
print(response.status_code)
print("-------------------------response.content------------")
print(response.content)
print("-------------------------response.cookies------------")
print(response.cookies)
print("-------------------------response.encoding------------")
print(response.encoding)
print("-------------------------response.reason------------")
print(response.reason)
print("-------------------------response.history------------")
print(response.history)