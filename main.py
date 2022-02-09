import time

import requests
import random
from sys import argv

from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.common.by import By

_, take_email, take_username = argv


class GetToken:
    register_url = 'https://discord.com/register'
    login_url = 'https://discord.com/login'
    token = None

    def __init__(self, new_email: str, new_username: str):
        self.email = new_email
        self.username = new_username
        self.pas = "".join([str(random.randint(i, 10)) for i in range(10)]) + self.username[::-1]

    def registration(self):
        driver = webdriver.Chrome('/home/scren2010/project/get_token/chromedriver')
        driver.get(self.register_url)
        email = driver.find_element(By.NAME, 'email')
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        btn = driver.find_elements(By.TAG_NAME, 'button')

        email.send_keys(self.email)
        username.send_keys(self.username)
        password.send_keys(self.pas)
        driver.find_element(By.ID, 'react-select-4-input').send_keys('1993')
        driver.find_element(By.ID, 'react-select-2-input').send_keys('15')
        driver.find_element(By.ID, 'react-select-3-input').send_keys('11')
        driver.find_element(By.CLASS_NAME, 'css-dwar6a-menu').click()

        for i in btn:
            if i.get_attribute('type') == 'submit':
                print(i.text)
                # i.click()
        time.sleep(10)

    def login(self):
        r = requests.get(self.login_url, auth=HTTPBasicAuth(username=self.email, password=self.pas))
        if r.status_code == 200:
            self.token = r.request.headers.get('authorization')
        else:
            print('Авторизация прошла не успешно')


s = GetToken(take_email, take_username)
s.registration()
s.login()
print("Ваш токен: ", s.token)



"""
Задание:
написать питон скрипт, который автоматически создает discord аккаунт и логиниться в него получая token авторизации из headers “authorization”
Условия:
- cкрипт должен принимать емейл и никнейм в командной строке
- пароль генерируется автоматически
- подтверждать почту не надо
- должен создаваться аккаунт и возвращать в командную строку token после логина
Ожидаемое 
"""








#
# print(take_email)
# print(take_username)
# register_url = 'https://discord.com/register'
# login_url = 'https://discord.com/login'
#
# pas = "".join([str(random.randint(i, 10)) for i in range(10)]) + take_username[::-1]
# print(pas)
#
# driver = webdriver.Chrome('/home/scren2010/project/get_token/chromedriver')
# driver.get(register_url)
#
# print(driver.title)
#
# email = driver.find_element(By.NAME, 'email')
# username = driver.find_element(By.NAME, 'username')
# password = driver.find_element(By.NAME, 'password')
# btn = driver.find_elements(By.TAG_NAME, 'button')
#
# email.send_keys(take_email)
# username.send_keys(take_username)
# password.send_keys(pas)
# driver.find_element(By.ID, 'react-select-4-input').send_keys('1993')
# driver.find_element(By.ID, 'react-select-2-input').send_keys('15')
# driver.find_element(By.ID, 'react-select-3-input').send_keys('11')
# driver.find_element(By.CLASS_NAME, 'css-dwar6a-menu').click()
#
# for i in btn:
#     if i.get_attribute('type') == 'submit':
#         print(i.text)
#         # i.click()
# time.sleep(20)
# r = requests.get(login_url, auth=HTTPBasicAuth(username=take_email, password=pas))
# print(r.status_code)
# print(r.request.headers.get('authorization'))
#
