from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_kp_name_by_link(link):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        driver.get(link)

        # Ждем выполнения скрипта и перенаправления
        WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).click()

        # Извлекаем заголовок после выполнения перенаправления
        header = driver.find_element(By.TAG_NAME, 'h1')
        return header.text
    except Exception as e:
        return e


if __name__ == '__main__':
    print(get_kp_name_by_link('https://www.kinopoisk.ru/series/1199686/'))
