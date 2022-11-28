class employ:
    def __init__(self,name,salary,eno,ephonenumber,place,designation):
        self.name=name
        self.salary=salary
        self.eno=eno
        self.ephonenumber=ephonenumber
        self.place=place
        self.designation=designation
    def talk(self):
        print('My Name is :',self.name)
        print('My Salary is:',self.salary)
        print('My Employ Number is:',self.eno)
        print('My Phone Number is:',self.ephonenumber)
        print('My Place is:',self.place)
        print('My Designation is:',self.designation)
        print('\n')

e1=employ('Hanumant',50000,'E-101',9964008625,'Bangalore','Software Enginner')
e2=employ('Ramesh',60000,'E-102',9964008626,'Bangalore','Software Enginner')
e3=employ('Sharath',70000,'E-103',9964008627,'Bangalore','Software Enginner')
e4=employ('Suma',40000,'E-104',9964008628,'Bangalore','Software Enginner')
e5=employ('Shantala',60000,'E-105',9964008629,'Bangalore','Software Enginner')
e1.talk()
e2.talk()
e3.talk()
e4.talk()
e5.talk()