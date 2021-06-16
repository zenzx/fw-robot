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
        try:
            smt_p = smtplib.SMTP(host='smtp.163.com')
            smt_p.connect(host='smtp.163.com', port=25)
            sender, password = config_data['user']['user_email'], config_data['user']['user_passwd']
            print("正在登录账号 -> " + config_data['user']['user_email'])
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
                    msg['subject'] = header.Header('subject', 'utf-8')
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