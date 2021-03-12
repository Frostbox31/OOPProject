from layout import app
from flask import render_template

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
clabels = []
cvalues = []
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    # for i in range(0, 11):
    count = 0
    for row in results:
        if count <= 10:
            fname = row[1]
            fvol = row[2]
            # Now print fetched result
            print("count = %d, fname = %s, fvol = %d \n" %
                  (count, fname, fvol))
            clabels.append(fname)
            cvalues.append(fvol)
            count += 1
except:
    print("Error: unable to fecth data")
# disconnect from server
mydb2.close()

blabels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

bvalues = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

tvalues = [
    1090.03, 2104.09, 2430.75, 2030.11,
    5370.85, 6160.51, 6180.27, 6540.93,
    8890.16, 11700.89, 13120.04, 15600.09
]

tlabels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route('/')
@app.route('/dash')
def dash():
    line_labels = clabels
    line_values = cvalues
    return render_template('index.html', title='Dashboard', max=99999999, labels=line_labels, values=line_values)


@app.route('/bitcoin')
def bitcoin():
    line_labels = blabels
    line_values = bvalues
    return render_template('index.html', title='Bitcoin', max=17000, labels=line_labels, values=line_values)


@app.route('/ethereum')
def ethereum():
    line_labels = tlabels
    line_values = tvalues
    return render_template('index.html', title='Ethereum', max=17000, labels=line_labels, values=line_values)


@app.route('/home')
def homepage():
    return render_template('homepage.html', title='homepage')
