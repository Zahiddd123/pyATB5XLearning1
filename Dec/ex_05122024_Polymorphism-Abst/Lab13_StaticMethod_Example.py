class ExcelReader:

    @staticmethod
    def read_from_excel():
         print("Reading from excel")

class MySQLDBConnection:

     @staticmethod
     def readMySqlFile():
         print("Reading MySQL")

class TC1:
     static_var= 19

     def testcase(self):
         MySQLDBConnection.readMySqlFile()
         ExcelReader.read_from_excel()
         print(TC1.static_var)



obj_TC1= TC1()
obj_TC1.testcase()