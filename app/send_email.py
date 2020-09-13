import smtplib
import config


def send_email():
    gmail_user = config.GMAIL_USER
    gmail_password = config.GMAIL_PSW

    sent_from = gmail_user
    to = config.TO_ADDRESSES
    subject = 'Alguien prendio la loooooz!'
    body = 'Cuerpo del mail'

    email_text = "Alarma activada"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        raise('Something went wrong...')

