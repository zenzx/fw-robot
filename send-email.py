import smtplib
from email import header
from email.mime import text
from email.mime import multipart
import os
import json

import data


def sender_mail(html):
    if os.path.exists('./data.json') != True:
        print("您还没有配置您的邮箱\n")
        data.config()
        sender_mail(html=html)
    else:        
        with open("./data.json", encoding='utf-8') as f:
            config_data = json.load(f)
        for receiver in config_data['receivers']:
            msg = multipart.MIMEMultipart()
            msg['From'] = config_data['user']['user_name'] + '<' + config_data['user']['user_email'] + '>'
            msg['To'] = receiver
            msg['subject'] = header.Header('subject', 'utf-8')
            texts = html
            msg.attach(text.MIMEText(texts, 'html', 'utf-8'))
            try:
                smt_p = smtplib.SMTP()
                smt_p.connect(host='smtp.163.com', port=25)
                sender, password = config_data['user']['user_email'], config_data['user']['user_passwd']
                print("正在登录账号")
                smt_p.login(sender, password)
                print("正在发送给 -> " + receiver)
                smt_p.sendmail(sender, receiver, msg.as_string())
            except Exception as e:
                print("发送失败！" + str(e))
                continue
            smt_p.quit() 
            print("发送成功！")

sender_mail("<h1>Hello</h1><p>我叫FW，是Facker的邮件机器人，一个不懂人工智能的智能机器人</p><p>不过嘞，某个人有点懒，名字起的有点随便，作为他老婆，不然。。您来一个</p>")
    