# Install Mysql on your computer  
# pip install mysql 
# pip install mysql-connector or 
# pip install mysql-connector-python



import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ed$1115Ed$"
    
    )

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# Create a database named "elderly_care_db"
cursorObject.execute("CREATE DATABASE elyor_db")
print('all done')