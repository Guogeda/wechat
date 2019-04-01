#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/1 6:24
# @Author  : Geda

import  requests
import  re

def get_address(content):
    download_address=[]
    url ='http://www.80s.tw/api_movie/search/%s'%content

    #html=requests.get(url).json()[0]
    html=requests.get(url).content
    print html
    move_id= html['id']
    download_url='http://www.80s.tw/api_movie/movie/%s'%move_id
    download_html = requests.get(download_url).json()
    urls= download_html['formats']['4']['dlurls']
    for i in urls:
        download_address.append( i['url'])
    return download_address

def get_online_watching_url(content):
    start_url='http://www.88ys.tv/index.php?m=vod-search'
    data={
        'wd':content,
        'submit':''
    }
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    html=requests.post(url=start_url,headers=headers,data=data).content

    second_url=r'<li class="p1 m1"><a class="link-hover" href="(.*?)"'
    second_url=re.findall(second_url,html)[0]

    url = 'http://www.88ys.tv'+second_url
    return url
def get_new_url(content):
    new_url='http://www.kuaishantu.com/index.php?m=vod-search'
    data={
        'wd':content
    }
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    html =requests.post(url=new_url,data=data,headers=headers).content
    second_url=r'a class="item-info" href="(.*?)"'
    second_url=re.findall(second_url,html)[0]
    url = 'http://www.kuaishantu.com'+second_url
    return url

if __name__=='__main__':
    content=u'战狼'

    req1 = '\n'.join(get_address(content))
    print req1
    # print (get_online_watching_url('白夜追凶'))
    # get_new_url('白夜追凶')