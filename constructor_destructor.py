class account:
    def __init__(self,ac_no,bal):
        self.ac_no=ac_no
        self.bal=bal
    def display(self):
        print(self.ac_no)
        print(self.bal)
    def __del__(self):
        print("Destructor called.")
ac1=account(1,1000)
ac1.display()
ac2=account(2,5000)
ac2.display()
del ac1
del ac2
