"""
【Python】メール送信をしてみよう！
PythonのEmailとSmtplibモジュールを利用してメール送信行う方法を確認します。
下記サンプルコードは smtp_mode にて切り替えできるようにしています。

smtp_mode: normal, starttls, ssl

Blog URL : https://develop.blue/2020/02/python-use-mail/
"""
from email import message
import smtplib
import ssl

smtp_mode = 'normal'
smtp_host = 'メールサーバのホスト名'
smtp_account_id = '送信メールのアカウントID'
smtp_account_pass = '送信メールのアカウントパスワード'

from_mail = '送信メールアドレス'
to_mail = '送り先メールアドレス'

msg = message.EmailMessage()
msg.set_content('Test Text Send');
msg['Subject'] = 'Email Subject'
msg['From'] = from_mail
msg['To'] = to_mail

if smtp_mode == 'starttls':
    server = smtplib.SMTP(smtp_host, 587, timeout=10)
    server.ehlo()
    server.starttls()
    server.ehlo()

elif smtp_mode == 'ssl':
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_host, 465, timeout=10, context=context)

else:
    server = smtplib.SMTP(smtp_host, 25, timeout=10)

server.login(smtp_account_id, smtp_account_pass)
server.send_message(msg)
server.quit()

print('exit')