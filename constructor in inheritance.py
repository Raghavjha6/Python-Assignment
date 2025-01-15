class person:
    def __init__(self, an, nm, db):
        self.ad_no= an
        self.name= nm
        self.dob= db
    def putdata(self):
        print(self.ad_no,self.name,self.dob)
class student(person):
    def __init__(self, inst, roll,ad,n,d):
        person.__init__(self,ad,n,d)
        self.inst= inst
        self.roll= roll
    def display(self):
        print(self.inst, self.roll)
        self.putdata()
s1=student('SIT',1,123,'Raghav','20/12')
s1.display()
s1.putdata()
