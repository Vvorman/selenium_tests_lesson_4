from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def solve_quiz_and_get_code(self):
        time.sleep(1)  # Добавляем небольшую задержку
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")
        except NoAlertPresentException:
            print("No alert presented")

    # https://stepik.org/lesson/201964/step/3?unit=176022

    def get_product_name(self):
            product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE)
            return product_name_element.text

    def get_product_price(self):
            product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
            return product_price_element.text



    # def should_be_message_about_adding(self):
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "No message about adding product"
    #     product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
    #     product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text
    #     assert product_name_in_message == product_name_on_page, \
    #         f"Product name in message '{product_name_in_message}' does not match product name on page '{product_name_on_page}'"
    #
    # def should_be_message_basket_total(self):
    #     assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), "No message about basket total"
    #     basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
    #     product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    #     assert product_price in basket_total_message, \
    #         f"Basket total '{basket_total_message}' does not contain product price '{product_price}'"

# https://stepik.org/lesson/201964/step/3?unit=176022

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "No message about adding product"
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        product_name_on_page = self.get_product_name()
        assert product_name_in_message == product_name_on_page, \
            f"Product name in message '{product_name_in_message}' does not match product name on page '{product_name_on_page}'"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), "No message about basket total"
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        product_price = self.get_product_price()
        assert product_price in basket_total_message, \
            f"Basket total '{basket_total_message}' does not contain product price '{product_price}'"

    # Метод should_be_product_price можно оставить без изменений, так как он проверяет наличие элемента
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "No product price element"



    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared"


    def should_be_success_message_disappeared(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.invisibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE))
        except TimeoutException:
            assert False, "Success message is still present, but should have disappeared"