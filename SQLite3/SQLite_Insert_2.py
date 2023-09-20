import sqlite3

def insertVariableIntoTable(id,name,email,joining_date,salary):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db.db')
        cursor = SQLite_connect.cursor()
        print('Sucessfully connected to DB')

        SQLite_Insert_Query = '''
        INSERT INTO SqliteDB_Developers
        (id, name, email, joining_date, salary)
        VALUES
        (?, ?, ?, ?, ?);'''
        data_tuple = (id, name, email, joining_date, salary)
        cursor.execute(SQLite_Insert_Query, data_tuple)
        SQLite_connect.commit()
        print(f'Data successfully inserted in the table. {cursor.rowcount} row updated')
        cursor.close

    except Exception as e:
        print(e)

    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print('DB connection closed')

insertVariableIntoTable(2, 'levis', 'levis@gmail.com', '2020-01-28', 380000)
insertVariableIntoTable(3, 'Mat', 'mathew@aol.com', '2023-12-25', 50000)
insertVariableIntoTable(4, 'Shee', 'muhoni@yahoo.com', '2001-04-01', 10000000)
