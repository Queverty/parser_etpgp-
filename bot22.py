from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import sys
from contextlib import redirect_stdout
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from subprocess import call

def parsing():
    #Список покупных Proxy
    PROXY = ['####','####']
    lk = random.choice(PROXY)
    ua = UserAgent()
    #Настройки webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument(f"user-agent={ua.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--proxy-server=%s' % lk)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    
    wait = WebDriverWait(driver, 120)
    stealth(driver,
        languages=["ru-RU", "ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    
    #Заход на сайт
    driver.get('https://etpgp.rzd.ru/#orders/new/start')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-top-suggestions-wrapper.js-suggestions-wrapper > div > div > div.js-shell-suggestions > div > div:nth-child(1)')))
    driver.find_element(By.CSS_SELECTOR,"body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-top-suggestions-wrapper.js-suggestions-wrapper > div > div > div.shell-favorite-title.js-favorite-title.shell-favorite-title-closing").click()    
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-top-middle.js-shell-top-data > div.shell-top-area-top > div.js-shell-route-manager > div.shell-route-block > div > div:nth-child(1) > div.shell-route-input > input')))
    #Выбор станций
    citi_1 = 'CITY_1'
    citi_2 = 'CITY_2'
    for i in citi_1:
        driver.find_element(By.CSS_SELECTOR,"body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-top-middle.js-shell-top-data > div.shell-top-area-top > div.js-shell-route-manager > div.shell-route-block > div > div:nth-child(1) > div.shell-route-input > input").send_keys(i)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-top-suggestions-wrapper.js-suggestions-wrapper > div > div > div.js-shell-suggestions > div > div > span").click()
    print('Откуда: '+driver.find_element(By.CSS_SELECTOR,'body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-top-middle.js-shell-top-data > div.shell-top-area-top > div.js-shell-route-manager > div.shell-route-block > div > div:nth-child(1) > div.shell-route-input > div').get_attribute("innerHTML"))
    for j in citi_2:
        driver.find_element(By.CSS_SELECTOR,"body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-top-middle.js-shell-top-data > div.shell-top-area-top > div.js-shell-route-manager > div.shell-route-block > div > div:nth-child(2) > div.shell-route-input > input").send_keys(j)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-top-suggestions-wrapper.js-suggestions-wrapper > div > div > div.js-shell-suggestions > div > div > span").click()
    print('Куда: '+driver.find_element(By.CSS_SELECTOR,'body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-top-middle.js-shell-top-data > div.shell-top-area-top > div.js-shell-route-manager > div.shell-route-block > div > div:nth-child(2) > div.shell-route-input > div').get_attribute("innerHTML"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#goods > div.page-header-container > div > div > div')))
    #Код груза
    driver.find_element(By.CSS_SELECTOR,'#goods > div.page-search-container > div > div > div > input').send_keys("####")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#cargoes-list-container > div')))
    print('Груз: ' + driver.find_element(By.CSS_SELECTOR, '#cargoes-list-container > div > div').get_attribute("title"))
    print('Код: ' + driver.find_element(By.CSS_SELECTOR,'#cargoes-list-container > div > div > div.cargo-item-code').get_attribute("innerHTML"))
    driver.find_element(By.CSS_SELECTOR,'#cargoes-list-container > div').click()
    #Вес груза
    driver.find_element(By.CSS_SELECTOR, '#goods > div.supplier-modal-container > div > div > div > div.cargo-edit-menu-inputs > div > input').send_keys("####")
    driver.find_element(By.CSS_SELECTOR,"#goods > div.supplier-modal-container > div > div > div > div.cargo-edit-menu-input-with-margin > div > div > div > div.css-1hwfws3.account-payers-company__value-container").click()
    #Упаковка
    time.sleep(2)
    driver.find_element(By.ID, "react-select-2-option-2").click()
    try:
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#goods > div.supplier-modal-container > div > div > div > div:nth-child(4) > div.cargo-edit-menu-input-with-margin > div > input").send_keys("50")
        print('Объем:50м3')
    except Exception as _ex:
        print('Объем:0')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"#goods > div.supplier-modal-container > div > div > div > div.supplier-add-service-btns.orf-button-with-margin-top > button.supplier-add-point-btn.supplier-add-point-btn-submit").click()
    driver.find_element(By.CSS_SELECTOR,'#goods > div.container > div:nth-child(2) > div > button').click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-data-carriage.js-shell-carriage > div.container > div > div:nth-child(4)')))
    driver.find_element(By.CSS_SELECTOR,'body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-data-carriage.js-shell-carriage > div.container > div > div:nth-child(5)').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-sign-in-btn.js-side-panel-btn").click()
    #Ввод данных от аккаунта
    driver.find_element(By.CSS_SELECTOR,"#side-panel > div > div > div > div.side-panel-upper-part > div > div.side-panel-pages-container > div > div.side-panel-page.side-panel-page-signin > div.side-panel-submit-form.side-panel-form-signin > form > div:nth-child(1) > input").click()
    driver.find_element(By.CSS_SELECTOR,"#side-panel > div > div > div > div.side-panel-upper-part > div > div.side-panel-pages-container > div > div.side-panel-page.side-panel-page-signin > div.side-panel-submit-form.side-panel-form-signin > form > div:nth-child(1) > input").send_keys("@mail.ru")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#side-panel > div > div > div > div.side-panel-upper-part > div > div.side-panel-pages-container > div > div.side-panel-page.side-panel-page-signin > div.side-panel-submit-form.side-panel-form-signin > form > div:nth-child(2) > input").click()
    driver.find_element(By.CSS_SELECTOR,"#side-panel > div > div > div > div.side-panel-upper-part > div > div.side-panel-pages-container > div > div.side-panel-page.side-panel-page-signin > div.side-panel-submit-form.side-panel-form-signin > form > div:nth-child(2) > input").send_keys("PASSWORD")
    driver.find_element(By.CSS_SELECTOR,"#side-panel > div > div > div > div.side-panel-upper-part > div > div.side-panel-pages-container > div > div.side-panel-page.side-panel-page-signin > div.side-panel-submit-form.side-panel-form-signin > div > input").click()
    time.sleep(10)
    try:
        driver.find_element(By.CSS_SELECTOR,'#side-panel > div > div.modal-window-container.modal-window-container-visible.modal-window-confirm > div > div.modal-window-message.custom-message > div > button').click()
    except Exception as _ex:
        pass
    time.sleep(3)
    print ('Вес: ' + driver.find_element(By.CSS_SELECTOR,'body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-top-middle.js-shell-top-data > div.shell-top-area-bottom > div.shell-nav-goods-list.js-shell-selected-goods-list > div > span').get_attribute("innerHTML"))
    print ('Тип вагона: полувагон')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-data-carriage.js-shell-carriage > div.container > div.floating-bottom-buttons-container > button')))  
    try:
        driver.find_element(By.CSS_SELECTOR,'body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-data-carriage.js-shell-carriage > div.container > div.floating-bottom-buttons-container > button').click()
    except Exception as _ex:
        print("Аккаунт заблокирован")
        return
    time.sleep(10)
    #Количество вагонов для планировки
    vg=25
    for nedel in range(3,10):
        for day in range(8): 
            try:
                s1 = driver.find_element(By.CSS_SELECTOR,
                                         f"body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-data-arrival.js-shell-arrival > div.container > div > table > tbody > tr:nth-child({nedel}) > td:nth-child({day}) > a").get_attribute(
                    "class")
                if s1 == "cal-day":
                    driver.find_element(By.CSS_SELECTOR,
                                        f"body > div.shell-data.side-panel-offset-respectful.js-shell-data > div.shell-data-arrival.js-shell-arrival > div.container > div > table > tbody > tr:nth-child({nedel}) > td:nth-child({day})").click()
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                 "#preorder-finish > div > div.order-form-block-big-bottom-margin > div.order-form-tariff-group")))
                    time.sleep(15)
                    print('Дата:' + ' ' + driver.find_element(By.CSS_SELECTOR,
                                                              'body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-top-middle.js-shell-top-data > div.shell-top-area-bottom > div.shell-nav-button.nav-icon-button.nav-btn-selected-date.js-arrival-date').get_attribute(
                        "innerHTML"))
                    try:
                        s = (driver.find_element(By.CSS_SELECTOR,
                                                 '#preorder-finish > div > div.order-form-block-big-bottom-margin > div.preorder-recalc-container > button').get_attribute(
                            "innerHTML"))
                        if s == "ОБНОВИТЬ ДАННЫЕ" or "Обновить данные":
                            print('Обновить данные доступно')
                            #Оформление вагонов, если доступна планировка
                            time.sleep(4)
                            driver.find_element(By.CSS_SELECTOR,"#preorder-finish > div > div.order-form-block-big-bottom-margin > div.preorder-recalc-container > button").click()
                            time.sleep(20)
                            driver.find_element(By.CSS_SELECTOR,'#preorder-finish > div > div.order-form-block-big-bottom-margin > div:nth-child(4) > label > div.order-form-tariff-name > div').click()
                            time.sleep(20)
                            driver.find_element(By.CSS_SELECTOR,'#preorder-finish > div > div.order-form-block-big-bottom-margin > div:nth-child(4) > div > div.order-form-block-service.order-form-block-service-for-btn.shipment-cal > button.shell-button.order-form-submit-button.js-submit-btn').click()
                            time.sleep(60)
                            print("Вагон оформлен")
                            jj='вагон оформлен'
                            with open('test8.txt','a') as f:
                                f.write(f'{jj}\n')
                            time.sleep(15)                    
                            driver.find_element(By.CSS_SELECTOR,"#order-info > div > div.order-form.falsefalse > div.order-payment-section > div.order-form-block.orf-buttons > button:nth-child(7)").click()
                            time.sleep(15)
                            with open('test8.txt','r') as f:
                                y = len(f.readlines())
                            print(f'{y} вагон из {vg}')
                            if y == vg:
                                return
                    except Exception as _ex:
                        print('нет вагонов')
                    try:
                        driver.find_element(By.CSS_SELECTOR,
                                            "body > div.shell-most-top.side-panel-offset-respectful.js-header-full > div.shell-top > div.shell-top-data > div.shell-top-middle.js-shell-top-data > div.shell-top-area-bottom > div.shell-nav-button.nav-icon-button.nav-btn-selected-date.js-arrival-date").click()
                    except Exception as _ex:
                        pass
                    print('_____________________')
            except Exception as _ex:
                pass
            time.sleep(5)
    driver.close()

def send_telegram():
    
    #Вызов парсер и запись в файл
    with open('file_name1.txt', 'w') as f:
        with redirect_stdout(f):
            parsing()
            
    #Отправление результата в ТГ
    with open('file_name1.txt', 'r') as f:
        file = f.read()

    #api token telegram чата
    api_token = 'token'
    word = 'Обновить данные доступно'
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
            chat_id='@####',
            text=file
        ))



def main():
    send_telegram()


if __name__ == "__main__":
    main()
