# coding=utf-8


import unittest
import traceback
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException ,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import pyperclip
import xlrd,xlwt
import xlsxwriter
import traceback
import requests
import json
import time
import pymysql
import re
from retrying import retry




chrome_options = Options()


chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9400")
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9400 --user-data-dir="~/ChromeProfile"  这个也可以
#Google\ Chrome --remote-debugging-port=9300 --user-data-dir="~/ChromeProfile"  这个也可以
# chrome.exe - -remote - debugging - port = 9229 - -user - data - dir = "C:\selenum\AutomationProfile"

chrome_driver = "/usr/local/bin/chromedriver"  #  \u 报错，\\u mac 路径
#chrome_driver = "/Applications/Google\ Chrome.app/Contents/MacOS/chromedriver"  #  \u 报错，\\u


driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

driver.maximize_window()
driver.refresh()
time.sleep(2)










class BaiduTestCase(unittest.TestCase):
    def setUp(self):
        # print('爹爹我要开始删除了哈 ',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        # url = 'https://pan.baidu.com/'
        self.driver = driver  # 选择谷歌浏览器
        # self.driver.get(url)  # 打开页面
        # # contexts = self.driver.current_window_handle  # 获取当前句柄
        # # print(contexts), type(contexts)
        # time.sleep(2)
        #self.driver.maximize_window()  # 浏览器全屏显示

    @retry(stop_max_attempt_number=20, wait_fixed=8000)
    def test_bubutton(self): # 必须以test开头 setup teardown 这些才执行
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("0110fenzhi shangma ")



        # 如果不用actionchains 就单击运行两次也能点击


        # contexts = self.driver.current_window_handle  # 获取当前句柄
        # print(contexts)
        # file_test = xlrd.open_workbook(r'/Users/lisanqingduck/Documents/zhufanayiduck/zhufanayipython/neirong.xlsx')  # 读取test1.xlsx文件
        # count = len(file_test.sheets())  # 获取该文件中的工作簿数
        # print("工作簿总数为：", count)
        # table1 = file_test.sheet_by_name("Sheet1")  # 根据工作簿名字获取该工作簿的数据
        #
        # nrows = table1.nrows  # 获取工作簿行数
        # ncols = table1.ncols  # 获取工作簿列数
        # print("Sheet1的行数为：", nrows, "列数为：", ncols)
        # table1.write(nrows+1, 4, 'head')
        self.conn = pymysql.connect(
            host='',
            port=3306,
            user='',
            passwd='',
            db='',
            charset='utf8')

        #data = ("小鱼", 20, "W")
        cursor = self.conn.cursor()

        #e = cursor.execute('SELECT id FROM users order by id asc ;')
        #f = cursor.fetchall()  # 获取所有记录
        # print(cursor)
        # print(e)
        h=0
        henduo = self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd')
        # henduo = self.driver.find_elements_by_xpath('//dd[contains(@_cmd_installed,"1")]/following-sibling::dd')
        # henduo = self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd')
        # henduoclickspan = self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd/child::span')
        a = len(henduo)
        datalianjie = []
        dataname=[]
        # WebDriverWait(self.driver, 5).until(
        #     lambda x: x.find_element_by_xpath('//*[@id="layoutMain"]/div[2]/div[2]/div/ul[1]/li[1]/div/span[3]'))
        #
        # quxuan = self.driver.find_element_by_xpath(
        #     '//*[@id="layoutMain"]/div[2]/div[2]/div/ul[1]/li[1]/div/span[3]')
        #
        # quxuan.click()  # 2009热闹 -42
        while h <=a-2:
            time.sleep(1.5)
            # for i  in henduoclickspan:
            f = self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd/child::div/child::div/child::a')[1 +h]
            m = f.get_attribute('text')
            # print(m,'是什么')
            wenben = ["我的资源","打算要看的180925","更新不易谢谢帮助，顺手帮助谢谢","w-x-in ，xiao-cheng-xu每日同步更新；搜（dengdaideche）自取更方便i","留言帮找资源看这里","后续记录每周累积三次未点，拉黑处理，直接失效"
                      ,"来自：iPad","我的应用数据","搜集全网网盘 若这里没有 其他地方也不会有","点击进来看在线教程","apps(1)",'w-x-in ，xiao-cheng-xu搜索（窝认输）','自用款vpn首次注册送免费时长好用就买，进来自取地址']


            if  m in wenben:
                h=h+1
                # print(h,'h的值')
                # f1 = self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd/child::div/child::div/child::a')[1 + h]
                # m1 = f1.get_attribute('text')
                # if m1 in wenben:
                #     h =h+1
                #
                # else:
                #     pass

            else:
                # pass


                time.sleep(0.8)
                self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd/child::span')[1+h].click()
                time.sleep(2)
                # i.click()

                WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath('//a[contains(@data-button-id,"b53")]'))
                fenxiang=self.driver.find_element_by_xpath('//a[contains(@data-button-id,"b53")]')
                fenxiang.click()
                time.sleep(2)
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath('//span[contains(text(),"创建链接")]'))
                self.driver.find_element_by_xpath('//span[contains(text(),"创建链接")]').click()
                time.sleep(2)
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath('//span[contains(text(),"复制链接及提取码")]'))
                self.driver.find_element_by_xpath('//span[contains(text(),"复制链接及提取码")]').click()
                time.sleep(2)
                print(pyperclip.paste()[0:70],'复制的链接啊')

                datalianjie.append(pyperclip.paste()[0:70])



                time.sleep(1.5)
                self.driver.find_element_by_xpath('//*[@id="dialog1"]/div[1]/div/span').click()
                time.sleep(0.8)
                self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd/child::span')[1+h].click()
                h = h + 1
                # before = self.driver.page_source 
                # self.driver.swipe(0.5 * x, 6 / 7 * y, 0.5 * x, 2 / 7 * y,1000) 
                # after = self.driver.page_source 
                # if before == after:  




                henduo =self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd')
        a =len(henduo)
        i=  self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd')[0]
        n = 0  # 2009热闹 -42
        while n <a-2:

            f= self.driver.find_elements_by_xpath('//dd[contains(@_installed,"1")]/following-sibling::dd/child::div/child::div/child::a')[1+n]
            h1 = f.get_attribute('text')
            wenben = ["我的资源","打算要看的180925","更新不易谢谢帮助，顺手帮助谢谢","w-x-in ，xiao-cheng-xu每日同步更新；搜（dengdaideche）自取更方便i","留言帮找资源看这里","后续记录每周累积三次未点，拉黑处理，直接失效"
                      ,"来自：iPad","我的应用数据","搜集全网网盘 若这里没有 其他地方也不会有","点击进来看在线教程","apps(1)",'自用款vpn首次注册送免费时长好用就买，进来自取地址','w-x-in ，xiao-cheng-xu搜索（窝认输）']
            if h1 in wenben:
               n = n + 1

            else:

                dataname.append(h1+'(度)')
                print(h1)
                n=n+1
        heqilailianjiename = dict(zip(dataname, datalianjie))
        print(heqilailianjiename)
        # cursor.execute("insert into SHuju(lianjie) values('%s')" % (datalianjie))
        for cc in heqilailianjiename:

            cursor.execute("insert into SHuju (wenjian,lianjie,mima) values('%s','%s','1')" % (cc,heqilailianjiename[cc]))
            # cur.execute("insert into b values('%d','%s')" % (i, d[i]))

            self.conn.commit()













    def tearDown(self):
        print('复制好了我的宝贝', time.strftime("%Y%m%d %H:%M:%S", time.localtime()))
        #print('我复制好了呢爹爹。')
        kw = {'appid': '',
              "secret": ""}
        r = requests.get("", params=kw, )
        # print( r.text, '登录以后拿到具体')
        # print(r.json()["data"]["access_token"])# 获取响应报文
        tokena = r.json()["data"]["access_token"]
        print(tokena, '拿到的token')
        self.url = ''

        self.headers = {"Content-Type": "application/json",
                        "token": tokena}
        timea = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        self.data = {
            # "ats": {
            #     "15563": ["lijiaye"]
            # },
            "msg": "饭煮熟了" + timea,
            "receiver_ids": [""],
            "receiver_type": "person",
            "sender_id": ""
        }

        r = requests.post(url=self.url, json=self.data, headers=self.headers)  # 发送请求

        # self.driver.quit()  # 退出浏览器


if __name__ == '__main__':
    unittest.main()
