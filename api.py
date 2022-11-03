import requests
import json
import mysql.connector
import sys
try:

    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'userdb')
except mysql.connector.Error as e:
    sys.exit('connection failure')
mycursor = mydb.cursor()
data = requests.get("https://jsonplaceholder.typicode.com/users").text

data_info = json.loads(data)
#user_list = []
#print(data_info)
for i in data_info:
    #user_list.append([i["name"],i["email"],i["phone"]])
    sql = "INSERT INTO `user`(`Name`, `Address`, `Phone_num`) VALUES ('"+i['name']+"','"+i['email']+"','"+i['phone']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print('Data inserted Successfully',i['name'])
#print(user_list)