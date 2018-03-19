import sqlite3
import csv
import random
from sqlite3 import Error

def main():
    #start = input("start num : ")
	start = "300000"
    db = "gradeStudent.db"
    file = "5801012610164.csv"
    conn = create_connect(db)
    grade = ['A','B+','B','C+','C','D+','D','F','I']
    cur = conn.cursor()
    if conn is not None:
        for i in range(0,999999):
            start = str(int(start) + i)
            year = random.randint(550,620)
            if(i<100):
                student_id = str(year) + str(1012710000+int(start))
            elif(i<1000):
                student_id = str(year) + str(101271000+int(start))
            elif(i <10000):
                student_id = str(year) + str(10127100+int(start))
            elif(i <100000):
                student_id = str(year) + str(1012710+int(start))
            elif(i <1000000):
                student_id = str(year) + str(101271+int(start))
            student_firstN = "sarik_"+start
            student_lastN = "kumpan_"+start
            inf = (student_id, student_firstN, student_lastN)
            create_studnt(conn, inf)
            try:
                add_subject = '''INSERT INTO Student_records 
                           (SubjectID, SubjectName, Weight, Section, Grade, Term, Student_id) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)'''
                with open (file, encoding="utf8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            record = (row['SubjectID'],row['SubjectName'],row['Weight'],
                                      random.randint(1,5),grade[random.randint(0,8)],random.randint(1,10),student_id)
                            print(record, end='  ')
                            cur.execute(add_subject, record)
                        except Error as e:
                            print(e)
                        else:
                            print('--done--')
            except Error as e:
                print(e)
            print(i)
        else:
            print("Error cant create database connection.")
        conn.commit()
        cur.close()

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
   
    
if __name__ == '__main__':
    main()