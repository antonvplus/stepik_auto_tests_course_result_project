from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[id=registration_link]")
    LOGIN_LINK2 = (By.CSS_SELECTOR, "[id=login_link]")

class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "[id=login_form]")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "[id=register_form]")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    MESSAGE_AFTER_ADD_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSAGE_AFTER_ADD_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_COST_OF_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in "
                                               "> div > p:nth-child(1)")
    MESSAGE_COST_OF_BASKET_COST = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in "
                                                    "> div > p:nth-child(1) > strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


