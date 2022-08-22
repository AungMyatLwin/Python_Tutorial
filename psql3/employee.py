import sqlite3 as sq

class Employee:
    def __init__(self,name,age,position,salary):
        self.name=name
        self.age=age
        self.position=position
        self.salary=salary
    
    @classmethod
    def create_dbs(cls):
        connection = sq.connect("Employee.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE Employee (name TEXT, age TEXT, position TEXT,salary INT)")
        print("db created")


    @property
    def get_working_hrs(self):
        return("9 to 5 hours")
    @property
    def get_salary(self):
        return self.salary
    @get_salary.setter
    def set_salarys(self,salary):
        self.salary=salary

em1=Employee("Steven","28","GM",3000)
print(em1.get_salary)