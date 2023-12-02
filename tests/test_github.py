from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.config import *
import time


# Locators: ID, NAME, LINK_TEXT,

def login(browser):
    # login process
    browser.find_element(By.ID, 'login_field').send_keys(EMAIL)
    browser.find_element(By.ID, 'password').send_keys(PASSWORD)
    browser.find_element(By.NAME, 'commit').click()


def test_create_rep():
    browser = webdriver.Chrome()
    browser.get('https://github.com/login')
    login(browser)
    # repo creation
    browser.get(f'https://github.com/{USERNAME}')
    browser.find_element(By.ID, 'repositories-tab').click()
    time.sleep(1)
    browser.find_element(By.LINK_TEXT, 'New').click()
    time.sleep(1)
    browser.find_element(By.ID, ':r2:').send_keys(REPO)
    browser.find_element(By.NAME, 'Description').send_keys('Sample description')
    browser.find_element(By.ID, ':r6:').click()
    browser.find_element(By.ID, ':r8:').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button').click()
    time.sleep(2)
    # check (optional)
    # rep_name = browser.find_element(By.XPATH, '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a')
    # status = browser.find_element(By.XPATH, '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/span[2]')
    # read_me_file = browser.find_element(By.LINK_TEXT, 'README.md')
    # time.sleep(2)
    # assert rep_name.text == REPO
    # assert status.text == 'Private'
    # assert read_me_file.text == 'README.md'
    # # repo deleting
    browser.get(f'https://github.com/{USERNAME}/{REPO}/settings')
    time.sleep(2)
    browser.find_element(By.ID, 'dialog-show-repo-delete-menu-dialog').click()
    browser.find_element(By.ID, 'repo-delete-proceed-button').click()
    time.sleep(1)
    browser.find_element(By.ID, 'repo-delete-proceed-button').click()
    time.sleep(1)
    browser.find_element(By.ID, 'verification_field').send_keys(f'{USERNAME}/{REPO}')
    time.sleep(1)
    browser.find_element(By.ID, 'repo-delete-proceed-button').click()
    time.sleep(2)

    # checking
    message = browser.find_element(By.XPATH, '//*[@id="js-flash-container"]/div/div/div')
    assert message == f'Your repository "{USERNAME}/{REPO}" was successfully deleted.'
    browser.quit()
