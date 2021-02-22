import requests


response = requests.get("http://www.sina.com.cn")

# 看下默认拿的什么请求头请求的数据
print(response.request.headers)

# 查看完整url
print(response.url)

# 查看响应头部字符编码
print(response.encoding)

# 查看响应码
print(response.status_code)

# 与下面reponse.text对比
print(response.content.decode())
