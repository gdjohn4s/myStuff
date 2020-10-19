#!/usr/bin/python3

# -- This script will send mail if an specific event start

import smtplib, ssl
from config import *

# Create a secure SSL context
context = ssl.create_default_context()

def get_subject():
    subject = 'TEST MAIL'
    return subject

# - Preparing message to send
def prepare_message():
    # message["Subject"] = 'TEST MAIL'
    message = """
              CIAO
              
              Questo e' un messaggio di prova mandato ad alessio (Adidas)
              """
    return message.encode('utf-8')

message = prepare_message()

# - Creating context with SSL connection
try:
    context = ssl.create_default_context()
except Exception as e2:
    print('Error creating context: \n', e2)

with smtplib.SMTP_SSL(smtp_server, port=port, context=context) as server:
    try:
        server.ehlo()
        if context is not None:
            pass
        else:
            print("Error: Context can't be null")
            server.quit()
            exit 

        # # - Trying to verify RFC822 address
        # try:
        #     mail_from = server.verify(mail_from)
        #     print(mail_from)
        # except Exception as e3:
        #     print("Exception, failed to verify email address: ")
        #     server.quit()
        #     exit

        server.ehlo()
        server.login(mail_from, password)
        server.sendmail(mail_from, mail_to, message)
    except Exception as e:
        print("Exception: ",e)
    finally:
        server.quit()


   
