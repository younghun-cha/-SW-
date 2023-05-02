# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:21:56 2022

@author: scw47
"""

# 셀레니움 4.0미만 설치
# 크롬 버젼 브라우저에서 확인
# 구글 드라이버 : https://chromedriver.chromium.org/downloads

import time
from selenium import webdriver

# 구글 크롬 드라이브
url='https://flight.naver.com/'
driver = webdriver.Chrome(r"chromedriver.exe")

try:    
    driver.get(url)
    time.sleep(0.5)
    
    #목적지 설정(프랑스 파리)
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i').click()
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[5]').click()
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[1]').click()
   
    #가는 날짜, 오는 날짜 설정(1월 27일-1월 29일)
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]').click()
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[7]').click()
    time.sleep(0.2)
    
    #검색
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()
    time.sleep(17)
        
    #airplane = 원래 목적지 가장 저렴한 항공 정보
    airplane=driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div[3]/div[1]')

except Exception as e:
    print(e)

finally:
    print(airplane.text) #원래 목적지로 가는 가장 저렴한 항공 정보 출력
    print('\n')
    print('Reservation Complete')