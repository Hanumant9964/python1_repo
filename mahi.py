from random import *
alphabets=['hanumant','supriya','suresh','pavan']
digits='0123456789'
city=['Bangalore','Mumbai','Chenai','Hydrabad','Delhi']
designation=['software engineer','senior software engineer','project lead','project mananger']

def get_fake_ename():
	ename=choice(alphabets).upper()
	
	return ename

def get_fake_emn():
	emn=choice('6789')
	for i in range(9):
		emn=emn+choice(digits)
	return emn

def get_fake_ecity():
	ecity=choice(city)
	return ecity
	
def get_fake_esalary():
	esalary=uniform(10000,50000)
	return esalary

def get_fake_eno():
	eno='E-'
	for i in range(4):
		eno=eno+choice(digits)
	return eno

def get_fake_edesignation():
	edesignation=choice(designation).upper()
	return edesignation


def get_fake_edata():

	print(' Employ Name:',get_fake_ename())
	print(' Employ Number:',get_fake_eno())
	print(' Employ Mobile Number:',get_fake_emn())
	print(' Employ City Name:',get_fake_ecity())
	print(' Employ Designation:',get_fake_edesignation())
	print(' Employ Salary:','{:.2f}'.format(get_fake_esalary()))

	
	
for i in range(2):
	get_fake_edata()
	print()


