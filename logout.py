import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class gf_login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
       user = "groyce"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://ishma.pythonanywhere.com/")
       time.sleep(2)
       driver.get("http://ishma.pythonanywhere.com/shop/login")
       elem = driver.find_element_by_xpath("//*[@id='id_username']")
       elem.send_keys(user)
       elem = driver.find_element_by_xpath("//*[@id='id_password']")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://ishma.pythonanywhere.com/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='bs-example-navbar-collapse-1']/ul[2]/li[2]/a")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='bs-example-navbar-collapse-1']/ul[2]/li[2]/ul/li[2]/a")
       time.sleep(2)
       driver.get("http://ishma.pythonanywhere.com/logout/")
       time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()
