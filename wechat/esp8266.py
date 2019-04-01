#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 22:55
# @Author  : Geda

import  requests
import  urllib2
import  urllib

def POST_light():
    print 'hello geda'
    url='http://api.heclouds.com/devices/35433574/datastreams/WD'
    headers={
        'api-key': 'wqgy4xP0a2SWWNrntZrryv3TYz4=',
        'Content-Type': 'application/json'
    }
    data={
        'qos':'1',
        'timeout':'300',
        'type': '1'

    }

    req=requests.get(url,headers=headers).json()
    print req

def conLED(state):

    url='http://api.heclouds.com/cmds?device_id=20547109&qos=1&timeout=300&type=0'
    headers = {
        'api-key': 'IgUN7zpaOZevvNTfXftX7kJBbdc=',
        'Content-Type': 'application/json'
    }
    data={
        'LED':state
    }

    req=requests.post(url,data=data,headers=headers).json()
    return  req

if __name__ == '__main__':
    POST_light()
    #print conLED(0)