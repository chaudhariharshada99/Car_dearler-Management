import mysql.connector
import sys

mydb= mysql.connector.connect(host='localhost',user='root',database='car_dealer')

mycursor = mydb.cursor()

class Vehicle:
    def newEntry(self):
        print("\nEnter details of new model you want to register in vehicle data.\n")
        self.Model_code=input("Enter name of Model:")
        self.Selling_channel=input("Enter its selling channel:")
        self.Veh_price=int(input("Enter its price:"))
        self.stock=int(input("Enter its available stock:"))

        sql=("INSERT INTO vehicle (Model_code,Selling_channel,Veh_price,stock)" "values(%s,%s,%s,%s)")
        val=(self.Model_code,self.Selling_channel,self.Veh_price,self.stock)
        
        mycursor.execute(sql,val)
        mydb.commit()

        print("\nNew Vehicle Model details fed successfully.")
        
    def display(self):
        v_list=[]
        mycursor.execute("select Model_code from vehicle")
        for i in mycursor:
            v_list.append (str(i))
        
        Model_code=input("Enter name of Model Registered with dealer:")
        m="('{}',)".format(Model_code)
        
        if m in v_list:
            k=["Model code" , "Selling channel", "Vehicle price", "Stock available"]
            value=[]
            v=[]

            mycursor.execute("SELECT * FROM vehicle where Model_code='{}'".format(Model_code)) 
            for i in mycursor:
                value.append(i)
    
            a = value[0]
            for i in a:
                v.append(i)

            v_dict=dict(zip(k,v))
            print(v_dict)
            
        else:
            print("Model does not exist.")
            c=int(input("\nPress 1 to register new vehicle model.\nPress 0 to exit."))
            if c==1:
                c1=Vehicle()
                c1.newEntry()
            elif c==0:
                sys.exit()
        

    def vehList(self):
            print("List of available vehicles.")
            mycursor.execute("select Model_code from vehicle")
            for i in mycursor:
                print(str(i))
                
                           
