import mysql.connector

mydb= mysql.connector.connect(host='localhost',user='root',database='car_dealer')

mycursor = mydb.cursor()

class Employee:
    def __init__(self):
        
        self.Emp_ID=input("Enter employeeID:")
        self.Ename=input("Enter name of employee:")
        self.Job_title=input("Enter Job title:")
        self.E_contact=input("Enter contact number:")
        self.E_email=input("Enter email:")
        self.E_addline_1=input("Enter addressline1:")
        self.E_addline_2=input("Enter addressline2:")
        self.E_PAN=input("Enter PAN:")
        self.E_salary=input("Enter salary:")

        sql=("INSERT INTO employees (Emp_ID,Ename,Job_title,E_contact,E_email,E_addline_1,E_addline_2,E_PAN,E_salary)" "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        val=(self.Emp_ID,self.Ename,self.Job_title,self.E_contact,self.E_email,self.E_addline_1,self.E_addline_2,self.E_PAN,self.E_salary)
        
        mycursor.execute(sql,val)
        mydb.commit()

        print("User {} successfully registered.".format(self.Ename))

