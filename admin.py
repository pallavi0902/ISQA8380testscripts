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
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/admin/login/?next=/admin/")
       elem = driver.find_element_by_xpath("//*[@id='id_username']")
       elem.send_keys(user)
       elem = driver.find_element_by_xpath("//*[@id='id_password']")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://ishma.pythonanywhere.com/admin/")
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/")
       time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()
