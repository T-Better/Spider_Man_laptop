import requests


session = requests.session()  # 实例化一个session对象 就像天上的云，拿一块下来

post_url = "https://mail.163.com/"

post_data = {"email":"15132352140@163.com","password":"584120"}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# 使用session发送post请求，请求到之后讲cookie放到保存下来当做我们的内应
session.post(post_url, data = post_data,headers = headers)  # 这个专门就是安插内应的，不用赋值

# 在使用session进行请求登陆之后才能访问地址
r = session.get("https://mail.163.com/js6/s?sid=mCpAlNPVrcLnyqlibcVVOcHfaGbceHii&func=mbox:listMessages")


# 保存页面
with open("151_163mail0202.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())