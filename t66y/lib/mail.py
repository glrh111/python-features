# -*- coding: utf-8 -*-
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr
from email.header import Header
import random
import re

import os

# glrh_test@163.com - qwe123

# To : 1601661339@qq.com

# more refer:http://www.liaoxuefeng.com/ +\
# wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000

# define base infos
sender = 'glrh11@163.com'
sender_password = 'woshishouquanma1'

smtp_server = 'smtp.163.com'

# receivers = ['1601661339@qq.com']
# receivers = ['1601661339@qq.com', '897335942@qq.com', '405235515@qq.com', '1136462491@qq.com']
receivers = ['1601661339@qq.com', '405235515@qq.com', '1136462491@qq.com', '1015134111@qq.com']

# first : zhengwen 

prefix = u'我们唱着东方红，改革开放站起来！我们唱着春天的故事，改革开放富起来！继往开来的领路人，带领我们走向那新时代，高举旗帜开创未来！'
subject = u'老王 - ' + u'公司相关文件' + str(random.randint(1, 10000))



def _format_addr(s):
    name, addr = parseaddr(s) 
    return formataddr((\
        Header(name, 'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))



def send_email(subject, content):
    # sender = 'glrh11_test@163.com'
    # sender_password = 'qwe1231'
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

def send_mail_with_file(content, args):
    r_content = '<html><body>' + u'<h1>嘿嘿哈哈</h1>'
    # message obj
    msg = MIMEMultipart()
    msg['From'] = _format_addr(u'小王 <%s>' % sender)
    msg['To'] = _format_addr(u'嘿嘿嘿 <%s>' % ','.join(receivers))
    msg['Subject'] = Header(u'老王准备嘿嘿嘿了', 'utf-8').encode()

 
    # add add_ons
    for idx, img in enumerate(args):
        try:
            with open('img/%s' % img, 'rb') as f:
                filename=str(idx)+'.jpg'
                # set MIME and filename
                # there is a keng
                mime = MIMEBase('image', 'jpg', filename=filename)
                # add header info 
                mime.add_header('Content-Disposition', 'attachment', filename=filename)
                mime.add_header('Content-ID', '<%s>' % idx)
                mime.add_header('X-Attachment-ID', str(idx))
                # add file content
                mime.set_payload(f.read())
                # base64 encode
                encoders.encode_base64(mime)
                # attach with msg
                msg.attach(mime)
                r_content += '<p><img src="cid:%s"></p>' % idx
        except:
            # raise
            continue

    # replace \n with <br /> in content
    # pattern = re.compile('\n')
    content = re.sub(r'\n', '<br />', content)

    r_content = prefix + content + prefix + '</body></html>'
    # content text
    msg.attach(MIMEText(r_content, 'html', 'utf-8'))


    # send 
    server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1)
    server.login(sender, sender_password)
    server.sendmail(sender, receivers, msg.as_string())
    server.quit()
