# -*- coding: utf-8 -*-
"""
@author: chengy
"""
from selenium import webdriver
from time import sleep
import traceback
import time, sys
class huoche(object):
    """docstring for huoche"""
    #浏览器驱动
    webdriver=''
    browsr=''
    # 用户名，密码
    username = u"12306用户名"
    passwd = u"12306密码"
    # cookies值得自己去找, 下面两个分别是北京, 洛阳
    starts = u"%u5317%u4EAC%2CBJP"
    ends = u"%u6DF1%u5733%2CSZQ"
    # 时间格式2018-01-19
    dtime = u"2018-01-19"
    # 车次，选择第几趟，0则从上之下依次点击
    order = 0
    ###乘客名
    users = [u"你的名字"]
    ##席位
    xb = u"二等座"
    pz = u"成人票"

    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    login_url = 'https://kyfw.12306.cn/otn/login/init'

    #def __init__(self):
    #    self.browsr = webdriver.Chrome()

    def login(self):
        browsr.get(self.login_url)
        userNameText = browsr.find_element_by_name("loginUserDTO.user_name")
        passWordText = browsr.find_element_by_name("userDTO.password")
        userNameText.send_keys(self.username)
        passWordText.send_keys(self.passwd)
        print("等待验证码，自行输入...")
        while True:
            if browsr.current_url != self.initmy_url:
                sleep(1)
            else:
                break
    def start(self):
        self.login()
        print(browsr.current_url)
        browsr.get(self.ticket_url)
        print(u"购票页面开始...")
        cookie = browsr.get_cookies()
        browsr.add_cookie({'name': '_jc_save_fromStation', 'value': self.starts})
        browsr.add_cookie({'name': '_jc_save_toStation', 'value': self.ends})
        browsr.add_cookie({'name': '_jc_save_fromDate', 'value': self.dtime})
        browsr.refresh()
        print(cookie)
        count = 0
        if self.order != 0:
            while browsr.current_url == self.ticket_url:
                browsr.find_element_by_id("query_ticket").click()
                count += 1
                print(u"循环点击查询... 第 %s 次" % count)
                sleep(10)
                try:
                    browsr.find_elements_by_class_name("btn72")[self.order - 1].click()
                except Exception as e:
                    print(e)
                    print(u"还没开始预订")
                    continue
        else:
            while browsr.current_url == self.ticket_url:
                browsr.find_element_by_id("query_ticket").click()
                count += 1
                print(u"循环点击查询... 第 %s 次" % count)
                if count != 1:
                    sleep(5)
                isClick = 0
                while isClick == 0:
                    try:
                        for i in browsr.find_elements_by_class_name("btn72"):
                            j = browsr.find_elements_by_class_name("btn72").__sizeof__()
                            print("=====j %s" %j)
                            try:
                                print("===可预定元素")
                                # 使得提交按钮可点的重要代码
                                browsr.execute_script("arguments[0].scrollIntoView()", i)
                                i.click()
                                isClick = 1
                                break
                            except Exception as e:
                                print(e)
                                print(u"还没开始预订 %s" % count)
                                continue
                    except Exception as e:
                        print(e)
                        break
                if isClick == 1:
                    print(u"开始预订...")
                    sleep(3)
                    break
        if browsr.current_url == self.buy:
                # sleep(3)
                # self.driver.reload()
                print(u'开始选择用户...')
                browsr.find_elements_by_class_name("check")[0].click()
                print(u"提交订单...")
                sleep(1)
                browsr.find_element_by_id('submitOrder_id').click()
                sleep(1.5)
                print(u"确认选座...")
                browsr.find_element_by_id('qr_submit_id').click()

cities= {'成都':'%u6210%u90FD%2CCDW',
'重庆':'%u91CD%u5E86%2CCQW',
'北京':'%u5317%u4EAC%2CBJP',
'广州':'%u5E7F%u5DDE%2CGZQ',
'杭州':'%u676D%u5DDE%2CHZH',
'宜昌':'%u5B9C%u660C%2CYCN',
'郑州':'%u90D1%u5DDE%2CZZF',
'深圳':'%u6DF1%u5733%2CSZQ',
'西安':'%u897F%u5B89%2CXAY',
'大连':'%u5927%u8FDE%2CDLT',
'武汉':'%u6B66%u6C49%2CWHN',
'上海':'%u4E0A%u6D77%2CSHH',
'南京':'%u5357%u4EAC%2CNJH',
'合肥':'%u5408%u80A5%2CHFH',
'贵阳':'%u8D35%u9633%2CGIW',
'昆明':'%u6606%u660E%2CKMM',
'洛阳':'%u6D1B%u9633%2CLYF'

		 }
if __name__ == '__main__':
    huoche = huoche()
    print("请输入12306登录账号:")
    huoche.username = input()
    print("已填写登录账号为：" + huoche.username)
    print("请输入12306登录密码以明文形式显示:")
    huoche.passwd = input()
    print("已填写登录密码为：" + huoche.passwd)
    print("请输入起始地址:")
    huoche.starts = cities[input()]
    print("已选择起始点为："+huoche.starts)
    print("请输入终点地址:")
    huoche.ends = cities[input()]
    print("已选择终止点为："+huoche.ends)
    print("请输入查询起始时间以YYYY-MM-DD形式:")
    huoche.dtime=input()
    print("已选择查询起始时间为："+huoche.dtime)
    browsr = webdriver.Chrome()
    huoche.start()
