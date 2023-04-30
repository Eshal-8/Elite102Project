import unittest
import mysql.connector

connection = mysql.connector.connect(user = 'root', password = 'Magic', 
                                     host = 'localhost', 
                                     port = '3306',
                                     database = 'phosmabank')

cursor = connection.cursor()
cursor.execute("SELECT id, username, password FROM userinfo")
_existinguser = []

for i in cursor:
    _existinguser.append(i)

print(_existinguser)
print(_existinguser[1][0])
#I LOOOVE MULTIDIMENSIONAL ARRAYS AHHH THEYRE SOOOO GOOD FOR ORGANIZATION <333

cursor.execute("SELECT balance FROM userinfo")

for i in cursor:
    print(i)

cursor.close()
connection.close()

#Awesome! It works! Yay!