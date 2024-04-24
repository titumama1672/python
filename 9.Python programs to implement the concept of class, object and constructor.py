#9. Python programs to implement the concept of class, object and constructor.

class myClass():
    def method1(self):
        print("Manas")
    def method2(self,someString):
        print("HEY..!:"+ someString)
def main():
    c=myClass()
    c.method1()
    c.method2("Manas")
if __name__=="__main__":
    main()
