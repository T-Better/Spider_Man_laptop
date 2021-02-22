import requests


def get_jindong_html(url):
    """
    获取京东数据
    :param url:
    :return:
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # 如果不是200，产生异常，requests.httperror
        return r.content.decode()
    except:
        return "请求错误"


if __name__ == "__main__":
    url = "https://item.jd.com/2967929.html"
    get_jindong_html_result = get_jindong_html(url)
    with open("jingdong_rongyao8.html","w",encoding="utf-8") as f:
        f.write(get_jindong_html_result)
