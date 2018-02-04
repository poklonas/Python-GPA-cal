import csv
import sys
import mysql.connector as sql
from mysql.connector import errorcode

# insert data to mysql database
def main(student, file, dbName):
    # set config
    port = '3000'
    user = 'root'
    password = '123456789'
    # connect to host,user ,pass and dbname
    db = sql.connect(user = user, password = password, port = port, database = dbName)
    cursor = db.cursor()
    # set sql command
    add_student = ("INSERT INTO Student "
               "(Student_id, First_name, Last_name) "
               "VALUES (%s, %s, %s)")
    add_subject = ("INSERT INTO Student_records "
               "(SubjectID, SubjectName, Weight, Section, Grade, Term, Student_id) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    # create new student from student id 
    try:
        print('try to add student id {}: '.format(student[0]), end='')
        cursor.execute(add_student, student)
    except sql.Error as err:
        print(err.msg)
    else:
        print('done')
               
    with open (file, encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                record = (row['SubjectID'],row['SubjectName'],row['weight'],\
                          row['section'],row['grade'],row['term'],student[0])
                print(record, end='  ')
                cursor.execute(add_subject, record)
            except sql.Error as err:
                print(err.msg)
            else:
                print('--done--')
    db.commit()
    cursor.close()  
    
if __name__ == "__main__":
   main(sys.argv[1].split(','), sys.argv[2], sys.argv[3])