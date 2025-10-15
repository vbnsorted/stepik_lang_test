import time

from conftest import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/reviews/add/"

def test_button(browser):
    browser.get(link)
    try:
        korzina_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']"))
        )
        time.sleep(30)
    finally:
        assert korzina_button.is_displayed(), "кнопка не найдена"
