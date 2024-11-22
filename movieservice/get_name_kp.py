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
    chrome_options.add_argument("--disable-dev-shm-usage")  # Уменьшение использования памяти
    chrome_options.add_argument("--no-sandbox")  # Запуск без песочницы
    chrome_options.add_argument("--disable-gpu")  # Отключение GPU (не нужно в headless)
    chrome_options.add_argument("--remote-debugging-port=9222")  # Устранение ошибки DevToolsActivePort
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        driver.get(link)

        # Ждем выполнения скрипта и перенаправления
        (WebDriverWait(driver, 600)
         .until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[itemprop="name"]'))).click())

        # Извлекаем заголовок после выполнения перенаправления
        header = driver.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]')
        return header.text
    except Exception as e:
        return e


if __name__ == '__main__':
    print(get_kp_name_by_link('https://www.kinopoisk.ru/series/1199686/'))
