from selenium import webdriver
import time
import os
import urllib3
import json

urllib3.disable_warnings()

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DRIVER_PATH = BASE_PATH + '/files/chromedriver'
SAVED_IMAGE_PATH = BASE_PATH + '/daily_weather.png'

TOWN_NUM = '09710104' # 송파구
NAVER_WEATHER_URL = "http://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=" + TOWN_NUM


def save_current_weather_to_image():
    import download_chromedriver
    download_chromedriver.download()

    driver = webdriver.Chrome(DRIVER_PATH)
    driver.set_window_size(605,550)
    driver.get(NAVER_WEATHER_URL)
    driver.execute_script("window.scrollTo(149, 958)")
    time.sleep(1)
    driver.get_screenshot_as_file(SAVED_IMAGE_PATH)

    driver.close()


def notify_to_line():
    LINE_NOTIFY_URL = 'https://notify-api.line.me/api/notify'
    REQUEST_HEADERS = {
        # 'Authorization' : 'Bearer ' + 'bAFVjvYYFfNQUsIMKQO4DBwWIHAciM8Nn3VyPv92xkd'
        'Authorization' : 'Bearer ' + 'TjdWkNh9v3CAN6fCMdcPTNbUihfrC9234miYCf8Sp3T',
    }

    try:
        with open(SAVED_IMAGE_PATH, 'rb') as fp:
            weather_image_binary_data=fp.read()
        http = urllib3.PoolManager()
        response = http.request(
            'POST',
            LINE_NOTIFY_URL,
            headers=REQUEST_HEADERS,
            fields={'message': 'Daily Weather', 'imageFile': ('daily_weather.png', weather_image_binary_data, 'image/png')}
        )
        response_data = json.loads(response.data.decode())
        print('Response HTTP Status Code: {status_code}'.format(status_code=response_data['status']))
        print('Messgae: {message}'.format(message=response_data['message']))
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed.')

            
save_current_weather_to_image()
notify_to_line()
