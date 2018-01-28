import csv, sys
import MySQLdb

# insert data to mysql database
def main(tableName, dbName):
    # set config
	host = 'localhost'
	user = 'root'
	password = '123456789'
	# connect to host,user ,pass and dbname
    db = MySQLdb.connect(host, user, password, dbName)
	cursor = db.cursor()
    # try to create db
    try:
	    cursor.execute()
	except:
	    db.rollback()
	
    print('---------complete---------')

if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])