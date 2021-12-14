from email.message import EmailMessage
from decouple import config
from pywhatkit import send_mail , sendwhatmsg_instantly,sendwhatmsg
import requests
def find_my_ip():
    #returns ip address
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def send_email(subject,body,receiver):
    #EMAIL = config("EMAIL")
    #PASSWORD = config("PASSWORD")

    send_mail("veronica.2021.v1@gmail.com","aiwillruletheworld",subject,body,receiver)

def whatsapp(number,msg):
    sendwhatmsg_instantly(number,msg,20,True,5)


