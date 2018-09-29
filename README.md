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



## Golang branch
What I've learned in Golang

### Udemy course: 
[Go the complete developer's guide](https://www.udemy.com/go-the-complete-developers-guide/)

#### Current learning status (45/82)
#### Section progress:
- [x] Section 1: Getting Started
- [x] Section 2: A Simple Start
- [x] Section 3: Deeper into Go
- [ ] Section 4: Organizing Data with Structures
- [ ] Section 5: Maps
- [ ] Section 6: Interfaces
- [ ] Section 7: Channels and Go Routines


