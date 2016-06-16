# -*- coding: utf-8 -*-
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
import random

# glrh_test@163.com - qwe123

# To : 1601661339@qq.com

# more refer:http://www.liaoxuefeng.com/ +\
# wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000

def _format_addr(s):
    name, addr = parseaddr(s) 
    return formataddr((\
        Header(name, 'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def send_email(subject, content):
    # sender = 'glrh11_test@163.com'
    # sender_password = 'qwe1231'

    sender = 'glrh11@163.com'
    sender_password = 'woshishouquanma1'

    smtp_server = 'smtp.163.com'

    # receivers = ['1601661339@qq.com']
    # receivers = ['1601661339@qq.com', '897335942@qq.com', '405235515@qq.com', '1136462491@qq.com']
    receivers = ['1601661339@qq.com', '405235515@qq.com', '1136462491@qq.com']

    # first : zhengwen 
    
    prefix = u'我们唱着东方红，改革开放站起来！我们唱着春天的故事，改革开放富起来！继往开来的领路人，带领我们走向那新时代，高举旗帜开创未来！'
    subject = u'老王 - ' + u'公司相关文件' + str(random.randint(1, 10000))
    content = prefix + content + prefix

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = _format_addr(u'老王 <%s>' % sender)
    message['To'] = _format_addr(u's-1 <%s>' % ','.join(receivers))
    message['Subject'] = Header(subject, 'utf-8').encode()

    # send 
    server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1)
    server.login(sender, sender_password)
    server.sendmail(sender, receivers, message.as_string())
    server.quit()