from selenium import webdriver
import time
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DRIVER_PATH = BASE_PATH + '/files/chromedriver'
TOWN_NUM = '09710104' # 송파구
NAVER_WEATHER_URL = "http://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=" + TOWN_NUM
SAVED_IMAGE_PATH = BASE_PATH + '/daily_weather.png'

driver = webdriver.Chrome(DRIVER_PATH)
driver.set_window_size(605,550)
driver.get(NAVER_WEATHER_URL)
driver.execute_script("window.scrollTo(149, 958)")
time.sleep(1)
driver.get_screenshot_as_file(SAVED_IMAGE_PATH)

driver.close()
