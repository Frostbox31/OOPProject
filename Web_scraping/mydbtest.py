import mysql.connector

mydb2 = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="F2814939p",
    database="DataProject"
)

# prepare a cursor object using cursor() method
cursor = mydb2.cursor()

sql = "SELECT * FROM coinvolume"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    # for i in range(0, 11):
    count = 0
    cname = []
    cvalue = []
    for row in results:
        if count <= 10:
            fname = row[1]
            fvol = row[2]
            
            # Now print fetched result
            print("count = %d, fname = %s, fvol = %d \n" %
                (count, fname, fvol))
            cname.append(fname)
            cvalue.append(fvol)
            count += 1
except:
    print("Error: unable to fecth data")
# disconnect from server
mydb2.close()

print(cname)
print(cvalue)
