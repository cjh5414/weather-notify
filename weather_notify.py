from selenium import webdriver
import time
import os
import urllib3

urllib3.disable_warnings()

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DRIVER_PATH = BASE_PATH + '/files/chromedriver'
TOWN_NUM = '09710104' # 송파구
NAVER_WEATHER_URL = "http://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=" + TOWN_NUM
SAVED_IMAGE_PATH = BASE_PATH + '/daily_weather.png'

LINE_NOTIFY_URL = 'https://notify-api.line.me/api/notify'
REQUEST_HEADERS = {
    # 'Authorization' : 'Bearer ' + 'bAFVjvYYFfNQUsIMKQO4DBwWIHAciM8Nn3VyPv92xkd'
    'Authorization' : 'Bearer ' + 'TjdWkNh9v3CAN6fCMdcPTNbUihfrC9234miYCf8Sp3T'
}
# REQUEST_DATA = {'message': 'test', 'imageFile': SAVED_IMAGE_PATH}
REQUEST_DATA = {'message': 'test', 'imageFile': '@/Users/jihun/Projects/weather-notify/test.png'}

print(REQUEST_DATA)
print(type(REQUEST_DATA))

driver = webdriver.Chrome(DRIVER_PATH)
driver.set_window_size(605,550)
driver.get(NAVER_WEATHER_URL)
driver.execute_script("window.scrollTo(149, 958)")
time.sleep(1)
driver.get_screenshot_as_file(SAVED_IMAGE_PATH)

driver.close()



def notify_to_line():
    try:
        http = urllib3.PoolManager()
        response = http.request(
            'POST',
            LINE_NOTIFY_URL,
            headers=REQUEST_HEADERS,
            fields=REQUEST_DATA
        )
        print('Response HTTP Status Code: {status_code}'.format(
        status_code=response.status))
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed.')

notify_to_line()
