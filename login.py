#Standard library import
import mysql.connector

#Connect with the precise info, also with dataset name






def checkCredetials(username, password):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7gimtwDS.1.1",
    database="volleyballdatabase"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT M.username, M.password FROM manager M")
    for x in mycursor:
        if username==x[0]:
            if password==x[1]:
                return 1
            else:
                return 0
    mycursor.execute("SELECT J.username, J.password FROM jury J")
    for x in mycursor:
        if username==x[0]:
            if password==x[1]:
                return 2
            else:
                return 0
    mycursor.execute("SELECT P.username, P.password FROM player P")
    for x in mycursor:
        if username==x[0]:
            if password==x[1]:
                return 3
            else:
                return 0
    mycursor.execute("SELECT C.username, C.password FROM coach C")
    for x in mycursor:
        if username==x[0]:
            if password==x[1]:
                return 4
            else:
                return 0
    #burda databaseden name password tuple çek sonra check et
    mycursor.close()
    mydb.close()
    return 0
