import csv, sys

# insert data to mysql database
def main(user, csv):
    createDB()
    insertData(user, csv)
    print(user + csv)

# create DB in first time
def createDB():
    pass

# insert data to mysql
def insertData(user, csv):
    pass


if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])