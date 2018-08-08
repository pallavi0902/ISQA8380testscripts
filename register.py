import unittest
import time
from selenium import webdriver

class gf_login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
       username = "pal"
       firstname = "pallavi"
       lastname = "chauhan"
       email = "p1994@chauhan@gmail.com"
       password = "12345"
       repeat_password = "12345"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://ishma.pythonanywhere.com/")
       time.sleep(2)
       driver.get("http://ishma.pythonanywhere.com/shop/shop/register/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_username']")
       elem.send_keys("pal")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_first_name']")
       elem.send_keys("pallavi")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_last_name']")
       elem.send_keys("chauhan")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_email']")
       elem.send_keys("p1994chauhan@gmail.com")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_password']")
       elem.send_keys("12345")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='id_password2']")
       elem.send_keys("12345")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/form/p[7]/input").click()
       time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()
