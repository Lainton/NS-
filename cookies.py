import json
import importlib
import urllib.parse
from selenium import webdriver

class Cookies:
    def __init__(self, driver, cookie_path):
        """
        保存 添加cookie
        driver: 浏览器实例
        """
        self.driver=driver
        self.cookie_path = cookie_path
    

    def parse_cookie(self, cookie_str):
        cookielist = []
        cookie={}
        for item in cookie_str.split(';'):
            itemname=item.split('=')[0].strip()
            itemvalue=item.split('=')[1]
            cookie[itemname]=urllib.parse.unquote(itemvalue)
        cookielist.append(cookie)
        return cookielist

    def save_cookie(self, cookies):
        json_cookies=json.dumps(cookies)
        with open(self.cookie_path,'w') as f:
            f.write(json_cookies)
            print('[+]写入cookie成功')


    def save_driver_cookie(self):
        """
        获取cookies保存到文件
        """
        cookies=self.driver.get_cookies()
        json_cookies=json.dumps(cookies)
        with open(self.cookie_path,'w') as f:
            f.write(json_cookies)


    #读取文件中的cookie
    def read_cookie(self):
        self.driver.delete_all_cookies()
        dict_cookies={}
        with open(self.cookie_path,'r',encoding='utf-8') as f:
            list_cookies=json.loads(f.read())
        for i in list_cookies:
            self.driver.add_cookie(i)

# cookie = Cookies('driver', './cookies.json')
# c = cookie.parse_cookie('t=ad95c74e58e16dd60f90117169644076; cookie2=123986276ca7fbb7c1b16fd5a5cab527; _tb_token_=e747ef3a65ee3; _samesite_flag_=true; thw=cn; cna=FM01FdzysTcCAXPmYm84nWGw; v=0; sgcookie=EthM8y6qoLN5Dg2zcqp5w; uc3=lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dBxd9nV7UbSbmjULo%3D&id2=UUtMHo2Qj7mEcQ%3D%3D&nk2=2XrumlnY%2BEb1kqHC; csg=1ee475e2; lgc=%5Cu9ED1%5Cu591C%5Cu5982%5Cu58A8%5Cu6D53mk; dnk=%5Cu9ED1%5Cu591C%5Cu5982%5Cu58A8%5Cu6D53mk; skt=f5a345137307a7d2; existShop=MTU4NDU5ODcwNw%3D%3D; uc4=id4=0%40U2l2xLRS90X%2BFTtaLN6NbfbYnehv&nk4=0%4025yN9Yu1Otd8ZjS2VWh1%2BHBYZsW%2B4mQ%3D; tracknick=%5Cu9ED1%5Cu591C%5Cu5982%5Cu58A8%5Cu6D53mk; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; tfstk=cMXRB3caWonJLpiIblVcAQshlcUGZzVv8bTipkEfFGEmmUDdiqXGB9b3VhgJHoC..; mt=ci=70_1; enc=Vw1KhCXvRJ9XIY0zKnPebM0tjkPBb3UqqUxkStgnDqwOm1OwYIP%2Bedh1YSFneZQFiBWvdzPTQPdQpTKIGIwjBw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=VT5L2FSpccLuJBreK%2BBd&existShop=false&pas=0&cookie14=UoTUP2Kh9gkljQ%3D%3D&tag=10&lng=zh_CN; l=dBxWUxRRqzn2wrbtBOCGlOocif_OSIRAguzii2mwi_5IJ686Su7OoPOcFFJ6VjWfGXYB45hH9bw9-etbZ7DmndH8sxAJwxDc.; isg=BEVFs9n4t70JfpNC-qditxz7VId_AvmUdvF2GkeqAXyL3mVQD1IJZNM86AIonhFM')
# cookie.save_cookie(c)