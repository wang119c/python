# -*- coding: utf-8 -*-
#!/usr/bin/python
# from datetime import time

from selenium import webdriver
from scrapy.selector import Selector
import time
# 自动化测试
# browser = webdriver.Chrome(executable_path="./chromedriver")
# browser.get("https://www.zhihu.com/#signin");
# print()
# text = browser.page_source ;
# title = browser.find_element_by_css_selector('.tb-main-title')
# 模拟淘宝
# t_select  = Selector(text=browser.page_source)
# price = t_select.css('.tb-rmb-num::text').extract()
# 模拟知乎
# browser.find_element_by_css_selector(".view-signin input[name=account]").send_keys('13126858018')
# browser.find_element_by_css_selector(".view-signin input[name=password]").send_keys('wanghui1203')
# browser.find_element_by_css_selector(".view-signin button.sign-button").click()

# 微博模拟登陆
# browser.get("http://weibo.com/")
#
# time.sleep(15)
#
# browser.find_element_by_css_selector('#loginname').send_keys('18810485210')
# browser.find_element_by_css_selector('#pl_login_form input[name=password]').send_keys('wang516898')
# browser.find_element_by_css_selector('.info_list.login_btn .W_btn_a.btn_32px').click()
#
# browser.get('http://weibo.com/dashizhongbiao/home?wvr=5&lf=reg')
# print(browser.page_source)

# 开源中国模拟下拉

# browser.get("https://www.oschina.net/blog")
# for i in range(3):
#     script_str ='''
#     window.scrollTo(0,document.body.scrollHeight);var lenOfPage = document.body.scrollHeight ;return lenOfPage ;
#     '''
#     browser.execute_script(script_str)
#     time.sleep(3)

# 设置chomedriver 不加载图片
# chrome_opt = webdriver.ChromeOptions()
# prefs = {'profile.managed_default_content_settings.images':2}
# chrome_opt.add_experimental_option('prefs',prefs)
# browser = webdriver.Chrome(executable_path="./chromedriver",chrome_options=chrome_opt)
# browser.get("http://www.coart.cn")

# phantomjs,无界面的浏览器 多进程情况下,性能下降
# browser = webdriver.PhantomJS(executable_path="./phantomjs")
# browser.get('https://detail.tmall.com/item.htm?spm=a230r.1.14.3.MgdtPb&id=545918910192&cm_id=140105335569ed55e27b&abbucket=3&sku_properties=10004:653780895;5919063:6536025')
# print(browser.page_source)



#print(price)
# help(browser)
# browser.quit()


