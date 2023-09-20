import sqlite3

def updateTable(rowList):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print('Successfully connected to DB')

        SQLite3_Update_Query = '''
                                UPDATE SqliteDB_Developers SET EMAIL = ?, JOINING_DATE = ?, SALARY = ? WHERE ID = ?;'''
        
        cursor.executemany(SQLite3_Update_Query, rowList)
        SQLite_connect.commit()
        print(f'Database updated successfully. {cursor.rowcount} rows affected')
        cursor.close()
        

    except Exception as e:
        print(e)
        #SQLite_connect.rollback()
        #print('Rollback successful: ')

    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print('DB connection closed')

rawData = [("james@gmail.com",	"2020-01-03",	30000, 1),
            ("levis@gmail.com",	"2020-01-28",	380000, 2),
            ("mathew@aol.com",	"2023-12-25",	50000, 3),
            ("muhoni@yahoo.com",	"2001-04-01",	10000000.0, 4),
            ("jos@gmail.com",	"2019-01-14",	9500, 5),
            ("chris@gmail.com",	"2019-05-15",	7600, 6),
            ("jonny@gmail.com",	"2019-03-27",	8400, 7)]



updateTable(rawData)