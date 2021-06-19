import smtplib
from email import header
from email.mime import text
from email.mime import multipart
import os
import re
import json

import data


def detect():
    if os.path.exists('./data.json') != True:
        print("您还没有配置您的邮箱\n")
        data.config()
    else:        
        with open("./data.json", encoding='utf-8') as f:
            config_data = json.load(f)
        host = re.findall('@(.*)\.com', config_data['user']['user_email'])
        if host == "qq":
            host = 'smtp.qq.com'
            port = 25
        elif host == "163":
            host = 'smtp.163.com'
            port = 25
        elif host == "gmail":
            host = 'smtp.gmail.com'
            port = 587
        else:
            print("请选择你要使用的邮箱系统，目前支持QQ邮箱，网易邮箱，谷歌邮箱。")
            print("请重新配置你的文件")
            data.config()
            detect()
    return host, port


def sender_mail(html):
    host, port = detect()
    with open("./data.json", encoding='utf-8') as f:
        config_data = json.load(f)
    try:
        smt_p = smtplib.SMTP(host)
        smt_p.connect(host, port)
        sender, password = config_data['user']['user_email'], config_data['user']['user_passwd']
        print("正在登录账号 -> " + config_data['user']['user_email'])
        if host == "gmail":
            smt_p.ehlo()
            smt_p.starttls()
            smt_p.ehlo()
        smt_p.login(sender, password)
        print("登录成功！")
        for receiver in config_data['receivers']:
            try:
                msg = multipart.MIMEMultipart()
                msg['From'] = config_data['user']['user_name'] + '<' + config_data['user']['user_email'] + '>'
                msg['To'] = receiver
                msg['subject'] = header.Header('FwRobot😆的早安问候', 'utf-8')
                texts = html
                msg.attach(text.MIMEText(texts, 'html', 'utf-8'))
                print("正在发送给 -> " + receiver)
                smt_p.sendmail(sender, receiver, msg.as_string())
            except Exception as e:
                print("发送失败：" +str(e))
                continue
    except Exception as e:
        print("报错：" + str(e))
    smt_p.quit() 
    print("发送成功！")