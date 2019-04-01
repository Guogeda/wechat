#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 19:31
# @Author  : Geda
# import requests
#
# url='http://www.tuling123.com/openapi/api'
# api="c3763c2a1af340969452d53b80fb2392"
# data={
#     "key":api,
#     "info":"你好",
#     "userid":"123456"
# }
# content = requests.post(url=url,data=data).json()
# print content["text"]



import os

def get_listdit(filename):
    for path in os.listdir(filename):
        path_dir =os.path.join(filename,path)
        print path_dir
        if os.listdir(path_dir) != None:
            get_listdit(path_dir)


get_listdit("filename")
