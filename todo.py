# Todo Project
# CRUD => Create, Read, Update, Delete
 
# Step
 
# python => python -V or python --version
# pip list => display all the dependency of python
# mysql => pip install mysql-connector-python
 
# connect => connection, method
# cursor => cursor => cursor object
# execute => execute the query
 
import mysql.connector as mysql
 
con = mysql.connect(host="localhost", user="root", passwd="Jyoti@0987")
 
cursor = con.cursor()
 
cursor.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")
# Database => collection of tables
 
 
# print("Database created...")
 
cursor.execute("USE TODOAPP")
 
# create the tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")
 
 
# show databases or show tables
 
cursor.execute("SHOW TABLES")
 
for i in cursor:
    print(i)
 
# print("Table created...")
 
 
# insert data
 
while True:
    print("\n Task Management")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
        task = input("Enter task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        print("✅ Task added successfully!")
        con.commit() # commit the changes to the database
        print("Task added successfully!")
 
    elif choice == "5":
        print("Exiting Task Management...")
        break
 
    else:
        print("Invalid choice. Please try again.")
 
con.close()