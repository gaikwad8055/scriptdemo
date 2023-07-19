import time
from pageObject.Loginpage import Login
from pageObject.homepage import home

class Test_login_to_LI:
    baseurl = "https://in.linkedin.com/"
    useremail = "rohitgaikwad9535@gmaol.com"
    userpass = "@abc123"

    def test_linkedin(self,setup):
        self.driver =setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.l = Login(self.driver)
        self.l.enter_email(self.useremail)
        time.sleep(1)
        self.l.enter_pass(self.userpass)
        time.sleep(1)
        self.l.submit()

        self.ho = home(self.driver)
        self.ho.link()






