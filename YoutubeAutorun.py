"""
@Author: Lana, Chen
@Update: May 29th, 2020
@Description: Help your favorite idol to increase the click through rate(CTR) on Youtube!!!

@How to use?
    SETTING:
        |--Part1: Set your url.
        |--Part2: Set your LOOP,VEDIOTIME.
            LOOP for run the vedio(eg.Red Velvet--happiness) how many times;
            VEDIOTIME for how many seconds you want to run the vedio.
            RANDOM_NO for set a random number(minutes)(or Youtube will cut the rate).
    NOTICE:
        Always open your auto-button(upper right side of the page) on Youtube.
        Always open your javascript of your browser.
        It's said that click through rate(CTR) won't increase if your volumn of the computer sound is 
        less than half of it.
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
import time
import random

#Setting:
#Part1: Set your url here!
URL='https://www.youtube.com/watch?v=uR8Mrt1IpXg'
#Part2: Set your LOOP,VEDIOTIME here!
#LOOP for run your vedio(eg.Red Velvet--Psycho) how many times;
#VEDIOTIME for how many seconds you want to run the vedio.
LOOP,VEDIOTIME,RANDOM_NO=10,20,7

for i in range(LOOP):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    try:
        element=driver.find_element_by_xpath("//*[@class='ytp-large-play-button ytp-button']")
        element.click()
        time.sleep(VEDIOTIME+random.randint(0,RANDOM_NO))
    except:
        print("[Exception]======= It will refresh immediately.======")
    driver.close()