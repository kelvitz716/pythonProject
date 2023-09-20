import sqlite3

# Connect to DB
try:
    SQLite_connect = sqlite3.connect('sqlite3db.db')
    cursor = SQLite_connect.cursor()
    print('Sucessfully connected to DB')

    SQLite_Insert_Query = '''
    INSERT INTO SqliteDb_developers
    (id, name, email, joining_date, salary)
    VALUES
    (01, 'James', 'james@gmail.com', '2020-01-03', 30000);'''

    cursor.execute(SQLite_Insert_Query)
    SQLite_connect.commit()
    print('Data successfully inserted in the table', cursor.rowcount)
    cursor.close

except Exception as e:
    print(e)

finally:
    if SQLite_connect:
        SQLite_connect.close()
        print('DB connection closed')