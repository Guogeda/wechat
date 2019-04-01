#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/1 14:12
# @Author  : Geda
import  requests
import sys
from xml import etree
import re
reload(sys)
sys.setdefaultencoding('utf-8')

def get_access_token(content):
    list=[]
    url='http://trains.ctrip.com/trainbooking/TrainSchedule/%s/'%content
    html =requests.get(url).content
    html=html.decode('gbk').encode('utf-8')

    reg=r'<tbody>(.*?)</tbody>'
    html=re.findall(reg,html,re.S)
    html=''.join(html)

    reg=r'<tr>(.*?)</tr>'
    html2=re.findall(reg,html,re.S)
    del html2[0]
    for j in html2:
        reg=r'<td>(.*?)</td>'
        html2=re.findall(reg,j,re.S)
        r = r'<a.*?>(.*?)</a>'
        i = re.findall(r, html2[2])[0]
        html2[2]=i
        for  i   in  html2:
            i=i.strip()
            list.append(i)
    return list
def youjian():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr


    my_sender = '1725128685@qq.com'  # 发件人邮箱账号
    my_pass = 'pmmjygodgronbbdb '  # 发件人邮箱密码
    my_user = '2740403857@qq.com'  # 收件人邮箱账号，我这边发送给自己

    try:
        msg = MIMEText('hello word', 'plain', 'utf-8')
        msg['From'] = formataddr(["Fromgeda",my_sender ])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(['', my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "hello word!"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()

        return 1
    except Exception:
        return 0

if __name__ == '__main__':
    # content ='z69'
    # list=get_access_token(content)
    # print list
    # b = [list[i:i + 5] for i in range(0, len(list), 6)]
    # for  i  in  b :
    #     req1 = ' '.join(i)
    #     print req1
    qq='1725128685'
    print (youjian())