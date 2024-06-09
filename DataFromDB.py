import sqlite3 as sql
from sys import argv as cmdArgs

def getDataFromDB() -> None:

    sqlConnection = sql.connect(cmdArgs[1])

    cursor = sqlConnection.cursor()

    query = "SELECT * FROM Song WHERE totalPlayTimems > 5000 "

    cursor.execute(query)

    FILE_DataFromDB = open("DataFromSQL_DB.py", 'w')

    result = cursor.fetchall()
    print(result, file=FILE_DataFromDB)

if __name__ == '__main__':
    getDataFromDB()

else:
    print("This file is meant to run as a script")
