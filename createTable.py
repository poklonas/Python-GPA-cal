import sys
import mysql.connector as sql
from mysql.connector import errorcode

# create table student and student record for table 
def main(dbName):
    # set config
    port = '3000'
    user = 'root'
    password = '123456789'
    # connect to host,user ,pass and dbname
    db = sql.connect(user = user, password = password, port = port, database = dbName)
    cursor = db.cursor()
    # prepare table data
    TABLES = {}
    TABLES['Student'] = (
    "CREATE TABLE Student ("
    "   `Student_id` varchar(13) NOT NULL,  "
    "   `First_name` varchar(100) NOT NULL,"
    "   `Last_name` varchar(100) NOT NULL,"
    "   PRIMARY KEY (`Student_id`),"
    "   UNIQUE (Student_id))")
                        
    TABLES['Student_Records'] = (
    "CREATE TABLE Student_Records ("
    "    PK int(11) NOT NULL AUTO_INCREMENT,"
    "    SubjectID varchar(10) NOT NULL,"
    "    SubjectName varchar(100) NOT NULL,"
    "    Weight int(1) NOT NULL,"
    "    Section int(3) NOT NULL,"
    "    Grade varchar(2) NOT NULL,"
    "    Term int(2) NOT NULL,"
    "    Student_id varchar(13) NOT NULL,"
    "    PRIMARY KEY (`PK`),"
    "    FOREIGN KEY (Student_id) REFERENCES Student(Student_id))")
    
    # try to create db
    for name, ddl in TABLES.items():
        try:
            print("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)
        except sql.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
        
    db.commit()
    cursor.close()  

if __name__ == "__main__":
   main(sys.argv[1])