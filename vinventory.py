import sqlite3
from sqlite3 import Error
import sys
import datetime
# a comment

def create_table(conn,create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def InsertData():
    name = input("Enter the name of the item: ")
    ndc = input("Enter the national drug code of the items: ")
    loc = input ("Enter the item inventory location: ")
    aval = input("Enter number of doses left: ")
    avd = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    avt = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:
        conn.execute("INSERT INTO vaccines (name,ndc,loc,aval,avd,avt)\
            values("+"'"+ str(name) +"'" + ",'"+ str(ndc) +"', '"+ str(loc) +"','"+ str (aval)+"','"+str(avd)+"','"+str(avt)+"')");
        conn.commit()
        print("**Data inserted successfully**")
        print("")
        print("")
    except Error as e:
        print (e)
        pass
def selectData():
    try:
        cursor = conn.execute ("SELECT id,name, ndc,LocationInInventory,Availability,ArrivalDate, ArrivalTime, FROM vaccines" )
        print("")
        print("")
        print('*********')
        for row in cursor:
            print("ID =", row[0])
            print("Name =", row[1])
            print("ndc =", row[2])
            print("LocationInInventory =", row[3])
            print("AvailabilityArrivalTime=", row[4])
            print("ArrivalDate =", row[5])
            print("ArrivalTime=", row[6])
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
    print("Press 1 if you want to edit VName")
    print("Press 2 if youwant to edit ndc")
    print('Press 3 if you want to edit location')
    print('Press 4 if you want to edit Aval ')

    inp + input("Enter which feature of the data do you want to edit:")
    print("")
    upv = input ("Enter the new value:")

    if(inp == "1"):
        sql = "UPDATE VINVENTORY set ProductName = ? where id =  ?"
    elif (inp == "2"):
       sql = "UPDATE VINVENTORY set ndc = ? where id =  ?" 
    elif (inp == "3"):
       sql = "UPDATE VINVENTORY set LocationInInventory  = ? where id =  ?"
    elif (inp == "4"):
       sql = "UPDATE VINVENTORY set aval  = ? where id =  ?"
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
        sql = "DELETE FROM VINVENTORY WHERE id = ?"
        conn.execute(sql,(str(id_)))
        conn.commit()
        print("sucessfully deleted")
    except Error as e:
        print (e)
        pass

conn = sqlite3.connect("myinventory.db")
now = datetime.datetime.now()

if (conn) :
    print ("Connected to database.",conn)
    
    if conn is not None:
        sql_create_vaccines_table = """ CREATE TABLE IF NOT EXISTS vaccines (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        exp_date text,
                                        ndc text,
                                        location text,
                                        avd text,
                                        aval text,
                                        avt text
                                    ); """
            # create projects table
        create_table(conn, sql_create_vaccines_table)
    else:
        print("Error! cannot create the database connection.")

else:
    print("Error connecting database or connecting to it")

while True:
    print("Choose the operation to perform")
    print("press 1 to insert the data")
    print("press 2 to view the data in database")
    print("press 3 to update the data in dataset")
    print("press 4 to Delete the data in dataset")
    print("press X to exit the system")
    name = input ("Choose an operation to perform: ")
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
        break