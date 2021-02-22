import requests

proxies = {
    "http":"http://183.166.70.242:9999",
    # "https":"http://183.166.71.112:9999",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

r = requests.get("https://www.baidu.com/",proxies = proxies, headers = headers)

print(r.status_code)
