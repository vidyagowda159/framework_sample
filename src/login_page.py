from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


class LoginPage:

    def launch_url(self):
        driver.get("https://demo.actitime.com/login.do")
        driver.maximize_window()

    def enter_username(self, username):
        driver.find_element("id", "username").send_keys(username)

    def enter_password(self, password):
        driver.find_element("name", "pwd").send_keys(password)

    def select_checkbox(self):
        driver.find_element("name.", "remember").click()

    def click_login(self):
        driver.find_element("xpath", '//div[text()="Login "]').click()
