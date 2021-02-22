import requests


url = "https://www.ip138.com/iplookup.asp?ip=200.10.20.33&action=2"
headers = {"user-agent":"Mozilla/5.0"}

r = requests.get(url,headers=headers)

r.encoding = r.apparent_encoding

print(r.request.headers)

print(r.status_code)

print(r.text[-500:])

# print(r.text)