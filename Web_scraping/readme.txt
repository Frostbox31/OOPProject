#1 install python from python.org
#2 install virtualenv, check - virtualenv --version, install - pip install virtualenv
#3 setup virtual environment, virtualenv venv
#4 test activate virtual environment, .\venv\Scripts\activate
#5 install flask, pip install flask, check - pip show flask OR flask --version
#6 install mysql connector pip install mysql-connector-python (if nv do this will encounter SHA error etc)
#7 test run, python run.py

#SELECT * FROM coingeckodata WHERE Name like '%ethereum%' AND (SELECT MAX(Date)) Limit 1

select * from coingeckodata t join ( select name, max(date) as date from coingeckodata group by name) s on  s.name = t.name and s.date = t.date;