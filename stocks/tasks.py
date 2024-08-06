from celery import shared_task
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from stocks.models import Stock


@shared_task
def get_stock_price(stock_name):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(
        options=options,
        service=ChromeService
        (ChromeDriverManager().install())
    )

    url = 'https://www.google.com'

    driver.get(url)

    search_input = driver.find_element(
        By.XPATH,
        '//textarea[@aria-label="Pesquisar"]'
    )
    search_input.send_keys(f'preço da ação {stock_name}')
    search_input.send_keys(Keys.ENTER)

    sleep(2)

    price_div = driver.find_element(
        By.XPATH,
        '//div[@data-attrid="Price"]'
    )
    price = price_div.find_elements(
        By.TAG_NAME,
        'span'
    )[2].text.replace(',', '.')

    driver.quit()

    Stock.objects.create(
        name=stock_name,
        price=float(price)
    )

    return price
