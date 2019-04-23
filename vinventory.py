import sqlite3
import sys
import datetime

conn = sqlite3.connect("myinventory.db")

x = 1
now = datetime.datetime.now()

if (conn) :
    print ("Database created")

else:
    print("Error connecting database or connecting to it")

def CreateTable():
    try:
        conn.execute('''CREAT TABLE IF NOT EXSIST VINVENTORY (
            ProductName TEXT NOT NULL,FROM_ TEXT NOT NULL, ArrivalDate TEXT NOT NULL,
            ArrivalTime TEXT NOT NULL, LocationInInventory TEXT NOT NULL);''')
        print("Table Created Sucessfully")

    except Error as e:
        print (e)
        pass

def InsertData():
    name = input("Enter the name of the item:")
    from_ = input("Enter the from location of the items:")
    loc = input ("Enter the item inventory location:")
    avd = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    avt = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:
        conn.execute("INSERT INTO VINVENTORY (ProductName,From_,ArrivalDate,ArrivalTime,LocationInInventory)\
            values("+"'"+ str (name) +"'" + ",'"+ str(from_) +"','"+ str (adv)+"','"+str(avt)+"','"+str(loc)+"')");
        conn.commit()
        print("**Data inserted successfully**")
        print("")
        print("")
    except Error as e:
        print (e)
        pass
    def selectData():
        try:
            cursor = conn.execute ("SELECT oid,ProductName, From_,ArrivalDate, ArrivalTime, LocationInInventory FROM VINVENTORY" )
            print("")
            print("")
            print('*********')
            for row in cursor:
                print("ID =", row[0])
                print("ProductName =", row[1])
                print("From_ =", row[2])
                print("ArrivalDate =", row[3])
                print("ArrivalTime=", row[4])
                print("LocationInInventory =", row[5])
            print("")
            print("")
            print("****Operation Done successfully****")
        except Error as e:
            print (e)
            pass
        print("Here is your data")
        print("")
        print("")
def updateData():
    selectData()
    dte = input("Enter the ID of the column you want to edit")
    print("")
    print("")
    print("Press 1 if you want to edit ProductName")
    print("Press 2 if youwant to edit from_ ")
    print('Press 3 if you want to edit location')

    inp + input("Enter which feature of the data do you want to edit:")
    print("")
    upv = input ("Enter the new value:")

    if(inp == "1"):
        sql = "UPDATE VINVENTORY set ProductName = ? where oid =  ?"
    elif (inp == "2"):
       sql = "UPDATE VINVENTORY set From_ = ? where oid =  ?" 
    elif (inp == "3"):
       sql = "UPDATE VINVENTORY set LocationInInventory  = ? where oid =  ?"
    
    try:
        conn.execute(sql, (str(uvp), str(dte)))
        conn.connect()
        print ("successfully updated")

    except Error as e:
        print(e)
        pass

    def deleteData():
        selectData()

        id_   =  input("Above is your data choice choose the Id you want to delete:")
        try:
            sql = "DELETE FROM VINVENTORY WHERE oid = ?"
            conn.execute(sql,(str(id_)))
            conn.commit()
            print("sucessfully deleted")

        except Error as e:
            print (e)
            pass

    while(x):
        print("Choose the operation to perform")
        print("press 1 to insert the data")
        print("press 2 to view the data in database")
        print("press 3 to update the data in dataset")
        print("press 4 to Delete the data in dataset")
        print("press X to exit the system")
        name = input ("Choose an operation to perform")
        if (name =="1"):
            InsertData()
        elif(name == "2"):
            SelectData()
        elif(name == "3"):
            updateData()
        elif(name == "4"):
            deleteData()
        elif(name=="X"):
            conn.close()
            X=0


