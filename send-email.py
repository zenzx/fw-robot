import smtplib
from email import header
from email.mime import text
from email.mime import multipart
import os

import data


def sender_mail(html):
    if os.path.exists('./data.json') != True:
        print("您还没有配置您的邮箱\n")
        data.config()
        sender_mail(html=html)
    else:
        # print(html)
        msg = multipart.MIMEMultipart()
        msg['From'] = 'Facker'
        msg['To'] = '**********@**.com'
        msg['subject'] = header.Header('subject', 'utf-8')
        texts = html
        msg.attach(text.MIMEText(texts, 'html', 'utf-8'))
        
        try:
            smt_p = smtplib.SMTP()
            smt_p.connect(host='smtp.***.com', port=25)
            sender, password = '*******@***.com','****************'
            smt_p.login(sender, password)
            smt_p.sendmail(sender, '2362315840@qq.com', msg.as_string())
        except Exception as e:
            print("发送失败！")
        smt_p.quit()
        print("发送成功！")

sender_mail("facker")
    