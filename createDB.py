import sys
import mysql.connector as sql


# create a new empty database 
def main(dbName):
    # set config
    user = 'root'
    password = '123456789'
    port = '3000'
    # connect to host,user ,pass and dbname
    db = sql.connect(user=user, password=password, port=port)
    cursor = db.cursor()
    # try to create db
    try:
        cursor.execute('CREATE DATABASE {}'.format(dbName))
        db.commit()
        cursor.close()
        print('---done---')
    except sql.Error as err:
        print("Something went wrong: {}".format(err))

if __name__ == "__main__":
   main(sys.argv[1])