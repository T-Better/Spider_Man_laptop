import requests
from retrying import retry

class SpiderBaidu():

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
        self.url = "https://www.baidu.com"
        self.key_word = "requests.text和requests.content.decode的区别"

    @retry(stop_max_attempt_number = 5)
    def parse_url(self):
        """

        :return:
        """
        try:
            res = requests.get(self.url,params = self.key_word,timeout =3, headers=self.headers)
            res.raise_for_status()
            return res.content.decode()
        except:
            return "爬取失败"

    def save_res(self,res):
        """

        :return:
        """
        with open("baidu_res.html","w",encoding="utf-8") as f:
            f.write(res)

    def run(self):
        # 1.发送请求，获取相应
        baidu_res = self.parse_url()

        # 2. 保存数据
        self.save_res(baidu_res)

if __name__ == "__main__":
    spider_baidu = SpiderBaidu()
    spider_baidu.run()