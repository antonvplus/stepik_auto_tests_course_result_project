from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "[id=login_form]")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "[id=register_form]")

