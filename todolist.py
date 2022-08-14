import sqlite3

class NoteTake:
    def __init__(self,noteName):
        self.noteName=noteName
        self.place=0
        self.con = ""

    def connect(self):
        self.file=sqlite3.connect(f'{self.noteName}.db')
        self.con=self.file.cursor()


    def create_sql(self):
        self.con.execute(f'Create Table {self.noteName} (id INTEGER PRIMARY Key,Todo Text)')

    def dbexecute(self,sql):
        self.con.execute(sql)
        self.file.commit()

    def create_notes(self,notes):
        sql=f"""Insert into {self.noteName}(Todo) values("{notes}"); """
        print(self.noteName)
        print(sql)
        self.dbexecute(sql)
    
    def read_notes(self):
        return self.con.execute(f"Select * from {self.noteName}")

    def edit_notes(self,msg,id):
        sql=f"""UPDATE {self.noteName}
                SET Todo='{msg}'
                where id={id}
                """
        self.dbexecute(sql)

    def delete_notes(self,line_no):
        sql=f"""DELETE FROM {self.noteName}
                WHERE id={line_no};"""
        self.dbexecute(sql)


    def close_sql(self):
        self.file.close()


n=NoteTake("Todolist")
n.connect()
n.create_sql()
n.create_notes("Hello")
n.create_notes("123")
readline=n.read_notes()
for x in readline:
    print(x)


# n.edit_notes("editing Hello",1)
n.delete_notes(4)
n.delete_notes(3)

readline=n.read_notes()
for x in readline:
    print(x)


n.close_sql()
