import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import vehicle
import login
import employee as emp
import customer as cust
import booking as bk

mydb= mysql.connector.connect(host='localhost',user='root',database='car_dealer')

mycursor = mydb.cursor()

COUNT=0
while COUNT<3:
    if True:
        print("\n\n========================================================================================")
        print("\n              1.Press 1 for Booking new vehicle or to check booking details of previous one.")
        print("              2.Press 2 for Vehicle section.")
        print("              3.Press 3 for customer section.")
        print("              4.Press 4 for Employee details or to register New Employee.")
        print("              5.Press 5 for Sales Report.")
        print("              6.Press 6 to exit.")
     
        print("\n\n========================================================================================")
        print()
        c=int(input("Enter your choice:"))
        print()

    #Booking:    
        if c==1:
            print("\n========================================================================================")
            b = bk.Booking()
            option=int(input("           Select 1 for new booking \n          2 for getting previous booking details:"))
            if option==1:
                try:
                    b.newBooking()
                except mysql.connector.errors.IntegrityError as  msg:
                    print("\nBooking Failed.\tCustomer Id must be registered with us.\n")
                    print(msg)
                finally:
                    choice=int(input("Press 1 for registering new customer.\nPress 0 for exit."))
                    if choice==1:
                        c1 = cust.Customer()
                        c1.create()
                    else:
                        sys.exit()
            elif option==2:
                b.fetch()
            else:
                print("Incorrect input given.")

    #Vehicle:  
        elif c==2:
            print("\n\n========================================================================================")
            print("                             Welcome to Vehicle section.")
            v=vehicle.Vehicle()
            v.vehList()
            c4=int(input("Select 1 for registering new model to database.\nSelect 2 for fetching details of existing models."))

            if c4==1:
                v.newEntry()
            elif c4==2:
                v.display()
            else:
                 print("Incorrect input given.")
                

    #Customer:  
        elif c==3:
            print("\n\n========================================================================================")
            print("                             Welcome to Customer section.")
            c = cust.Customer()
            c2=int(input("Select 1 for registering new customer.\nSelect 2 for fetching details of existing customer.\n"))
            if c2==1:
                c.create()
            elif c2==2:
                c.fetch()
            else:
                print("Incorrect input.")
    #Employee:     
        elif c==4:
            print("\n\n========================================================================================")
            print("                                 Welcome to Employee section.")
            c3=int(input("Select 1 for registering new employee.\nSelect 2 for fetching details of existing employee.\n"))
            
            if c3==1:
                e = emp.Employee()
                
            elif c3==2:                       
                e_list=[]
                mycursor.execute("select Ename from employees")
                for i in mycursor:
                    e_list.append(str(i))

                N=input("Enter your registered name:")
                n="('{}',)".format(N)
                if n in e_list:
                    k=["Emp_ID","Ename","Job_title","E_contact","E_email","E_addline_1","E_addline_2","E_PAN","E_salary"]
                    value=[]
                    v=[]
                    
                    mycursor.execute("SELECT * FROM employees where Ename='{}'".format(N)) 
                    for i in mycursor:
                        value.append(i)

                    a=value[0]
                    for i in a:
                        v.append(i)

                    e_dict=dict(zip(k,v))
                    print(e_dict)

                else:
                    print("Incorrect input")

#Reports
        elif c==5:
            
            sr=int(input("Press (1) for Model-wise Sales Report.\nPress (2) for Month-wise Sales Report.\nPress (3) for Sales Target Report of Employees.\n"))
            
            if sr==1:                                         
                Brand=[]
                mycursor.execute("select Model_code from booking group by Model_code")
                for i in mycursor:
                    Brand.append(str(i))

                B_Sale=[]
                mycursor.execute("select count(BID) from booking group by Model_code")
                for i in mycursor:
                    B_Sale.append(i)

                plt.plot(Brand,B_Sale,marker='.',linewidth=2, markersize=12)
                plt.title("Modelwise Sales Report of 2021")

                plt.xlabel("---Vehicle Models---")
                plt.ylabel("---Sale of Vehicles---")

                plt.grid(True)
                plt.show()


            elif sr==2:
                Sale=[]
                for i in range(1,8):
                    mycursor.execute("select count(BID) from booking where B_date like '2021-0{}%'".format(i))
                    for i in mycursor:
                        Sale.append(i)

                Months=['January','February','March','April','May','June','July']

                plt.plot(Months,Sale,marker='.',linewidth=2, markersize=12)
                plt.title("Month-wise Sales Report of 2021")

                plt.xlabel("---Month---")
                plt.ylabel("---Sale---")

                plt.grid(True)
                plt.show()


            elif sr==3:
                    Emp=[]
                    mycursor.execute("select emp_id from booking group by emp_id")
                    for i in mycursor:
                        for j in i:
                            Emp.append(j)

                    E_s=[]
                    mycursor.execute("select count(BID) from booking group by emp_id")
                    for i in mycursor:
                        for j in i:
                            E_s.append(int(j))

                    E_sale= np.array(E_s)

                    plt.pie(E_sale,labels=Emp,autopct='%1.0f%%')
                    plt.title("Sales Target Report of Employees - 2021")
                    plt.show()
                

#Exit
        elif c==6:
            print("Thank you for Visiting!")
            break

    COUNT+=1
