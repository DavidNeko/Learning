# -*- coding: utf-8 -*-

class transCookie:
    
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        """
        将从浏览器上拷贝来的cookie字符串转化成scrapy可以用的Dict
        """
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ','')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "Your cookie"
    trans = transCookie(cookie)
    print trans.stringToDict()