import mysql.connector
import sys
from datetime import datetime

mydb= mysql.connector.connect(host='localhost',user='root',database='car_dealer')

mycursor = mydb.cursor()


class Booking:
    def newBooking(self):
        self.Cust_ID=int(input("Enter customer id:"))
        self.Model_code=input("Enter Model_code:")
        self.VIN=input("Enter VIN:")
        self.B_date=datetime.now()
        self.Del_status=input("Enter delivery status:")
        self.emp_id=input("Enter concern employee id:")
        self.payment_mode=input("Enter payment mode:")
        self.Final_veh_price=int(input("Enter booking amount:"))

        sql=("INSERT INTO booking (Cust_ID,Model_code,VIN,B_date,Del_status,emp_id,payment_mode,Final_veh_price)" "values(%s,%s,%s,%s,%s,%s,%s,%s)")
        val=(self.Cust_ID,self.Model_code,self.VIN,self.B_date,self.Del_status,self.emp_id,self.payment_mode,self.Final_veh_price)
        mycursor.execute(sql,val)
        mydb.commit()

        mycursor.execute("SELECT BID FROM booking WHERE VIN='{}'".format(self.VIN))
        myresult=mycursor.fetchone()
        self.BID=myresult[0]
        print("\nNew booking {} done successfully.".format(self.BID))

    def fetch(self):
        b_list=[]
        mycursor.execute("select BID from booking")
        for i in mycursor:
            b_list.append(i)

        BID=int(input("Enter your Booking ID:"))

        if BID in b_list:
            k=["BID", "Cust_ID","Model_code","VIN,B_date","Del_status","emp_id","payment_mode","Final_veh_price"]
            value=[]
            v=[]

            mycursor.execute("SELECT * FROM booking where BID={}".format(BID)) 
            for i in mycursor:
                value.append(i)

            a = value[0]
            for i in a:
                v.append(i)

            b_dict=dict(zip(k,v))
            print(b_dict)
            
        else:
            print("Booking does not exist.")
            c=int(input("\nPress 1 for new booking.\nPress 0 to exit."))
            if c==1:
                b = Booking()
                b.newBooking()
            elif c==0:
                sys.exit()
        


