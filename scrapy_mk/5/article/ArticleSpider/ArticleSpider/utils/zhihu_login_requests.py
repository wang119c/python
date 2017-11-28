# -*- coding: utf-8 -*-
import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re

# 用session获取
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie 加载失败")

headers = {
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36 QQBrowser/3.7.3773.400'
}


def is_login():
    # 通过个人z中心页面返回状态判断是否登录状态
    index_url = "https://www.zhihu.com"
    response = session.get(index_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True


def get_xsrf():
    response = session.get('https://www.zhihu.com', headers=headers)
    # text = '<input type="hidden" name="_xsrf" value="a11de9a21b40d7d7cc9b4111ff9d4fae"/>'
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        return match_obj.group(1)
    else:
        return ''


def get_index():
    response = session.get('https://www.zhihu.com', headers=headers)
    with open('index_page.html', 'wb') as f:
        f.write(response.text.encode('utf-8'))
    print('ok')


def zhihu_login(account, password):
    # 知乎登录
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            '_xsrf': get_xsrf(),
            'password': password,
            'phone_num': account
        }
    else:
        if '@' in account:
            print("邮箱登录")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                '_xsrf': get_xsrf(),
                'password': password,
                'phone_num': account
            }
    response_text = session.post(post_url, data=post_data, headers=headers)
    session.cookies.save()
    # zhihu_login('13126858018', 'wanghui1203')
    # get_index()
