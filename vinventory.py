import sqlite3
from sqlite3 import Error
import sys
import datetime

def create_connection(db_myinventory):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_myinventory)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn,create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:1
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insertdata():
    name = input("Enter the name of the item: ")
    ndc = input("Enter the national drug code of the items: ")
    location = input ("Enter the item inventory location: ")
    availability = input("Enter number of doses left: ")
    arrivaldate = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    expirationdate = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:
        conn.execute("INSERT INTO vaccines (name,ndc,location,availability,arrivaldate,expirationdate)\
            values("+"'"+ str(name) +"'" + ",'"+ str(ndc) +"', '"+ str(location) +"','"+ str (availability)+"','"+str(arrivaldate)+"','"+str(expirationdate)+"')")
        conn.commit()
        print("***Data inserted successfully**")
        print("")
        print("")
    except Error as e:
        print ("***Insert error: ",e)
        pass
def selectdata():
    try:
        cursor = conn.execute ("SELECT id,name, ndc,Location,availability,arrivaldate, expirationdate FROM vaccines" )
        alldata = []
        alldata.append(["ID","name","ndc","location","availability","arrivaldate","expirationdate"])
        for row in cursor:
            thisrow = []
            thisrow.append(row[0])
            thisrow.append(row[1])
            thisrow.append(row[2])
            thisrow.append(row[3])
            thisrow.append(row[4])
            thisrow.append(row[5])
            thisrow.append(row[6])
            alldata.append(thisrow)
        return alldata
    except Error as e:
        print (e)
        pass
def updatedata():
    print(selectdata())
    dte = input("Enter the ID of the column you want to edit")
    print("")
    print("")
    print("Press 1 if you want to edit name")
    print("Press 2 if youwant to edit ndc")
    print('Press 3 if you want to edit location')
    print('Press 4 if you want to edit availability')
    print('Press 5 if you want to edit arrivaldate')
    print('Press 6 if you want to edit expirationdate')

    inp + input("Enter which feature of the data do you want to edit:")
    print("")
    upv = input ("Enter the new value:")

    if(inp == "1"):
        sql = "UPDATE vaccines set Name = ? where id =  ?"
    elif (inp == "2"):
       sql = "UPDATE vaccines set ndc = ? where id =  ?" 
    elif (inp == "3"):
       sql = "UPDATE vaccines set location  = ? where id =  ?"
    elif (inp == "4"):
       sql = "UPDATE vaccines set availability  = ? where id =  ?"
    elif (inp == "5"):
       sql = "UPDATE vaccines set arrivaldate  = ? where id =  ?"
    elif (inp == "6"):
       sql = "UPDATE vaccines set expirationdate = ? where id =  ?"  
    try:
        conn.execute(sql, (str(uvp), str(dte)))
        conn.connect()
        print ("successfully updated")

    except Error as e:
        print(e)
        pass

def deletedata():
    selectdata()
    id_   =  input("Above is your data choice choose the Id you want to delete:")
    try:
        sql = "DELETE FROM vaccines WHERE id = "+id_
        conn.execute(sql,(str(id_)))
        conn.commit()
        print("sucessfully deleted")
    except Error as e:
        print (e)
        pass

conn = sqlite3.connect("myinventory.db")
now = datetime.datetime.now()

if conn:
    print ("Connected to database.",conn)
    
    if conn is not None:
        sql_create_vaccines_table = """ CREATE TABLE IF NOT EXISTS vaccines (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        ndc text,
                                        location text,
                                        availability text,
                                        arrivaldate text,
                                        expirationdate text
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
        insertdata()
    elif(name == "2"):
        print(selectdata())
    elif(name == "3"):
        updatedata()
    elif(name == "4"):
        deletedata()
    elif(name=="X"):
        conn.close()
        break