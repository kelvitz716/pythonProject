import sqlite3

def insertManyRecords(recordList):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = sqlite3.Cursor(SQLite_connect)
        print("Database connected successfully")

        SQLite3_Insert_Many_Records_Query = '''
        INSERT INTO SqliteDB_Developers
        (id, name, email, joining_date, salary)
        VALUES
        (?, ?, ?, ?, ?);'''

        cursor.executemany(SQLite3_Insert_Many_Records_Query, recordList)
        SQLite_connect.commit()
        print(f'Data successfully inserted in the table. {cursor.rowcount} row updated')
        cursor.close()


    except Exception as e:
        print(e)
    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print('DB connection closed')

recordsToInsert = [(5, 'Jos', 'jos@gmail.com', '2019-01-14', 9500),
                   (6, 'Chris', 'chris@gmail.com', '2019-05-15', 7600),
                   (7, 'Jonny', 'jonny@gmail.com', '2019-03-27', 8400)]

insertManyRecords(recordsToInsert)