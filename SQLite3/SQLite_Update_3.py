import sqlite3

def updateTable(rowList):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print('Successfully connected to DB')

        SQLite3_Update_Query = '''
                                UPDATE SqliteDB_Developers SET SALARY = ? WHERE ID = ?;'''
        
        cursor.executemany(SQLite3_Update_Query, rowList)
        SQLite_connect.commit()
        print(f'Database updated successfully. {cursor.rowcount} rows affected')
        cursor.close()
        

    except Exception as e:
        print(e)
        SQLite_connect.rollback()
        print('Rollback successful: ')

    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print('DB connection closed')

rawData = [(380000, 2),
           (50000, 3),
           (10000000, 4),
           (8400, 7),
           (7600.0, 6),
           (9500.0, 5)]

updateTable(rawData)