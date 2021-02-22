import requests



class TiebaSpider():
    """
    实现爬取贴吧的一个爬虫，可以爬去各个贴吧
    """
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name +"&ie=utf-8&pn={}"
        self.headers = {
            "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36"
        }

    def get_url_list(self):
        """
        用于获取所有url的方法
        :return: 一个包含所有url的列表
        """
        # url_list = []
        # for i in range(1000):  # 获取前二百页内容
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i * 50) for i in range(1000)]  # 扁平甚于嵌套

    def parse_url(self,url):
        """
        获取单个url的方法
        :param url:
        :return: response响应数据包
        """
        response = requests.get(url, headers = self.headers)
        return response.content.decode()

    def save_html(self,html_str,page_num):
        """
        保存html数据
        :param html_str:
        :param page_num:
        :return:
        """
        file_path = "{}-第{}页.html".format(self.tieba_name,page_num)  # 其实就是文件名
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(html_str)  # 如“李毅-第一页”

    def run(self):
        """
        主逻辑，调用各方法的代码
        :return:
        """
        url_list = self.get_url_list()  # 通过调用我们定义的get_url_list方法获取所有我们想要的url地址
        for url in url_list:  # 遍历url，请求每个url，获取响应数据
            html_str = self.parse_url(url)  # 调用了是上面的parse_url方法，将url传进去，获取数据
            page_num = url_list.index(url) + 1  # list.index()+1来拿取下一个url地址  页码数
            self.save_html(html_str,page_num)  # 保存获取到的response包，里面有html数据，也有第几页


if __name__ == "__main__":
    tieba_spider = TiebaSpider("李毅")  # 类方法实例化
    tieba_spider.run()