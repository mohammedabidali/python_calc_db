import sqlite3
from contextlib import closing

number1 = input("Please enter first number: ")
num1 = int(number1)
number2 = input("Please enter second number: ")
num2 = int(number2)

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

sum = add(num1, num2)
sub = sub(num1, num2)
mul= mul(num1, num2)
div = div(num1, num2)

sum_str = "addition"
sub_str = "subtraction"
mul_str = "multiplication"
div_str = "division"

with closing(sqlite3.connect("data.db")) as connection:
    with closing(connection.cursor()) as cursor:
        #cursor.execute("CREATE TABLE operations_table (id INTEGER PRIMARY KEY, name TEXT, result INTEGER);")
        #cursor.execute("INSERT INTO operations_table (name) VALUES ('addition')")
        #connection.commit()

        cursor.execute(f"INSERT INTO operations_table (name, result) VALUES ('{sum_str}', {sum})")
        cursor.execute(f"INSERT INTO operations_table (name, result) VALUES ('{sub_str}', {sub})")
        cursor.execute(f"INSERT INTO operations_table (name, result) VALUES ('{mul_str}', {mul})")
        cursor.execute(f"INSERT INTO operations_table (name, result) VALUES ('{div_str}', {div})")
        connection.commit()
        cursor.execute("SELECT * FROM operations_table;")
        records = cursor.fetchall()
        print(records)







'''
def create_table():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            #cursor.execute("CREATE TABLE operations_table (id INTEGER PRIMARY KEY, name TEXT);")
            #cursor.execute("INSERT INTO operations_table (name) VALUES ('addition')")
            #connection.commit()

            cursor.execute("SELECT * FROM operations_table;")
            records = cursor.fetchall()
            print(records)

def insert():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("INSERT INTO operations_table (name) VALUES ('addition')")
            connection.commit()

def show():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM operations_table;")
            records = cursor.fetchall()
            print(records)
'''
