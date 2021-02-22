import requests

# post和get区别就是参数不同，post多了data
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

formdata = {
    "from": "zh",
    "to": "en",
    "query": "快乐",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign":"713902.919455",
    "token":"32be6afef14b36b013c1853d09cd7e7f",
    "domain": "common"
}

# post_url = "https://fanyi.baidu.com/"
post_url = "https://fanyi.baidu.com/v2transapi"

response = requests.post(url = post_url, data=formdata, headers = headers)
print(response.content.decode())


