from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox.service import Service
import smtplib
import time


path = '/your/gecko/driver/path'
service = Service(executable_path=path)
browser = webdriver.Firefox(service=service)
browser.get('https://web.whatsapp.com/')

time.sleep(10)  # waiting for wp to open
browser.find_element_by_xpath('Target Button').click()

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


flag_1 = True
flag_2 = True
flag_3 = False

while True:
    try:
        browser.find_element_by_xpath('Your Online Button').click()  # çevrimiçi bir butondur wpde bu butona ata
        if flag_1:
            message = "Online"
            send_email(message)
            time_flag_start = time.time()
            flag_1 = False
            flag_2 = True
            flag_3 = True

    except NoSuchElementException:
        flag_1 = True
        if flag_2:
            message = "Offline"
            send_email(message)
            if flag_3:
                # noinspection PyUnboundLocalVariable
                time_flag_finish = time.time() - time_flag_start
                send_email(str(time_flag_finish))
                time_flag_start = time.time()
            flag_2 = False
