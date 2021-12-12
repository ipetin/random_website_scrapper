#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import random
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys


class Crawler:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--profile-directory=Profile 4");
        options.add_argument("--user-data-dir=C:/Users/iljap/AppData/Local/Google/Chrome/User Data/")
        driver = webdriver.Chrome(chrome_options=options)
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

        response = requests.get(word_site)
        WORDS = response.content.splitlines()
        mnum=1
        
        while True:
            driver.get('https://www.google.com/');
            mnum+=1
            word = random.choice(WORDS)
            word2 = random.choice(WORDS)
            #time.sleep(3) # Let the user actually see something!
            search_bar = driver.find_element_by_name("q")
            search_bar.clear()
            try:
                search_bar.send_keys(str(word).replace("b'","").replace("'","") + " " + str(word2).replace("b'","").replace("'",""))
                search_bar.send_keys(Keys.RETURN)
                result = driver.find_elements_by_xpath('//div[@class="yuRUbf"]/a/h3') 
                random.choice(result).click()
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except:
                pass
            print(driver.current_url)
            time.sleep(5) # Let the user actually see something!
                
        
Crawler()



