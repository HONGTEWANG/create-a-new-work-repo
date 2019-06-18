#!/usr/bin/Terence  python
#! -*-coding:utf-8 -*-
# Creattime: 2019/6/18 20:10
#!@Author:Terence
#!@File: zhihu.py

import requests
headers={
    'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'

}
r=requests.get('http://www.zhihu.com/explore',headers=headers)
print(r.text)
