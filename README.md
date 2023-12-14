# ctf-notes
白天是码农, 晚上是黑客\
ctf，夺旗笔记, 也算是对于网络攻防的一种理解。。。\
原来,网安中的flag无处不在如斯...\
![Alt text](image.png)
# 网络攻防录
- [x] 11/12【BUU SQL COURSE 1】sql注入, sql
- [ ] 11/13【BUU BRUTE 1】弱密码暴力fuzz, 但还没找到。。。
- [x] 11/15【BUU LFI COURSE 1】本地文件包含漏洞, php
- [x] 11/16【Linux Lab 1】LAMP架构,ssh远程登录
- [ ] 11/26【LFI Labs】这是一个大的专题, 不是很了解呢
- [x] 11/27【Upload-Labs-Linux】【文件上传漏洞】专题, pass01 ([客户端使用js对不合法图片进行检查](https://mp.weixin.qq.com/s?__biz=Mzk0NzMxOTAxMQ==&mid=2247485283&idx=1&sn=92aeb5f9fb2ec066958d9722fc5ca6a5&chksm=c379feeff40e77f9c5133940127f07875f526162bd8ce8a341a592257cd293836d4e56ea15b5&token=1722058134&lang=zh_CN#rd))
- [x] 11/28【Upload-Labbs-Linux】【文件上传漏洞】, Burp intercept and modify mime type to get shell
- [x] 11/30【Upload-Labbs-Linux】【文件上传漏洞】, 还是Burp修改文件类型. 今天参加软件大会志愿者, 老师们真是越老越吃香呀, 羡慕... 
- [x] 12/01【学习】参加ChinaSoft大会, 很不孬, 学者竞争论谷歌学术h指数, llm还真不孬嘞
- [x] 12/04【xss攻击 xss-lab lesson-01】xss攻击是一种前端攻击手段, level1的构造: playboard构造:直接在?name=<script>alert('1');</script> 今天面试若干
- [x] 12/11【wireshark】misc杂项中的题目, 过滤http协议出来, 肉眼找password, ok
- [x] 12/12【二维码】misc杂项中的题目, 发现二维码中隐藏的txt文件, 使用ziprello暴力破解zip文件的二维码
- [x] 12/13【你竟然赶我走】将图片后缀改成txt, 在最后发现隐藏的flag...
- [x] 12/14【乌镇峰会种图】将图片后缀改成txt, 在最后发现隐藏的flag...
- [x] 12/14【N种方法解决】将图片后缀改成txt, 发现base64编码的数据, 浏览器输入保存图片, 扫码得到flag
# 渗透测试资源
- [ ] [渗透测试学习笔记](https://learnku.com/docs/server-learn/1.0)
# 交流点滴
## fuzzing (模糊测试)
- [ ] fuzzing是很tricky的, 经常需要你手工挖到, 然后再去思考如何挖到.
- [ ] 做fuzzing的时候可以补充渗透测试的基础知识, 譬如在buuctf上刷刷ctf的题目

## 行业黑话
- [ ] webshell. Webshell的攻击方式通常是通过利用网站的漏洞或弱点，将Webshell文件上传到目标服务器上。一旦Webshell成功上传并执行，攻击者就可以通过它来执行各种操作，例如查看文件系统、上传和下载文件、执行命令、修改文件权限等。
- [ ] pwn. pwn是网络安全中的俚语, 是own的误写, 意思就是攻方对于目标机器的占有成功

## 武器库
- [ ] qr research, 查看二维码
- [ ] ziperello, 暴力破解zip文件
