class Student:
    def __init__(self,name,age,subject):
        self.name=name
        self.age=age
        self.subject=subject
    def myfun(self):
        print('welcome all'+self.name)
p1=Student("Vrushali",10,'pe')
p1.myfun()