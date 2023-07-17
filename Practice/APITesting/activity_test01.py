import requests

auth_token='sdfghjkloerdtfyguhiopfghjkl;fghjkl'
hed = {'Authorization': 'Bearer ' + auth_token}
data = {'app' : 'aaaaa'}

url = 'https://api.xy.com'
response = requests.post(url, json=data, headers=hed)
print(response)
print(response.json())