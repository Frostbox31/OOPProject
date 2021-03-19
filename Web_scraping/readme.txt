#1 install python from python.org
#2 install virtualenv run command: | check virtualenv version: virtualenv --version | install virtualenv: pip install virtualenv
#3 setup virtual environment run command: virtualenv venv
#4 test activate virtual environment run command: .\venv\Scripts\activate
#5 install flask run command: pip install flask | check - pip show flask OR flask --version
#6 install mysql connector run command: pip install mysql-connector-python (if nv do this will encounter SHA error etc)
#7 test run run command: python run.py

#New setup
# install python
# pip install virtualenv
# cd web_scraping, then run command: virtualenv venv
# run .\venv\Scripts\activate |after u activate, your starting instead of drive C:, it will show (venv)
# pip install flask
# pip install mysql-connector-python
# test run, must be in web_scraping directory and (venv), then type python run.py









#SELECT * FROM coingeckodata WHERE Name like '%ethereum%' AND (SELECT MAX(Date)) Limit 1

select * from coingeckodata t join ( select name, max(date) as date from coingeckodata group by name) s on  s.name = t.name and s.date = t.date;

#get second latest record in bitcoin
#SELECT * FROM (SELECT t.*, ROW_NUMBER() OVER(ORDER BY Date DESC) AS RowNumber FROM dataproject.coingeckodata t) AS tmp WHERE RowNumber = 2 and Name LIKE '%bitcoin%';


#SELECT * FROM dataproject.coingeckodata WHERE Date < ( SELECT MAX(Date) FROM dataproject.coingeckodata);
#SELECT TOP (1) * FROM dataproject.coingeckodata WHERE Date < ( SELECT MAX(Date) FROM dataproject.coingeckodata) ORDER BY Date DESC;

SELECT * FROM (SELECT t.*, ROW_NUMBER() OVER(ORDER BY Date DESC) AS RowNumber FROM dataproject.coingeckodata t) AS tmp WHERE RowNumber = 2;
#SELECT * FROM coingeckodata WHERE Name like 'bitcoin' Order By Date DESC;
#select * from coingeckodata t join ( select name, max(date) as date from coingeckodata group by name) s on  s.name = t.name and s.date = t.date;