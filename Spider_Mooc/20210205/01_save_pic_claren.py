import requests


# 发送请求
r = requests.get("https://tva1.sinaimg.cn/large/006Xzox4gy1gdfnksbr6gg309q09qmy9.gif")

# 重点 保存
with open("楼上智商不足，需要充值红包.gif","wb") as f:
    # 这里用了wb，w表示写入,b表示bytes类型，就是可读可写bytes类型，当遇到pdf、图片等格式使用此方式
    f.write(r.content)  # 这里也没有用r.content.decode()，因为只是一个bytes返回，不存在编码解码，所以不解码

