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
    add_subject = ("INSERT INTO Student_records "
               "(SubjectID, SubjectName, Weight, Section, Grade, Term, Student_id) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
	# read and write
    with open (file, encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                record = (row['SubjectID'],row['SubjectName'],row['weight'],\
                          row['section'],row['grade'],row['term'],row['Student_id'])
                cursor.execute(add_subject, record)
            except sql.Error as err:
                print(err.msg)
    db.commit()
    cursor.close()  
    
if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])