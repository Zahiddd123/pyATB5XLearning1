
# If we are able to import any function/ method it is module
from browserPackage.OpenBrowser_Module import  start_browser
from browserPackage.CloseBrowser_Module import stop_browser

# from "packagename.moduleName" import "func/ methodName"

class Testcase:
    def test_case(self):
        start_browser()
        print("hello runing tc ")
        stop_browser()

obj_t= Testcase()
obj_t.test_case()


