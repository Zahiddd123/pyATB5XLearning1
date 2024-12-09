from dotenv import load_dotenv
import os


class VolLoginPage:

    def __init__(self, email_arg, pass_arg):
        self.email= email_arg
        self.password= pass_arg

    def login_confirm(self):
        if self.email == "xyz@.com" and self.password == "pass123":
            print("Login pass")
        else:
            print("Login failed")
load_dotenv()   # use to read the data from environment file
email= os.getenv("EMAIL")
password= os.getenv("PASSWORD")
print(email, password)


login_obj= VolLoginPage(email, password)
login_obj.login_confirm()