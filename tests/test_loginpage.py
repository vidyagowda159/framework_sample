from src.login_page import LoginPage

class TestLoginPage:

    def test_valid_credential(self, init_driver):
        driver = init_driver
        try:
            lp = LoginPage()
            lp.launch_url()
            lp.enter_username("admin")
            lp.enter_password("manager")
            lp.select_checkbox()
            lp.click_login()

        except Exception as msg:
            driver.save_screenshot("screenshot1.png")
            raise msg

