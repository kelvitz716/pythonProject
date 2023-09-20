import sqlite3

try:
    sqliteConnection = sqlite3.connect('sqlite3db.db')
    Cursor = sqlite3.Cursor(sqliteConnection)
    print("Database created successfully")

    sqlite3_select_query = "select sqlite_version();"
    Cursor.execute(sqlite3_select_query)
    record = Cursor.fetchall()
    print(f"SQLite3 Database version is: {record}")
    Cursor.close()

    Cursor = sqlite3.Cursor(sqliteConnection)
    print("Database created successfully")

    sqlite3_create_table_query = '''
    CREATE TABLE SqliteDB_Developers
    (id INTERGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date datetime,
    salary REAL NOT NULL);
    '''

    Cursor.execute(sqlite3_create_table_query)
    sqlite3.connect('sqlite3db.db').commit()
    print('SqliteDB_Developers Table created')

    Cursor.close()

    # How to execute SQLite3 scripts
   # Cursor = sqlite3.Cursor(sqliteConnection)
   # print("Database created successfully")
   # with open("C:\Users\user\PycharmProjects\pythonProject\.db.sql", 'r') as sql_file:
   #     sql_script = sql_file.read()

    #    '''Note: After connecting to SQLite, We read all content of an SQLite script file stored on disk #and copied it into a python string variable. Then we called the cursor.executscript(script) #method to execute all SQL statements in one call.'''
    
   # Cursor.executescript(sql_script)
   # print('SQLite3 script executed sucessfully.')

   # Cursor.close()

except Exception as e:
    print(e)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Database connection closed.')

