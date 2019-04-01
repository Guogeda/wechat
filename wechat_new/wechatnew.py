#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/28 15:34
# @Author  : Geda

import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import hashlib
import xmltodict
import time
import sys
from tornado.web import RequestHandler
from tornado.options import options,define
import os

import requests
reload(sys)
sys.setdefaultencoding('utf-8')

WECHAT_TOKEN="guogeda"
NONCE ="1641262349"
MSG_SIGN="002e612f889197719d86a63727d6917a706d5022"
define("port",default=8080,type=int,help="")

def reply(dic_data,content,MsgType):

    resp_data={
                "xml":{
                    "ToUserName":dic_data["xml"]["FromUserName"],
                    "FromUserName":dic_data["xml"]["ToUserName"],
                    "CreateTime":int(time.time()),
                    "MsgType":MsgType ,
                    "Content":content
                }
            }

    return  resp_data

class WechatHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello,geda")
        signature =self.get_argument("signature","")
        print signature
        timestamp =self.get_argument("timestamp","")
        nonce =self.get_argument("nonce","")
        print nonce
        echostr =self.get_argument("echostr","")
        tmp=[WECHAT_TOKEN,timestamp,nonce]
        tmp.sort()
        tmp="".join(tmp)
        real_signature =hashlib.sha1(tmp).hexdigest()
        if signature==real_signature:
            self.write(echostr)
        else:
            self.write_error(403)
    def post(self, *args, **kwargs):
        appid="wx9ca18792c65b0b7f"
        xml_data=self.request.body
        dic_data=xmltodict.parse(xml_data)
        print dic_data
        msg_type =dic_data["xml"]["MsgType"]
        print msg_type
        if msg_type=="text":
            # print (type(dic_data["xml"]["Content"]))
            # url='http://www.tuling123.com/openapi/api'
            # api='c3763c2a1af340969452d53b80fb2392'
            # data={
            #     "Key":api,
            #     "info":dic_data["xml"]["Content"],
            #     "userid":dic_data["xml"]["FromUserName"]
            # }
            # content = requests.post(url=url,data=data).content
            # print content
            content =u"来自机器人的回复"
            self.write(xmltodict.unparse(reply(dic_data,content,msg_type)))

        elif msg_type=="voice":
            content=dic_data["xml"]["Recognition"]
            self.write(xmltodict.unparse(reply(dic_data, content,"text")))

        elif msg_type=="image":
            resp_data = {
                "xml": {
                    "ToUserName": dic_data["xml"]["FromUserName"],
                    "FromUserName": dic_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType":"image",
                    "MediaId": dic_data["xml"]["MediaId"]
                }
            }
            self.write(xmltodict.unparse(resp_data))
        else:
            content=u'好,这里是刷厕所的营养师'
            self.write(xmltodict.unparse(reply(dic_data, content,"text")))

class search(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("templates/helloMarkdown.html")
        query_arg = self.get_body_argument("href")
        print query_arg
class Filename(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("templates/filename.html")

class Dangke(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("templates/dangke.html")
settings = {
    'template_path':'templates',
}
class Download(RequestHandler):
    def initialize(self,filename):
        self.filename=filename
    def get(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=' + self.filename)
        with open(self.filename, 'rb') as f:
            while True:
                data = f.read()
                if not data:
                    break
                self.write(data)
        # 记得有finish哦
        self.finish()
def main():

    tornado.options.parse_command_line()


    app = tornado.web.Application(
        [
            (r"/wechat",WechatHandler),
            (r"/markdown",search),
            (r"/dangke",Dangke),

            (r"/filename/dangke/01.pptx", Download, {"filename": "filename/dangke/01.pptx"}),
            (r"/filename/dangke/02.doc", Download, {"filename": "filename/dangke/02.doc"}),
            (r"/filename/dangke/03.docx", Download, {"filename": "filename/dangke/03.docx"}),
            (r"/filename/dangke/old04.ppt", Download, {"filename": "filename/dangke/old04.ppt"}),

            (r"/filename",Filename),

            (r"/filename/SolidStatePhysics/Chapter1/01.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/01.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter1/02.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/02.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter1/03.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/03.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter1/04.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/04.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter1/05.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/05.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter1/06.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/06.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter1/07.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/07.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter2/01.ppt", Download,{"filename":"filename/SolidStatePhysics/Chapter1/01.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter2/02.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/02.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter2/03.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/03.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter2/04.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/04.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter2/05.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/05.ppt"}),
            (r"/filename/SolidStatePhysics/Chapter2/06.ppt",Download,{"filename":"filename/SolidStatePhysics/Chapter1/06.ppt"}),



            (r"/filename/IntelligentInstrument/01.ppt",Download,{"filename":"filename/IntelligentInstrument/01.ppt"}),
            (r"/filename/IntelligentInstrument/02.ppt",Download,{"filename":"filename/IntelligentInstrument/02.ppt"}),
            (r"/filename/IntelligentInstrument/03.ppt",Download,{"filename":"filename/IntelligentInstrument/03.ppt"}),
            (r"/filename/IntelligentInstrument/04.ppt",Download,{"filename":"filename/IntelligentInstrument/04.ppt"}),
            (r"/filename/IntelligentInstrument/05.ppt",Download,{"filename":"filename/IntelligentInstrument/05.ppt"}),
            (r"/filename/IntelligentInstrument/06.ppt",Download,{"filename":"filename/IntelligentInstrument/06.ppt"}),
            (r"/filename/IntelligentInstrument/07.ppt",Download,{"filename":"filename/IntelligentInstrument/07.ppt"}),
            (r"/filename/IntelligentInstrument/08.ppt",Download,{"filename":"filename/IntelligentInstrument/08.ppt"}),
            (r"/filename/IntelligentInstrument/09.ppt",Download,{"filename":"filename/IntelligentInstrument/09.ppt"}),
            (r"/filename/IntelligentInstrument/10.doc",Download,{"filename":"filename/IntelligentInstrument/10.doc"}),
            (r"/filename/IntelligentInstrument/智能仪器设计基础调课申请.doc",Download,{"filename":"filename/IntelligentInstrument/智能仪器设计基础调课申请.doc"}),

            (r"/filename/LaserPrinciple/01.pptx", Download, {"filename": "filename/LaserPrinciple/01.pptx"}),
            (r"/filename/LaserPrinciple/02.pptx", Download, {"filename": "filename/LaserPrinciple/02.pptx"}),
            (r"/filename/LaserPrinciple/03.pptx", Download, {"filename": "filename/LaserPrinciple/03.pptx"}),
            (r"/filename/LaserPrinciple/04.pptx", Download, {"filename": "filename/LaserPrinciple/04.pptx"}),
            (r"/filename/LaserPrinciple/05.pptx", Download, {"filename": "filename/LaserPrinciple/05.pptx"}),
            (r"/filename/LaserPrinciple/06.pptx", Download, {"filename": "filename/LaserPrinciple/06.pptx"}),
            (r"/filename/LaserPrinciple/07.pptx", Download, {"filename": "filename/LaserPrinciple/07.pptx"}),
            (r"/filename/LaserPrinciple/08.pptx", Download, {"filename": "filename/LaserPrinciple/08.pptx"}),

            (r"/filename/MicrocomputerInterface/01.ppt", Download, {"filename": "filename/IntelligentInstrument/01.ppt"}),

            (r"/filename/PrincipleOfEmbedded/01.pdf", Download, {"filename": "filename/IntelligentInstrument/01.pdf"}),
            (r"/filename/PrincipleOfEmbedded/02.pdf", Download, {"filename": "filename/IntelligentInstrument/02.pdf"}),


        ],
        debug=True
    )
    http_sever = tornado.httpserver.HTTPServer(app)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__=="__main__":
    main()