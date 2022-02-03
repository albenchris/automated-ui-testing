from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


# =======================================================================================================
def wait_a_few_secs(): sleep(3)


def search_for(item):
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="twotabsearchtextbox"]'))
    )
    element.clear()
    element.send_keys(item)
    element.send_keys(Keys.ENTER)


def fill_in(html_id, text):
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, html_id))
    )
    element.clear()
    element.send_keys(text)
    sleep(0.2)


def click_link(link_text):
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.LINK_TEXT, link_text))
    )
    element.click()


def click_the(html_id):
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, html_id))
    )
    element.click()


def click_element(xpath):
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath))
    )
    element.click()
# ======================================================================================


# Actions start here:
driver.get("https://www.amazon.com")
driver.maximize_window()

try:
    search_for("guardians of the galaxy")
    click_link("Movies & TV")
    click_link("DVD")
    click_the("add-to-cart-button")

    search_for("hitchhikers guide to the galaxy")
    click_link("Movies & TV")
    click_link("DVD")
    click_the("add-to-cart-button")

    # ===== Having difficulty with this for some reason =====
    # search_for("hitchhikers guide to the galaxy book")
    # # click_link("Any Department")
    # # click_link("Books")
    # click_link("The Ultimate Hitchhiker's Guide to the Galaxy: Five Novels in One Outrageous Volume")
    # wait_a_little_longer()
    # click_link("Hardcover")
    # # click_the("Hardcover")
    # # click_element('//span[text()="Hardcover"]')
    # click_the("add-to-cart-button")
    # =======================================================

    click_the("nav-cart")
    click_element('//input[@data-feature-id="proceed-to-checkout-action"]')
    click_link("Create your Amazon account")

    fill_in("ap_customer_name", "Dusty Bunsen")
    fill_in("ap_email", "dbunsen@fakemail.com")
    fill_in("ap_password", "S0Dusty!")
    fill_in("ap_password_check", "S0Dusty!")

    wait_a_few_secs()
    print("TEST PASSED")
except Exception:
    print("TEST FAILED")
    print(Exception)
    driver.quit()
finally:
    driver.close()
