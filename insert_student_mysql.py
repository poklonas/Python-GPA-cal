import csv
import sys
import MySQLdb as sql

# insert data to mysql database
def main( file, dbName):
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

    # create new student from student id 
    with open (file, encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                record = (row['Student_id'],row['First_name'],row['Last_name'])
                cursor.execute(add_student, record)
            except sql.Error as err:
                print(err.msg)
    db.commit()
    cursor.close()  
    
if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])