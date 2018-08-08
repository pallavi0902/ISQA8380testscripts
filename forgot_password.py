import unittest
import time
from selenium import webdriver

class gf_login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
       user = "groyce"
       pwd = "instructor1a"
       email = "p1994@chauhan@gmail.com"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://ishma.pythonanywhere.com/")
       time.sleep(2)
       driver.get("http://ishma.pythonanywhere.com/shop/login")
       time.sleep(2)
       driver.get("http://ishma.pythonanywhere.com/password_reset/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_email']")
       elem.send_keys(email)
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/form/p[2]/input")
       time.sleep(2)
       driver.get("http://ishma.pythonanywhere.com/password_reset/done/")

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()
