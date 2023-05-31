from selenium import webdriver
import requests
import ddddocr
import time
import os
import sys
from config.urls import *
from logger import logger


class Engine():
    
    def __init__(self, username: str, password: str, headless: bool = False) -> None:
        
        sys.stdout = open(os.devnull, 'w')
        self.ocr_reader = ddddocr.DdddOcr()
        sys.stdout = sys.__stdout__

        self.session = requests.session()

        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        if headless:    
            option.add_argument('headless')
        self.browser = webdriver.Chrome(options=option)

        self.username = username
        self.password = password

        self.cookies = []
        self.image = ''

    def __get_image(self):
        image_resp = self.session.get(IMAGE_URL)
        if image_resp.status_code == 200:
            self.image = image_resp.content
            print("succeed to get image.")
        else:
            self.image = ''
            print('fail to get image.')
        
    def __save_image(self, path):
        if (self.image == ''):
            print('get an image first')
            return
        with open(path, 'wb') as f:
            f.write(self.image)

    def __get_cookie(self):
        self.session.get(COOKIE_URL, allow_redirects=False)
        cookie = self.session.cookies.get_dict()
        try:
            self.cookies.append(
            {
                'name': 'JSESSIONID',
                'value': cookie['JSESSIONID'],
                'path': '/',
                'httpOnly': True,
                'domain': 'zhjwxk.cic.tsinghua.edu.cn'
            })
            self.cookies.append(
            {
                'name': 'serverid',
                'value': cookie['serverid'],
                'path': '/',
                'httpOnly': True,
                'domain': 'zhjwxk.cic.tsinghua.edu.cn'
            })
        except:
            self.cookies = []
            print('fail to get cookie.')

    def login(self):
        self.__get_cookie()

        data = {
                'j_username': self.username,
                'j_password': self.password,
                'captchaflag': 'login1',
                '_login_image_': '',
            }
        
        img_path = 'image/image.jpg'
        while True:
            self.__get_image()
            if self.image != '':
                self.__save_image(img_path)
                result = self.ocr_reader.classification(self.image)
                data['_login_image_'] = result
                print('OCR result: ', result)
                response = self.session.post(POST_URL, data)
                # successfully sign in the system
                print(response.history)
                location = response.history[0].headers['Location']
                print(location)
                if location == ACCESS_URL:
                    break

    def set_browser_cookie(self):
        self.browser.get(MAIN_URL) # fail to access
        self.browser.delete_all_cookies()
        for i in range(len(self.cookies)):
            self.browser.add_cookie(self.cookies[i])
        print('login cookie:')
        print(self.browser.get_cookies())
        
    def access_mainpage(self):
        self.browser.get(MAIN_URL)
        time.sleep(5)
