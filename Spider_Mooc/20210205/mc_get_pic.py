import requests

path = "/home/claren/Super_Coder/Spider_Man/Spider_Mooc/20210205/abc.jpg"
url = "http://pic1.win4000.com/m00/fa/8a/19a1e1a68072837bb108f7656badaffd.jpg"

r = requests.get(url)

print(r.status_code)

with open(path,"wb") as f:
    f.write(r.content)





