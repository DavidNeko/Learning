# Learning
It's the repository of things that I learned...

## Python branch
What I've learned in python

### [Lil-tool] ascii.py

一个可以把图片转换成简单字符画的小工具，转自实验楼

-使用方法
* 安装pillow `sudo pip3 install pillow`
* 下载图片 example.png
* 处理 `python3 ascii.py example.png`

### LeetCode Practice

对LeetCode算法题的练习
* `main.py`中包含了对每题的测试
* 题目内容作为注释写在了py文件里

[Problem_1 TwoSum](https://github.com/DavidNeko/Learning/blob/Python/LeetCodePractice/p_001_TwoSum.py)

[Problem_17 Letter Combinations of a Phone Number](https://github.com/DavidNeko/Learning/blob/Python/LeetCodePractice/p_017_Letter_Combinations_of_a_Phone_Number.py)


### [Mini-Program] Hanabi

Python 模拟烟花的小程序
* under folder /Hanabi run with `python hanabi.py`
* 可以在hanabi.py中更改图片地址，用自己喜欢的图片做背景

![Hanabi_showcase](https://i.makeagif.com/media/9-14-2018/rgKbNS.gif)

### Webscraper learning

#### Selenium

**注：Selenium其实主要的应用不是scraper，而是Webapp的自动化测试
**

* `practice_one.py` **对Selenium基础的了解与练习**
	
	* 创建WebDriver实例，以及其应用
	
	* 使用 Selenium 在google.com输入查询内容并对其进行查询
	
	* 对查询的内容进行处理（这里只用了print）
	
	* 使用 Selenium 在google.com上点击相应按钮（此处点击了下一页）
	
	* 如何查找、使用选定网页元素的XPATH
	
	
* `practice_two.py` **使用Selenium在淘宝抓取选定商品信息**

	* 如何使用`CSS_SELECTOR`选定指定元素
	
	* 如何获得商品信息，并将其保存为字典格式
	
	* 使用`uni_decoder.py`将抓取的商品信息转化成可读csv
	
* 自动填写问卷星上的问卷 **使用Selenium模拟人为操作**

	* 涉及的知识点除了使用`CSS_SELECTOR`选取指定元素以外还有循环处理矩阵类题目的方法
	
	* 还涉及到了使用不同`IP代理`的方法
	
	* 涉及毕业设计，这里不发问卷星答题具体代码，只发布一个大概的框架作为学习笔记
	
	* `ip_scraper.py`是从西刺代理爬取可用IP信息的代码，会将可用IP存储到工作目录中
	
	* `ip_checker.py`是验证爬取IP可用性的代码，读取`ip_scraper.py`存储的IP信息并进行逐步认证

	
#### Scrapy

* taobao文件夹下的内容为**使用Scrapy框架抓取淘宝信息练习**

	* 在`items.py`中写明需要的数据项
	
	* 分析爬取信息所需URL，并在setting中添加相关常量
	
	* 分析网页内容，使用正则表达式解析信息
	
	* 将数据存储到`json`文件中
	
		*练习遇到的问题：需要使用cookie保持登陆状态*
		
	*	具体操作步骤以及实现方法，移步`taobao`文件夹下的[笔记](https://github.com/DavidNeko/Learning/blob/Python/WebScraper/Scrapy_practice/taobao/README.md)




## Golang branch
What I've learned in Golang

### Udemy course: 
[Go the complete developer's guide](https://www.udemy.com/go-the-complete-developers-guide/)

#### Current learning status (96/96)
#### Section progress:
- [x] Section 1: Getting Started
- [x] Section 2: A Simple Start
- [x] Section 3: Deeper into Go
- [x] Section 4: Organizing Data with Structures
- [x] Section 5: Maps
- [x] Section 6: Interfaces
- [x] Section 7: Channels and Go Routines

***

[Web Development w/ Google's Go(golang) Programming language](https://www.udemy.com/go-programming-language/)

#### Current learning status (15/171)
#### Section progress:
- [x] Section 1: Getting Started
- [ ] Section 2: Templates
- [ ] Section 3: Creating your own server
- [ ] Section 4: Understanding net/http package
- [ ] Section 5: Understanding routing
- [ ] Section 6: Serving files
- [ ] Section 7: Deploying your site
- [ ] Section 8: Creating state
- [ ] Section 9: Creating sessions
- [ ] Section 10: Amazon Web Services
- [ ] Section 11: Relational Databases
- [ ] Section 12: Scaling On AWS
- [ ] Section 13: Photo Blog
- [ ] Section 14: Web Dev Toolkit
- [ ] Section 15: Go & Mongodb
- [ ] Section 16: Docker
- [ ] Section 17: PostgreSQL
- [ ] Section 18: MongoDB


### LeetCode practice:

在Golang基础上对LeetCode算法题的练习 

[Problem_1 TwoSum](https://github.com/DavidNeko/Learning/blob/master/Golang/LeetCodePractice/p_001/algorithms/algorithms.go)

[Problem_1 Benchmark](https://github.com/DavidNeko/Learning/blob/master/Golang/LeetCodePractice/p_001/speed_test.go)

***

### Some good resources:

* [build-web-application-with-golang](https://github.com/astaxie/build-web-application-with-golang)

	A golang ebook intro how to build a web with golang. 一个很实用，讲解十分详细的教程。共有11个语言的版本可选择，在[Go语言基础章节](https://github.com/astaxie/build-web-application-with-golang/blob/master/zh/02.0.md)对基础知识的铺垫十分有用。



