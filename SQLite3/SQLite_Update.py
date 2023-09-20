import sqlite3

def updateTable():
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print('Successfully connected to DB')

        SQLite3_Update_Query = '''
                                UPDATE SqliteDB_Developers SET SALARY = 100000;'''
        cursor.execute(SQLite3_Update_Query)
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

updateTable()