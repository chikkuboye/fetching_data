import requests
import json
import mysql.connector
import sys
try:

    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'userdb')
except mysql.connector.Error as e:
    sys.exit('connection failure')
mycursor = mydb.cursor()
data = requests.get("https://jsonplaceholder.typicode.com/posts").text

data_info = json.loads(data)
#print(data_info)
for i in data_info:
    id = str(i['userId'])
    sql = "INSERT INTO `post`(`User_Id`, `title`, `body`) VALUES ('"+id+"','"+i['title']+"','"+i['body']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print('Inserted succesfully',id)

