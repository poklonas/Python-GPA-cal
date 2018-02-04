import sqlite3
from sqlite3 import Error

def main():
    db = "./gradeInf.db"
    table_student = """CREATE TABLE IF NOT EXISTS Student (
       `Student_id` text  PRIMARY KEY,  
       `First_name` text  NOT NULL,
       `Last_name` text  NOT NULL)"""
                        
    table_Student_Records = """CREATE TABLE IF NOT EXISTS Student_Records (
        PK INTEGER PRIMARY KEY AUTOINCREMENT,
        SubjectID text NOT NULL,
        SubjectName text NOT NULL,
        Weight INTEGER NOT NULL,
        Section INTEGER NOT NULL,
        Grade text NOT NULL,
        Term INTEGER NOT NULL,
        Student_id text NOT NULL,
        FOREIGN KEY (Student_id) REFERENCES Student(Student_id))"""
    
    conn = create_connect(db)
    if conn is not None:
        create_table(conn, table_student)
        create_table(conn, table_Student_Records)
    else:
        print("Error cant create database connection.")

def create_connect(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    conn.commit()
    c.close()
    print('done')


if __name__ == '__main__':
    main()