import requests

# AP url

response = requests.delete("https://reqres.in/api/users/2")

print(response)
print("------------------------status code")

print(response.status_code)