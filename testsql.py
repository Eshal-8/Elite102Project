import unittest
import mysql.connector

connection = mysql.connector.connect(user = 'root', password = 'Magic', 
                                     host = 'localhost', 
                                     port = '3306',
                                     database = 'phosmabank')

cursor = connection.cursor()
testQuery = ("SELECT * FROM userinfo")
cursor.execute(testQuery)

for item in cursor:

    print(item)

print('Hello world!')

cursor.close()
connection.close()

#Awesome! It works! Yay!