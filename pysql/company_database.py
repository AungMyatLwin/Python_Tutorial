import mysql.connector

class Company:
    def __init__(self,hostt,usert,passwordt,dbst):
        self.hostt=hostt
        self.usert=usert
        self.passwordt=passwordt
        self.dbst=dbst
        self.mydb=mysql.connector.connect(
            host=self.hostt,
            user=self.usert,
            password=self.passwordt,
            database=self.dbst
        )
        self.mycursor=self.mydb.cursor(buffered=True)

    def create_databse(self,db):
        self.cursor_execute(f'Create database {db}')

    def create_table(self,tname):
        self.cursor_execute(f'Create Table {tname}')

    def cursor_execute(self,queres):
        self.mycursor.execute(queres)

    def cursor_commit(self):
        self.mycursor.commit()

    def drop_table(self,tname):
        self.cursor_execute(f"Drop Table {tname}")
    
    def show_queries(self):
        for x in self.mycursor:
            print(x)


    


cdb=Company('localhost','root','root','giraffe')
# cdb.create_databse('Test')
# cdb.drop_table('student')
cdb.cursor_execute("Show databases")
cdb.show_queries()
