class person:
    def getdata(self, ad_no, name, dob):
        self.ad_no= ad_no
        self.name= name
        self.dob= dob
    def putdata(self):
        print(self.ad_no)
        print(self.name)
        print(self.dob)
class student(person):
    def takedata(self, inst, roll):
        self.inst= inst
        self.roll= roll
    def display(self):
        print(self.inst, self.roll)
ob1=person()
ob1.getdata(12,'XYZ','12/12')
ob1.putdata()
ob2=student()
ob2.takedata('SIT',1)
ob2.getdata(10,'ABC','10/10')
ob2.putdata()
ob2.display()
