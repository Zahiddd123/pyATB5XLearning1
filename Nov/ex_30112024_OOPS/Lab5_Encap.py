class VolLoginPage:

    def __init__(self, email_arg, pass_arg):
        self.email= email_arg
        self.password= pass_arg

    def login_confirm(self):
        if self.email == "xyz@.com" and self.password == "pass123":
            print("Login pass")
        else:
            print("Login failed")

login_obj= VolLoginPage("xyz@.com1","pass123")
login_obj.login_confirm()