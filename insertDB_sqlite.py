import sqlite3
import csv
from sqlite3 import Error

def main():
    student_id = input("student_id : ")
    student_firstN = input("student_firstName : ")
    student_lastN = input("student_lastName : ")
    db = input("db : ")
    file = input("file : ")
    conn = create_connect(db)
    if conn is not None:
        inf = (student_id, student_firstN, student_lastN)
        create_studnt(conn, inf)
        create_studnt_records(conn, file, student_id)
    else:
        print("Error cant create database connection.")

def create_connect(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None

def create_studnt(conn, inf):
    try:
        add_student = '''INSERT INTO Student
                  (Student_id, First_name, Last_name) 
                   VALUES (?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(add_student, inf)
    except Error as e:
        print(e)
    conn.commit()
    cur.close()
    
def create_studnt_records(conn, file, id):
    try:
        add_subject = '''INSERT INTO Student_records 
                   (SubjectID, SubjectName, Weight, Section, Grade, Term, Student_id) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)'''
        cur = conn.cursor()
        with open (file, encoding="utf8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    record = (row['SubjectID'],row['SubjectName'],row['weight'],\
                              row['section'],row['grade'],row['term'],id)
                    print(record, end='  ')
                    cur.execute(add_subject, record)
                except Error as e:
                    print(e)
                else:
                    print('--done--')
    except Error as e:
        print(e)
    conn.commit()
    cur.close()
    
if __name__ == '__main__':
    main()