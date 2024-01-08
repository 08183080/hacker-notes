# hack-notes
白天是码农, 晚上是黑客, 休闲追柯南
![Alt text](image.png)
# 网络攻防录
# 2023
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
- [x] 12/14【企业参观】今天参观腾讯的腾云大厦, 腾讯确实气势很大呐...
- [x] 12/14【BUU BRUTE】使用Burp Suite定向爆破...
- [x] 12/15【技术分享】看字节无恒实验室的安全技术分享
- [x] 12/15【Upload-Labs-Linux】【文件上传漏洞】, PASS-04, 继续钻黑名单验证的漏洞... 感觉这个单元的漏洞我对于搭建网站很了解的时候才有用...
- [x] 12/16【全球边缘计算大会 上海站】现场聆听, 印象最深这句话: AI三要素: 数据, 算法, 算力. 而所有的数据都产生在边缘(edge)...
- [x] 12/16【柯南大电影 跨龄识别系统】看柯南大电影, 提到的【跨零识别系统】是cv~
- [x] 12/22【当GPT遇到苏轼 方笑一教授】我们也应该学习GPT的虚心接受, 坚决不改的优点(一位 心理学生 如是说)
- [x] 12/23【AI绘画】发现poe平台可以text2image
- [x] 12/23【OSC 开源活动 LLM的基础设施】了解vector db, social了一下, 很不错. 学会 **冥想** 和 **英语**
# 2024
- [x] 1/1【网络爬虫】晚上看完泰勒的巡回演出, 在实验室写爬虫晚上| 优酷视频爬虫, **正则表达式**
- [x] 1/5【华为 计算部门 理科大楼B112 13:00-15:00】可以带着 简历 线下交流
  - [x] 1/5 华为 计算 人员点评我的resume, 可以修改突出学校和实习经历 
- [ ] 1/5【修改resume】将我的resume中2英, 投递red hat, 下周一上午10点面试remote intern
- [ ] 1/5 散步时候在想有时候天意弄人, 得完完全全拥抱自己提升自己, 顺应天命大势
- [ ] 1/6【AppAgent 分享】听cumt校友张弛phd的appagent分享, 很牛逼的, agent可以通过twitter验证码!
  - [ ] 第一直觉, 可以用agent通过web验证码
- [x] 1/6【redhat】投递resume
- [x] 1/7【模仿游戏 电影】晚上宿舍所有灯全部关闭, 看的这部电影, Turing, great and 悲剧性~
- [x] 1/8【社交】结交**爬虫大牛** 谢乾坤, 可以向他请教一二.
- [x] 1/8【RedHat interview】和马来西亚的小姐姐中英混杂面试交流, nice~
- [x] 1/9【最后一天】**今天是最后一天t**, 凌晨爬起来改改代码, 不想睡觉
- [ ] 1/9【courses】完成培训的3门课程
- [ ] 1/11【teams】Security Hackathon for Confidential Containers (https://github.com/confidential-containers)|Go和Rust很牛逼
- [ ] 1/13-1/14【Move 中国开发者大会】| 带老乡吃吃喝喝
- [ ] 1/15【年会】吃吃喝喝
# 渗透测试资源
- [ ] [渗透测试学习笔记](https://learnku.com/docs/server-learn/1.0)
# 交流点滴
## fuzzing (模糊测试)
- [ ] fuzzing是很tricky的, 经常需要你手工挖到, 然后再去思考如何挖到.
- [ ] 做fuzzing的时候可以补充渗透测试的基础知识, 譬如在buuctf上刷刷ctf的题目
- [ ] 理想状态下，例如在可接受的时间范围内，计算资源足够丰富且系统复杂度足够低的情况下，fuzzing就能够给你任何想要的结果。这就好像是让一台计算机去随机的print一些文字，只要时间足够长，随机字符产生的效率足够快，那么早晚有一天会print出一部《三体》出来。

## 行业黑话
- [ ] webshell. webshell的攻击方式通常是通过利用网站的漏洞或弱点，将webshell文件上传到目标服务器上。一旦webshell成功上传并执行，攻击者就可以通过它来执行各种操作，例如查看文件系统、上传和下载文件、执行命令、修改文件权限等。
- [ ] pwn. pwn是网络安全中的俚语, 是own的误写, 意思就是攻方对于目标机器的占有成功
- [ ] admin, 很多很多web系统默认登陆的管理员用户名
- [ ] 木马, 特洛伊木马, 伪装攻入内部, 达到破坏作用
## 武器库 (Tools)
- [ ] Qr research, 查看二维码
- [ ] Ziperello, 暴力破解zip文件
- [ ] Burp Suite, Web应用程序渗透测试和安全评估的集成工具
- [ ] Boofuzz, 模糊测试
- [ ] Peach, 模糊测试
- [ ] IDA， 反汇编和逆向工程
- [ ] ChatGPT, 人类有史以来最伟大的知识QA问答机器人, 现在每个时刻都是跨历史的东西!!!
- [ ] [URL在线编码/解码工具](https://tool.ip138.com/urlencode/)
  - [ ] url编码解码,又叫百分号编码，是统一资源定位(URL)编码方式。URL地址（常说网址）规定了常用地数字，字母可以直接使用，另外一批作为特殊用户字符也可以直接用（/,:@等），剩下的其它所有字符必须通过%xx编码处理。
- [ ] Git, Linus大神写的代码同步和版本管理软件
- [ ] Github, 全球最大同性交友网站
- [ ] VScode, 宇宙最强文本编辑器, 超级丰富的插件生态
- [ ] Linux, 开源操作系统
- [ ] VNC Viewer, 开源的远程控制软件
- [ ] RegExr: 在线正则操练网站 [Learn, Build, & Test RegExr](https://regexr.com/)
- [ ] Vim: vi的增强版, 代码编辑器
- [ ] Notepad++: notepad的增强版, 不错的代码编辑器, 内置的RE搜索模块是Perl写的模块
  - [ ] 查找替换的搜索模块用起来很舒服巴适
  - [ ] 很长的日志试试写入txt文件, notepad就会读截断, 这时候就应该用notepad++打开查看 
- [ ] MacBook Pro: 耳闻可以增强程序员的生产力
- [ ] ChatGPT4 Plus: 好想好想...|我需要找个人拼GPT4
  - [ ] 如何给自己的pc配置成功
  - [ ] 可恶, 我的clash梯子访问openai都被地区限制了。。。 
- [ ] GPT4-V: 图文大模型, 具有很强的图文能力, OCR能力的
- [ ] APPAgent: 基于GPT4-V的app智能操纵agent
## 信息源 (Information Sources)
- [ ] [腾讯安全玄武实验室](https://weibo.com/xuanwulab#_rnd1446180562141)
- [ ] 字节跳动无恒实验室
## 安全思考
- [ ] AI时代, AI伪装, AI产生的数据/文本/图像/视频可能会达到欺骗作用, 如何自动化智能化识别呢?
## 伟大问题
- [ ] 高并发, 高可用, 高性能 (互联网, 三高问题)
- [ ] 网络协议的测试覆盖率低 (软件测试)
- [ ] AI时代如何更好生存 (AI)
## 学习计划
### 2024年1月
- [x] 【第一周】正则表达式
  - [x] 【书籍】【学习正则表达式】
- [ ] 【第二周】【知识点】Python程序的解释运行流程
- [ ] 【第二周】阅读【流畅的Python】(fluent python)
## 程序员道友 (code man)
谦虚向学
### friend
- [ ] zy
- [ ] 阿浩
- [ ] 振宇, share site to read English books: zlibrary
### net friend
- [ ] 谢乾坤, 爬虫大牛, 目前在上海红杉资本
- [ ] 崔庆才, 爬虫大牛, 目前在北京微软
- [ ] 鱼皮, 上海创业
- [ ] 拓跋阿秀, SAP
# code god
- [ ] Ken Thompson: Unix之父, C之父, qed,grep之父, Go之父, 1983图灵奖得主, 去世时黑客们纷纷留言";" (一行指令的结束, R.I.P)
- [ ] Linus: Linux之父, just for fun....
# 程序员创业
## llm时代
- [ ] 斯坦福炒虾机器人: 成本22w, 牛逼
# 先进生产力
- [ ] 【耳机】我需要好用的耳机?
- [ ] 【GPT 4】我需要更好用的GPT
