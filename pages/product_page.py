from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):


    def add_to_cart_and_click(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()

    def add_to_cart(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)

    def should_be_product_page(self):
        self.should_be_message_about_add_product()
        #self.should_correct_text_message_about_add_product()
        self.should_correct_name_product_in_basket()
        self.should_be_message_about_basket_price()
        self.should_correct_cost_in_basket()

    def should_be_message_about_add_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_AFTER_ADD_PRODUCT), ("Not message about adding to "
                                                                                         "basket")

    #def should_correct_text_message_about_add_product(self):
        #assert "был добавлен в вашу корзину" in self.browser.find_element(*ProductPageLocators.
                                                                          #MESSAGE_AFTER_ADD_PRODUCT).text, \
            #f"Incorrect text after adding to basket: {self.browser.find_element(*ProductPageLocators.
                                                      #MESSAGE_AFTER_ADD_PRODUCT).text}"

    def should_correct_name_product_in_basket(self):
        assert (self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text ==
                self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADD_PRODUCT_NAME).text), \
            "Incorrect product in basket"

    def should_be_message_about_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST_OF_BASKET), \
            "Not message about cost"

    def should_correct_cost_in_basket(self):
        assert (self.browser.find_element(*ProductPageLocators.PRICE).text ==
                self.browser.find_element(*ProductPageLocators.MESSAGE_COST_OF_BASKET_COST).text), \
            "Incorrect cost in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_AFTER_ADD_PRODUCT)

    def should_not_be_success_message_use_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_AFTER_ADD_PRODUCT)
