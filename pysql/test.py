
import mysql.connector

def main():
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",password='root',
    database="giraffe"
    )

    mycursor =mydb.cursor(buffered=True)

    create_database="""Create Database Girraffe"""

    create_table="""Create Table student(
        student_id Int Primary Key Auto_Increment,
        name varchar(20) not null,
        major varchar(20)  not null,
    );"""

    delete_table="""
        Drop Table student
    """


    alter_table="""
    Alter table student ADD gpa Decimal(3,2);
    
    """

    alter_table2="""
    Alter table student drop column gpa;
    
    """
    describe_table="""Describe student;"""
    id=1
    name="Steven"
    major="ComputerScience"
    insert_tst=("insert into student(name,major) values('test13','test23');")

    mycursor.execute("select name,major from student")
    mydb.commit()
    for x in mycursor:
        print(x)

main()