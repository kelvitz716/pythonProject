import sqlite3

def deleteRecord(id):
    try:
        SQLite_connect = sqlite3.connect("sqlite3db.db")
        cursor = SQLite_connect.cursor()
        print(f'DB connected successfully!!')

        SQLite3_Delete_Query = '''
                    DELETE FROM SqliteDB_Developers WHERE ID = ?'''
        
        cursor.execute(SQLite3_Delete_Query, (id,))
        SQLite_connect.commit()
        print(f'Id {id} has been deleted successfully.')
        
        cursor.close()

    except Exception as e:
        print(e)
    
    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print(f'DB closed successfully')

toDelete = int(input('Enter the Id to be deleted: '))

deleteRecord(toDelete)