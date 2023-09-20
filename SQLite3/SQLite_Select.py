import sqlite3

def readSqlite3Table():
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print('Sucessfully connected to DB')

        SQLite_Select_Query = '''
        SELECT * FROM SqliteDB_Developers;'''

        cursor.execute(SQLite_Select_Query)
        records = cursor.fetchall()
        print(f'Total rows are {len(records)}')
        print('Printing each row')
        for row in records:
            print(f'''
                Id: {row[0]}
                Name: {row[1]}
                Email: {row[2]}
                Joining Date: {row[3]}
                Salary: {row[4]}
                \v''')
            
        cursor.close()

    except Exception as e:
        print(e)
    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print('DB connection closed')

readSqlite3Table()
    