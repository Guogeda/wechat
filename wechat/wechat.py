#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/25 15:28
# @Author  : Geda
from flask import  Flask
from flask import request
from xml.etree import  ElementTree as ET
from flask import render_template
import requests
import mobai
import sys
import spider_youdao
import spider_80s
import define_menu
import json


reload(sys)
sys.setdefaultencoding('utf-8')
define_auto_replay={
    'question':u'你是谁',
    'replay':u'我是疙瘩'
}
def get_mobai_detail():
    address = (mobai.get_address()[0])
    longitudes = (mobai.get_address()[1])
    latitudes = (mobai.get_address()[2])
    all_detail = []
    for i in range(0, mobai.get_address()[3] - 1):
        address1 = address[i].encode('utf-8')
        all_detail.append(str(address1))
        all_detail.append(mobai.get_mobai_ofo(address[i], longitudes[i], latitudes[i]))
    return all_detail

app = Flask(__name__)
def get_access_token():
    addid='wx9ca18792c65b0b7f'
    secret='b8fd601227378f3fc2a29e5277826ec7'
    url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(addid,secret)
    html=requests.get(url=url)
    html=html.json()['access_token']
    return html

@app.route('/',methods=['GET','POST'])
def index():
    if request.method =='GET':
        echostr = request.args.get('msg')
        return  echostr
    else:


        data=request.get_data()
        xml= ET.fromstring(data)
        ToUserName = xml.findtext('.//ToUserName')
        FromUserName = xml.findtext('.//FromUserName')
        CreateTime = xml.findtext('.//CreateTime')
        MsgType = xml.findtext('.//MsgType')
        Content = xml.findtext('.//Content')
        MsgId = xml.findtext('.//MsgId')
        Msg = xml.findtext('.//msg')


        if Content[0]=='t':
            transe_content=Content[1:]
            transe_content = spider_youdao.get_translate(transe_content)
            req1 = ''.join(transe_content)
            return render_template(
                "index.html",
                ToUserName=ToUserName,
                FromUserName=FromUserName,
                CreateTime=CreateTime,
                Content=req1,
            )
        else:
            if Content[0]=='m':
                movie_name=Content[1:]
                movie_download=spider_80s.get_address(movie_name)
                req1 = '\n'.join(movie_download)
                #req1=get_access_token()
                return render_template(
                    "index.html",
                    ToUserName=ToUserName,
                    FromUserName=FromUserName,
                    CreateTime=CreateTime,
                    Content=req1,
                )
            elif Content[0]=='o':
                movie_name = Content[1:]
                movie_download = spider_80s.get_online_watching_url(movie_name)

                return render_template(
                    "index.html",
                    ToUserName=ToUserName,
                    FromUserName=FromUserName,
                    CreateTime=CreateTime,
                    Content=movie_download,
                )
            elif Content[0]=='O':
                movie_name = Content[1:]
                movie_download = spider_80s.get_new_url(movie_name)

                return render_template(
                    "index.html",
                    ToUserName=ToUserName,
                    FromUserName=FromUserName,
                    CreateTime=CreateTime,
                    Content=movie_download,
                )
            elif Content[0] == 'c':
                choochoo = Content[1:]
                movie_download =define_menu.get_access_token(choochoo)
                req1 = '\n'.join(movie_download)
                return render_template(
                    "index.html",
                    ToUserName=ToUserName,
                    FromUserName=FromUserName,
                    CreateTime=CreateTime,
                    Content=req1,
                )
            elif 'dht' in Content:
                req=Dht11.values()
                req ='humudity:%s\ntempetature:%s'%(req[0],req[1])
                return render_template(
                    "index.html",
                    ToUserName=ToUserName,
                    FromUserName=FromUserName,
                    CreateTime=CreateTime,
                    Content=req,
                )
            elif '开灯' in Content:
                import esp8266
                req=esp8266.conLED(1)
                return render_template(
                    "index.html",
                    ToUserName=ToUserName,
                    FromUserName=FromUserName,
                    CreateTime=CreateTime,
                    Content=req,
                )
            elif '关灯' in Content:
                import esp8266
                req=esp8266.conLED(0)
                return render_template(
                    "index.html",
                    ToUserName=ToUserName,
                    FromUserName=FromUserName,
                    CreateTime=CreateTime,
                    Content=req,
                )
            elif Content[0] == 'q':
                choochoo = Content[1:]
                #define_menu.youjian(choochoo)

                result=define_menu.youjian(choochoo)
                return render_template(
                    "index.html",
                    ToUserName=ToUserName,
                    FromUserName=FromUserName,
                    CreateTime=CreateTime,
                    Content=result,
                )
            else:
                if u'课程表' in Content:

                    return render_template(
                        "kebiao.html",
                        ToUserName=ToUserName,
                        FromUserName=FromUserName,
                        CreateTime=CreateTime,
                        MediaId='9g4GsPZfe9C6d4Li8WJSJXISejLiFmjhNMsjvZSuhsjObfOHUnG8ikSiPSYCElVE',
                    )
                if u'你是谁' in Content:
                    return render_template(
                        "index.html",
                        ToUserName=ToUserName,
                        FromUserName=FromUserName,
                        CreateTime=CreateTime,

                        Content=u'我是疙瘩',
                    )
                if u'雨辰是变态' in Content:
                    return render_template(
                        "index.html",
                        ToUserName=ToUserName,
                        FromUserName=FromUserName,
                        CreateTime=CreateTime,
                        Content=u'你说的对',
                    )
                if u'膜拜查询' in Content:
                    req = get_mobai_detail()
                    req1 = ','.join(req)
                    return render_template(
                        "index.html",
                        ToUserName=ToUserName,
                        FromUserName=FromUserName,
                        CreateTime=CreateTime,
                        Content=req1,
                    )

                robot_key='65b523924f2be324c9912ea52fdcf235'
                robot_url='http://op.juhe.cn/robot/index?info=%s&key=%s'%(Content,robot_key)
                req =requests.get(robot_url)

                req2= req.json()['reason']
                if req2=='次数不足（达到数量限制100）':
                    return render_template(
                        "index.html",
                        ToUserName=ToUserName,
                        FromUserName=FromUserName,
                        CreateTime=CreateTime,
                        Content=u'你的机器人睡觉了，冲钱可以让他醒来',
                    )
                else:
                    req3 = req.json()['result']['text']
                    return render_template(
                        "index.html",
                        ToUserName=ToUserName,
                        FromUserName=FromUserName,
                        CreateTime=CreateTime,
                        Content=req3,
                    )
    return 'OK'
# @app.route('/esp8266',methods=['GET','POST'])
# def esp8266():
#     return render_template('esp8266.html')
#     if request.method =='GET':
#         echostr = request.args.get('msg')
#         return  echostr
#
#     if request.method =='POST':
#         data = request.get_data()
#         data= json.loads(data)
#         print data['msg']
#         if data['msg']['ds_id']=='humudity':
#             Dht11['humudity']=data['msg']['value']
#
#         if data['msg']['ds_id']=='temperature':
#             Dht11['tempetature']=data['msg']['value']
#
#         print  Dht11

if __name__ == '__main__':
    Dht11={

    }
    app.run(debug=True,port=8080)