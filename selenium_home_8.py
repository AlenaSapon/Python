import time
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonMainPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_JSONLink(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "//a[@title='More Applications']").click()
        self.assertIn("Applications for Python", driver.page_source)
        self.assertTrue(
            driver.find_element(By.LINK_TEXT, "JSON"))
        elem = driver.find_element(By.LINK_TEXT, "JSON").click()
        self.assertIn("JSON encoder and decoder ", driver.page_source)

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_PythonDocsButton(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        a = ActionChains(driver)
        # identify element
        m = driver.find_element(By.LINK_TEXT, "Documentation")
        # hover over element
        a.move_to_element(m).perform()
        # identify sub menu element
        driver.find_element(By.LINK_TEXT, "Python Docs").click()
        self.assertIn("Welcome! This is the official documentation for Python", driver.page_source)

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_donate(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        driver.find_element(By.XPATH, "//a[@class='donate-button']").click()
        self.assertIn("Donation for the PSF", driver.page_source)
        price5 = driver.find_element(By.XPATH, "//span[contains(text(),'$ 5.00')]")
        price5.click()
        email = "sapon@gmail.com"
        driver.find_element(By.XPATH, "//input[@id='email-5']").send_keys(email)
        driver.find_element(By.XPATH, "//button[@id='_qf_Main_upload-bottom']").click()
        time.sleep(3)
        self.assertIn("$5.00", driver.page_source)
        self.assertIn(email, driver.page_source)

    def tearDown(self):
        self.driver.close()

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_news_dropdown(self):
        driver = self.driver
        driver.get("http://www.python.org")
        elems = driver.find_elements(By.CSS_SELECTOR, '#events ul li a')
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))
        for i in range(len(href_list) - 1):
            # переходим по ссылке
            driver.get(
                href_list[i]
            )
            # получаем строчку хлебных крошек
            elem = driver.find_element(By.CSS_SELECTOR, '.breadcrumbs')
            # проверка наличия в хлебных крошках ссылки на пункт
            self.assertIn("Events", elem.get_attribute("innerHTML"))
            # проверка наличия в хлебных крошках
            # наличия названия текущего пункта
            self.assertIn(
                # название текущего пункта
                name_list[i],
                # строчка хлебных крошек
                elem.get_attribute('innerHTML')
            )
            # ждем 5 секунд
            time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
