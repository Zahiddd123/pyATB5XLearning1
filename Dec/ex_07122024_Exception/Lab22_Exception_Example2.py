class XYZ:

    def f1(self):
        try:
            a= int(input("Enter a number \n"))
        except Exception as e:
             print("Enter the int only vlue of a")
        else:
            print(a)
        finally:
            print("Finally: Anyhow I will be printed")

obj_xyz= XYZ()
obj_xyz.f1()