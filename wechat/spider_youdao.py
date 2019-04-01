#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 23:21
# @Author  : Geda
import requests

import time
import random
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def get_translate(content):
    content = content.encode('utf-8')
    u = 'fanyideskweb'
    d = content
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = 'rY0D^0\'nM0}g5Mm1z%1G4'

    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
    data={
        'i':content,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':f,
        'sign':sign,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_ENTER',
        'typoResult':'true'
    }
    headers ={
        'Cookie':'JSESSIONID=abcI2g__g6zP0-DKcoo7v; OUTFOX_SEARCH_USER_ID_NCOO=1528835660.8941286; _ntes_nnid=890e0919f1dc16db73a491db33a6320c,1506698356723; SESSION_FROM_COOKIE=fanyiweb; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-1946013977@223.11.95.119; ___rl__test__cookies=1506699306768',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    url ='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.google.com/'



    req = requests.post(url,data=data,headers=headers)
    result=[]
    req=req.json()
    print req
    print type(req)
    if 'smartResult'not in req:
        req = req['translateResult'][0]
        req = req[0]
        req = req['tgt']
        result.append(req)
    else:
        for i in req['smartResult']['entries']:
            result.append(i)
    return result


if __name__ == '__main__':
    #content =raw_input('please input :'  )
    content=u'在线观看 '
    content=get_translate(content)
    req1 = ''.join(content)
    print req1
