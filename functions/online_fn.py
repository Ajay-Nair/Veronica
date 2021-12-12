from email.message import EmailMessage
from decouple import config
import pywhatkit
import requests

from pywhatkit import send_mail
def find_my_ip():
    #returns ip address
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def send_email(subject,body,receiver):
    #EMAIL = config("EMAIL")
    #PASSWORD = config("PASSWORD")

    send_mail("veronica.2021.v1@gmail.com","aiwillruletheworld",subject,body,receiver)
