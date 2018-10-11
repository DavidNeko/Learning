# 使用Scrapy爬取淘宝商品信息 学习笔记
具体实现过程以及遇到的问题总结

## 步骤1 创建项目

### 1. 确保开发环境安装了scrapy
* 如果未安装，进行安装 `pip install scrapy`

### 2. 在选定的目录中创建scrapy项目

* `scrapy startproject taobao`

### 3. 创建一个名字为`mytaobao`的爬虫

* `scrapy genspider mytaobao taobao.com`
	
	* 之后会在**taobao/spiders**中生成`mytaobao.py`
	
	* 爬虫名字为 mytaobao
	
	* 爬虫允许访问的顶级域名为 taobao.com


## 步骤2 确定所需要的数据项

### 确定爬取信息的需求

* 这个爬虫练习中，我想要的商品信息有：

	* 淘宝店铺名称
	
	* 商品名称
	
	* 商品价格
	
	* 实际成交量（收获量）
	
	* 商品发货地
	
	* 商品详细信息链接
	
### 确定需求后，开始编辑items.py

* item是从scrapy中获取到的结果

* 在`item.py`中加入上述的信息

```
class TaobaoItem(scrapy.Item):
    price = scrapy.Field()
    deals = scrapy.Field()
    title = scrapy.Field()
    shop = scrapy.Field()
    location = scrapy.Field()
    detail_url = scrapy.Field()
    pass
```

### 在`setting.py`中，更改关于item的设置

* 当Item在Spider中被收集之后，它将会被传递到Item Pipeline，一些组件会按照一定的顺序执行对Item的处理。
	
```
ITEM_PIPELINES = {
   'taobao.pipelines.TaobaoPipeline': 300,
} 
```

## 步骤3 分析URL 

### 确定接口
* 抓取淘宝信息其实有很多可用接口，这里使用的是
`https://s.taobao.com/search?q=PS4&sort=sale-desc&s=44`

###分析接口

* q --> 搜索关键字 ：这里使用PS4
	
* sort --> 排序方式 ：这里使用sale-desc，销量降序
	
* s --> 展示商品个数 ： 这里使用44

###分析好接口，将爬虫需要的常量都写在`setting.py`中
```
KEY_WORDS = 'PS4'
PAGE_NUM = 100
COUNT_PER_PAGE = 44 
```

### 编辑爬虫`mytaobao.py`
* `start_request`函数功能是发送请求并或许返回的内容

* `parse`函数功能是解析返回的内容

## 步骤4 用正则表达式解析获取的信息

### 首先分析爬取信息的页面

* `g_page_config`这段**json**包含了我们需要爬取的全部信息

### 在爬虫的`parse`函数中对这段信息进行解析

* 在这里不再赘述正则表达式相关的知识，我们使用了scrapy内置正则解析了获取到的信息


## 步骤5 将数据写入文件存储

### 编辑pipeline过滤结果

* 在`TaobaoPipeline`这个类中，我们对信息进行了存储

**注：这里如果不使用`io.open`会报错，所以引用了`io`**

## 步骤6 运行爬虫

### 记得在`setting.py`中忽略robots协议

* Scrapy爬取网站遵循robots协议，这里我们将它手动关闭

```
ROBOTSTXT_OBEY = False
```

###运行爬虫

```
scrapy crawl mytaobao
```

* 然后就会看到目录中出现了`taobao.json`， 存储了我们刚刚爬取的商品信息

## 遇到的问题：需要使用cookie解决无法爬取信息

在第一遍运行爬虫时，由于未在爬虫里配置cookie，导致了无法爬取商品信息，随后我们又给爬虫添加了cookie配置

### 获取cookie步骤

* 登陆淘宝

* 进入开发者调试工具，选择Network选项卡

* 刷新页面

* 选择Doc子选项卡

* 找到主页的请求和返回情况

* 找到`Request Headers`

* 复制出cookie

### 转化cookie格式

在scrapy中设置cookie需要使用字典格式，但从浏览器复制出的cookie是字符串格式，所以需要进行转化

* `transCookie.py`对cookie进行了格式转化

* 运行`transCookie.py`之后，手动复制转化出的字典

* 将复制的字典放到`setting.py`中的`COOKIE`里

### 给爬虫配置cookie
重新编写一下爬虫文件，配置好cookie

* 在`start_request`函数中，对`scrapy.Request`进行简单更改

```
yield scrapy.Request(url, callback=self.parse, cookies=self.cookie,headers=self.headers, meta=self.meta)
```

* 重新运行爬虫，发现需要登录问题已经解决。

