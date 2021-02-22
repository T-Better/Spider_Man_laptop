import requests


# @retry(stop_max_attempt_number=3)
def getHTMLtext(url):
    """
    获取htmltext的方法
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }
    proxies = {
        "https":"http://183.166.71.112:9999"
    }

    try:
        r = requests.get(url,proxies=proxies,headers=headers)
        r.raise_for_status()  # 如果状态不是200，抛出httperror异常 TODO 学一下这个和raise的区别
        r.encoding = r.apparent_encoding  # 就是先用apparent_encoding方式分析一下内容的编码方式，然后以此方式对返回内容进行解码
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://www.baidu.com"
    print(getHTMLtext(url))