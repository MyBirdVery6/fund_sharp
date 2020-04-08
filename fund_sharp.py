#-*- coding:utf-8 -*-

import os, sys
import traceback
import json
import bs4
from selenium import webdriver

'''
https://www.jianshu.com/p/4b89c92ff9b4
https://cuiqingcai.com/2577.html
'''
    
driver = webdriver.PhantomJS(executable_path = "./bin/phantomjs.exe")

def func_load_webpage(code):
    if not code.isdigit() or len(code) != 6:
        return False
    base_url = 'https://qieman.com/funds/%s' % code
    
    dict_select = {
        'scale': '',        # 最新规模
        'withdrawal': '',   # 最大回撤
        'sharp': '',        # 夏普比率
        'volatility': '',   # 波动率
        'code': code,       # 基金代码
    }
    
    driver.get(base_url)
    
    content = driver.page_source.encode('utf8')

    target = ''
    soup = bs4.BeautifulSoup(content, "html.parser")
    for co in soup.find_all('span'):
        if target != '':
            dict_select[target] = co.text.encode('utf8')
            if target == 'volatility':
                break
            target = ''
    
        if co.text == u'最新规模':
            target = 'scale'
        elif co.text == u'最大回撤':
            target = 'withdrawal'
        elif co.text == u'夏普比率':
            target = 'sharp'
        elif co.text == u'波动率':
            target = 'volatility'

    return json.dumps(dict_select)
    
if __name__ == "__main__":
    code = '110027'
    if len(sys.argv) > 1:
        code = sys.argv[1]
    print func_load_webpage(code)





