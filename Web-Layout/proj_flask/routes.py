from proj_flask import app
from flask import render_template

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
    1090.03,2104.09,2430.75,2030.11,
    5370.85,6160.51,6180.27,6540.93,
    8890.16,11700.89,13120.04,15600.09
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
    line_labels=blabels
    line_values=bvalues
    return render_template('index.html',title='Dashboard', max=17000, labels=line_labels, values=line_values)

@app.route('/bitcoin')
def bitcoin():
    line_labels=blabels
    line_values=bvalues
    return render_template('index.html',title='Bitcoin', max=17000, labels=line_labels, values=line_values)

@app.route('/ethereum')
def ethereum():
    line_labels=tlabels
    line_values=tvalues
    return render_template('index.html',title='Ethereum', max=17000, labels=line_labels, values=line_values)

    
@app.route('/home')
def homepage():
    return render_template('homepage.html',title='homepage')
