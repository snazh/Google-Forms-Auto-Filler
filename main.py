from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
from timeit import default_timer as timer

if __name__ == '__main__':
    start = timer()
    answers = (
        random.choices(('i5', 'i8', 'i11', 'i14'), weights=(25, 25, 25, 25), k=1),
        random.choices(('i21', 'i24', 'i27', 'i30', 'i33'), weights=(20, 20, 20, 20, 20), k=1),
        random.choices(('i40', 'i43', 'i46', 'i49'), weights=(25, 25, 25, 25), k=1),
        random.choices(('i56', 'i59', 'i62', 'i25'), weights=(25, 25, 25, 25), k=1),
        random.choices(('i72', 'i75', 'i78', 'i81', 'i84'), weights=(20, 20, 20, 20, 20), k=1),
        random.choices(('i91', '94', 'i97', 'i100'), weights=(25, 25, 25, 25), k=1),
        random.choices(('i107', 'i110', 'i113', 'i116'), weights=(25, 25, 25, 25), k=1)
    )

    link = 'https://docs.google.com/forms/d/e/1FAIpQLSfd1iq02LJgHQ6iCO0Wb5VDIMtsVxGXYrkf6ixmJaWRzx9O-A/viewform'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(2)

    for i in range(25):
        for index, el in enumerate(answers, 0):
            browser.find_element(By.ID, *el).click()
        browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
        time.sleep(0.45)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    end = timer()
    print(f'Execution time {end - start}s')
    # execution speed -> 100 answers per 4 minute 6 seconds (approximately)
