#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 21:04
# @Author  : Geda
import  requests
import xlrd



def get_address():
    address=[]
    longitude=[]
    latitude=[]
    try:
        data = xlrd.open_workbook('addressdate.xlsx')
    except Exception,e:
        print str(e)
    table = data.sheet_by_name(u'Sheet1')
    nrows = table.nrows #hangshu
    for rownum in range(1,nrows):

        row = table.row_values(rownum)
        address.append(row[0])
        longitude.append(row[1])
        latitude.append(row[2])
    return address,longitude,latitude,nrows
def get_mobai_ofo(address,longitude,latitude):

    start_url = 'https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
    headers = {
        'referer': 'https://servicewechat.com/wx80f809371ae33eda/107/page-frame.html',
        'User-Agent': 'MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN',
        'Accept-Encoding': 'gzip',
    }
    data = {
        'longitude': longitude,
        'latitude': latitude,
        'citycode': '0354',
        'wxcode': '013CXPnj1n5dcy0AmZlj1QAHnj1CXPnq',
        'errMsg':'getLocation:ok'
    }
    requests.packages.urllib3.disable_warnings()
    req = requests.post(url=start_url,headers=headers,data=data,verify=False)
    print u'%s的膜拜单车数量：%s'%(address,len(req.json()['object']))


    return str(len(req.json()['object']))


def get_access_token():
    addid = 'wx9ca18792c65b0b7f'
    secret = 'b8fd601227378f3fc2a29e5277826ec7'
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (addid, secret)
    # html = requests.get(url=url)
    # html = html.json()
    # print  html
    access_token='R4xh6fVfmObcEwOP8MvvyBu8txh0VrEksx7nvLkbFr8CgzdfLsB6VUDEtiVA-WbbpvhAt3CyMKCppBJEqZhus1MsPtIsenWN5I62aMG0fhQ1hOL6y-1CznjdsX8wBoS7PQIbAGACDV'
    type='image'
    url ='https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s'%(access_token,type)
    files = {'media': open('test.jpg','rb')}
    req = requests.post(url,files=files)
    print req.json()


if __name__ =='__main__':

    get_access_token()