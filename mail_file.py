"""
【Python】メール送信をしてみよう！ (添付メール)
PythonのEmailとSmtplibモジュールを利用してメール送信行う方法を確認します。
下記サンプルコードは 添付ファイル の送信をしています。

smtp_mode: normal, starttls, ssl

Blog URL : https://develop.blue/2020/02/python-use-mail/
"""
from email import message
from email.mime import multipart
from email.mime import text
import smtplib
import ssl

smtp_mode = 'normal'
smtp_host = 'メールサーバのホスト名'
smtp_account_id = '送信メールのアカウントID'
smtp_account_pass = '送信メールのアカウントパスワード'

from_mail = '送信メールアドレス'
to_mail = '送り先メールアドレス'

msg = multipart.MIMEMultipart()
msg['Subject'] = 'Email Subject (File Send)'
msg['From'] = from_mail
msg['To'] = to_mail
msg.attach(text.MIMEText('Test File Send', 'plain', 'utf-8'))

# 添付ファイルの設定
with open('添付ファイルパス', 'r') as fp:
    attach_file = text.MIMEText(fp.read(), 'plain')
    attach_file.add_header("Content-Disposition", "attachment", filename='添付ファイル名')
    msg.attach(attach_file)

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
