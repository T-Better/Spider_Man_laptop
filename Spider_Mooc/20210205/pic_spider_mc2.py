import requests
import os

url = "http://pic1.win4000.com/m00/fa/8a/19a1e1a68072837bb108f7656badaffd.jpg"

root = "/Super_Coder/Spider_Man/Spider_Heima/"

path = "erciyuan.html"

try:
    if os.path.exists(path):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,"wb") as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
