import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class gf_login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_logi(self):
       user = "groyce"
       pwd = "instructor1a"

       code = "SAVE50"

       firstname = "Pallavi"
       lastname = "Chauhan"
       email = "p1994chauhan@gmail.com"
       address = "South 70th Plaza"
       postal_code = "68106"
       city = "Omaha"
       country = "America"
       mobile = "3213178253"
       quantity = "5"
       quantity2 = "3"
       creditcard = "4111 1111 1111 1111"
       cvv = "123"
       expiration = "12/20"
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
       driver.get("http://ishma.pythonanywhere.com/shop/accounts/profile/")
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/shop/shop/product_list")
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/shop/shop/product_list/business-information-technology/")
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/shop/shop/product_list/textbooks/")
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/shop/shop/product_list/1/django-2-example/")
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_quantity']")
       elem.send_keys(quantity)
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[3]").click()
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/cart/cart/cart_detail/")
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_quantity']")
       elem.send_keys(quantity2)
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[3]/form/input[2]").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_code']")
       elem.send_keys(code)
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/form[1]/input[2]").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/form[2]/input[2]").click()
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/orders/create/")
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_first_name']")
       elem.send_keys(firstname)
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_last_name']")
       elem.send_keys(lastname)
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_email']")
       elem.send_keys(email)
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_address']")
       elem.send_keys(address)
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_postal_code']")
       elem.send_keys(postal_code)
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_city']")
       elem.send_keys(city)
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_country']")
       elem.send_keys()
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='id_mobile']")
       elem.send_keys()
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div/form/p[9]/input").click()
       time.sleep(1)
       assert "Place order"
       time.sleep(1)
       card = '4111111111111111'
       cvv ='123'
       exp = '12/20'
       iframe = driver.find_elements_by_id("braintree-hosted-field-number")[0]
       driver.switch_to.frame(iframe)
       elem = driver.find_element_by_id("credit-card-number")
       elem.send_keys(card)
       time.sleep(1)
       driver.switch_to.default_content()
       iframe = driver.find_elements_by_id("braintree-hosted-field-cvv")[0]
       driver.switch_to.frame(iframe)
       elem = driver.find_element_by_id("cvv")
       elem.send_keys(cvv)
       time.sleep(1)
       driver.switch_to.default_content()
       iframe = driver.find_elements_by_id("braintree-hosted-field-expirationDate")[0]
       driver.switch_to.frame(iframe)
       elem = driver.find_element_by_id("expiration")
       elem.send_keys(exp)
       time.sleep(1)
       driver.switch_to.default_content()
       driver.find_element_by_xpath('//*[@id="payment"]/input[3]').click()
       time.sleep(1)
       driver.get("http://ishma.pythonanywhere.com/payment/done/")
       time.sleep(7)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()
