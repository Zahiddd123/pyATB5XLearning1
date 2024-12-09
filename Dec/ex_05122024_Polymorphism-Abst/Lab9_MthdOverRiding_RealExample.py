
class OldBrowser:

    def start_brower(self):
        print(
          "Op browser starting"
        )

    def closing_browser(self):
        print("Op browser closing")

class ChromeBrowse(OldBrowser):

    def start_brower(self): # Overriding parents func here
        super().start_brower() # parent start  browser also called using this method
        print("Chrome browser starting")
    def closing_browser(self):
        print("Chrome browser closing")


obj_C= ChromeBrowse()
obj_C.start_brower()
obj_C.closing_browser()