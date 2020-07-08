"""
Стандартная библиотека: отправка почты

Смартчас "Знакомство с Python"

Перед использованием необходимо заполнить переменные:
    email_host - адрес почтого сервера
    email_sender - УЗ отправителя
    email_recipient - УЗ получателя

А также создать файл "pwd.txt" и сохранить в нем пароль от УЗ 'email_sender'

"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# настройки
email_host = ''
email_port = 25

email_sender = ''
# открываем файл с паролем и сохраняем пароль
password_file = open("tmp/pwd.txt", "r")
email_sender_password = password_file.read()
password_file.close()

email_recipient = ''
email_subject = 'тестовова тема письма'
email_body = 'тестовый текст'


def send_email():
    """
    Ф-ция для отправки почты
    """
    # создание объекта почты
    msg_root = MIMEMultipart('mixed')
    msg_root['From'] = email_sender
    msg_root['To'] = email_recipient
    msg_root['Subject'] = email_subject
    msg_root.attach(MIMEText(email_body.encode("utf-8"), "html", "utf-8"))

    mail_server = smtplib.SMTP(email_host, email_port)
    mail_server.ehlo()
    mail_server.starttls()  # шифрование подключения
    mail_server.ehlo()
    mail_server.login(email_sender, email_sender_password)  # авторизация
    mail_server.send_message(msg_root)
    print('почта отправлена')
    mail_server.quit()  # не забываем закрыть подключение


if __name__ == '__main__':
    send_email()
