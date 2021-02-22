import requests
from retrying import retry


class Spider_amazon():
    """
    获取亚马逊的类对象
    """

    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        self.proxies = {
            "http": "http:///183.166.70.242:9999"
        }
        self.amazon_url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"

    @retry(stop_max_attempt_number=5)
    def parse_url(self,url):
        """
        发送请求获取相应
        :return:
        """
        print("-" * 20)
        try:
            res = requests.get(url, timeout=30, proxies=self.proxies, headers=self.headers)
            res.raise_for_status()
            return res.content.decode()

        except:
            return "请求异常"

    def save_html(self,res):
        """
        保存
        :return:
        """
        with open("amazon_html_res","w",encoding="utf-8") as f:
            f.write(res)

    def run(self):
        """
        代码跑起来的主逻辑
        :return:
        """
        # 1.发送请求，获取响应
        parse_html_res = self.parse_url(self.amazon_url)
        # 2. 解析并提取想要的数据 暂不做

        # 3. 将有用的数据保存到本地
        return self.save_html(parse_html_res)

if __name__ == "__main__":
    spider_amazon = Spider_amazon()
    spider_amazon.run()
