import requests
from bs4 import BeautifulSoup
from getpass import getpass
#from mysql.connector import connect, Error
import sqlite3
from sqlalchemy import create_engine
import pandas as pd

base_url='https://pe.computrabajo.com'
# Making a GET request
#HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
HEADERS = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
r = requests.get(base_url,headers=HEADERS)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s= soup.find_all('ul',class_='lS')
content=[]
for tags in s:
	content=content + tags.find_all('a')

endpoints=[]
for link in content:
	endpoints.append(link.get('href'))

jobs=[]
places=[]
for ep in endpoints:
	r = requests.get(base_url+ep,headers=HEADERS)
	soup = BeautifulSoup(r.content, 'html.parser')

	ss=soup.find_all('article')
	
	for link in ss:
		jobs=jobs+link.find_all('h1')
		places=places+link.find_all('p',class_='fs16')



df = pd.DataFrame(columns=["descripcion","lugar"])
for i in range(len(jobs)):
	objeto ={'descripcion':jobs[i].text,'lugar':''.join(places[i].find_all(recursive=False,text=True)).strip()}
	df = df.append(objeto,ignore_index = True)


con = sqlite3.connect("db.sqlite3")
df.to_sql('myapp_trabajos', con, if_exists="replace",index=True,index_label='id')

con.close()
print("ready.")

'''
try:
	with connect(
		host="localhost",
		#user="root",
		password="",
		#database="trabajos",
		user="arturoalmaquinta_admin",
		#password="gamer001!",
		database="pruebas",
	) as connection:
		db_data = "mysql+pymysql://"+ connection.user+":gamer001!@127.0.0.1,3306/"+connection.database+"?charset=utf8mb4"
		engine = create_engine(db_data)
		df.to_sql('myapp_trabajos',engine,if_exists='replace',index=True,index_label='id')
		print("ready.")

except Error as e:
	print(e)

for j in jobs:
	print(j.text)
print("*****************************************************************")
for p in places:
	print(''.join(p.find_all(recursive=False,text=True)).strip())
'''
