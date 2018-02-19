import sys
import mysql.connector as sql


# create a new empty database 
def main():
    # set config
    user = input('user : ')
    password = input('password : ')
    port = input('port : ')
    host = input('host : ')
    dbName = input('databasename : ')
    # connect to host,user ,pass and dbname
    db = sql.connect(user="{"+user+"}", password={password}, host="{"+host+"}", port=3306, database={dbName})
    # try to create db
    try:
        cursor.execute('CREATE DATABASE {}'.format(dbName))
        db.commit()
        cursor.close()
        print('---done---')
    except sql.Error as err:
        print("Something went wrong: {}".format(err))

if __name__ == "__main__":
   main()