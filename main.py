from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox.service import Service
import smtplib

path = '/your/gecko/driver/path'
service = Service(executable_path=path)
browser = webdriver.Firefox(service=service)
browser.get('https://whatsapp.com')


def send_email(message):
    to = '<YOUR EMAIL>'
    sender = '<WPBOT EMAIL>'
    mail = '<WPBOT EMAIL>'
    password = '<<PASSWORD KEY>>'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail, password)
    server.sendmail(sender, to, message)
    server.quit()


try:
    browser.find_element_by_xpath('Your Button').click()
    browser.refresh()
    print("Find")
except NoSuchElementException:
    print("Not Find")
    message = "Hata"
    send_email(message)
