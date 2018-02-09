import mysql.connector

def sqlexec(query = None, data = None):
    try:
        cnx = mysql.connector.connect(user='shared', password='nyxpluto', database='volvox')
        err = None
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return
        else:
            print(err)
            return

    cur = cnx.cursor()

    if query is not None and data is not None:
        cur.execute(query, data)    
        cnx.commit()
        res = None
    elif query is not None and data is None:
        cur.execute(query)
        res = cur.fetchall()
        
    cur.close()
    cnx.close()
    return res
