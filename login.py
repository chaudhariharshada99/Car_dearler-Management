import mysql.connector
import employee as emp
import sys

mydb= mysql.connector.connect(host='localhost',user='root',database='car_dealer')

mycursor = mydb.cursor()

#Login page
print("\n\n\n******************************************************************")
print("               Welcome to Rana Motors Employee portal.\n")

u_list=[]
mycursor.execute("select Ename from employees")

for i in mycursor:
    u_list.append(str(i))

U=input("            \tEnter your registered name:")
u="('{}',)".format(U)
if u in u_list:
    print("\t\t\tSuccessfully logged in\n")
else:
    print("Unknown user.")

    c=int(input("Press 0 to Exit.\nPress 1 to Register New User.\n"))
    if c==0:
        print("Bye")
        sys.exit()
    
    elif c==1:
        e = emp.Employee()
        
            
        

    
