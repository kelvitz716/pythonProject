import sqlite3

def toTitleCase(string):
    return str(string).title()

def getDevName(id):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print(f'DB connected successfully!!')

        SQLite_connect.create_function("TOTITLECASE", 1, toTitleCase)
        SQLite3_Read_Query = '''
                SELECT TOTITLECASE(name) FROM SqliteDB_Developers WHERE id = ?;'''
        
        SQLite_connect.execute(SQLite3_Read_Query, (id,))
        name = cursor.fetchone()
        print(f"The developer's name is {name}")

        cursor.close()

    except Exception as e:
        print(e)

    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print(f'DB closed successfully!!')

getDevName(2)