import sqlite3

def getDevInfo(id):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print('Sucessfully connected to DB')

        SQLite_Select_Query = '''
                        SELECT * FROM SqliteDB_Developers WHERE id = ?;'''
        cursor.execute(SQLite_Select_Query, (id,))
        records = cursor.fetchall()
       #records = cursor.fetchone() -----> this will return only 1 row
        print(f'The Selected Id is {id}')
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

number = int(input("Enter the id you'd like information about: "))
getDevInfo(number)