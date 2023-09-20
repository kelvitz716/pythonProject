import sqlite3

def updateTable(id, salary):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print('Successfully connected to DB')

        SQLite3_Update_Query = '''
                                UPDATE SqliteDB_Developers SET SALARY = ? WHERE ID = ?;'''
        data = (salary, id) # this is positional arguments depending on how the statement is setup, vice-verser doesn't work
        cursor.execute(SQLite3_Update_Query, data)
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

updateTable(1, 30000)