import mysql.connector

mydb= mysql.connector.connect(host='localhost',user='root',database='car_dealer')

mycursor = mydb.cursor()

import sys

class Customer:
    def create(self):
        self.Cust_name=input("Enter Customer name:")
        self.C_contact=int(input("Enter Contact number of customer:"))
        self.C_PAN=input("Enter PAN of Customer:")
        self.C_address_1=input("Enter Customer's Address line 1:")
        self.C_address_2=input("Enter Customer's Address line 2:")

        sql=("INSERT INTO customers (Cust_name,C_contact,C_PAN,C_address_1,C_address_2)" "values(%s,%s,%s,%s,%s)")
        val=(self.Cust_name,self.C_contact,self.C_PAN,self.C_address_1,self.C_address_2)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\nNew customer {} registered successfully.".format(self.Cust_name))

    def fetch(self):
        c_list=[]
        mycursor.execute("select Cust_name from customers")
        for i in mycursor:
            c_list.append(str(i))

        Cust_name=input("Enter name of Customer:")
        cust="('{}',)".format(Cust_name)

        if cust in c_list:
            k=["Cust_ID", "Cust_name","C_contact","C_PAN","C_address_1","C_address_2"]
            value=[]
            v=[]

            mycursor.execute("SELECT * FROM customers where Cust_name='{}'".format(Cust_name)) 
            for i in mycursor:
                value.append(i)

            a = value[0]
            for i in a:
                v.append(i)

            v_dict=dict(zip(k,v))
            print(v_dict)
            
        else:
            print("Customer does not exist.")
            c=int(input("\nPress 1 to register new customer.\nPress 0 to exit."))
            if c==1:
                c1=Customer()
                c1.create()
            elif c==0:
                sys.exit()
        
