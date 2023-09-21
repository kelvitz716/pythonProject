import sqlite3

def toDeleteMany(dataList):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print(f'DB connected successfully!!')

        SQLite3_Delete_Query = '''
                        DELETE FROM SqliteDB_Developers WHERE ID = ?'''
        
        cursor.executemany(SQLite3_Delete_Query, dataList)
        SQLite_connect.commit()
        print(f'{cursor.rowcount} rows deleted sucessfully')

        cursor.close()

    except Exception as e:
        print(e)
    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print(f'DB closed sucessfully!!')
        
dataList = [(2,),
            (4,)]
toDeleteMany(dataList)