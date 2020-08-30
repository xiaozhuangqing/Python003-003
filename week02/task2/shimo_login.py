import time
import requests
from fake_useragent import UserAgent
from selenium import webdriver


def login_request():
    ua = UserAgent(verify_ssl=False)
    headers = {
        'User-Agent' : ua.random,
        'Referer' : 'https://shimo.im/login?from=home'
    }

    s = requests.Session()

    login_url = 'https://shimo.im/lizard-api/auth/password/login'

    form_data = {
        'mobile':'187',
        'password':'xi'
    }

    response = s.post(login_url,data=form_data,headers=headers,cookies=s.cookies)
    print(response.cookies)

    visit_url = 'https://shimo.im/docs/6hdP3PYJJ8PHJDTX'
    content=s.get(visit_url,headers=headers, cookies=s.cookies)
    print(content.text)

def login_seleium():
    try:
        browser = webdriver.Chrome()

        browser.get('https://shimo.im/login?from=home')
        time.sleep(1)

        browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('187')
        browser.find_element_by_xpath('//*[@name="password"]').send_keys('xi')

        time.sleep(1)
        browser.find_element_by_xpath('//button[contains(@class,"sm-button submit")]').click()

        cookies = browser.get_cookies()
        print(cookies)
        time.sleep(3)

    except Exception as e:
        print(e)
    finally:
        browser.close()

def __name__ == "__main__":
    # login_request()
    login_seleium()