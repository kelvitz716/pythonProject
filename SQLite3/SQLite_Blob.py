import sqlite3

def convertToBinary(filename):
    # Convert digital to binary
    with open(filename, 'rb') as file:
        BLOBdata = file.read()
    return BLOBdata

def createNewDb():
    try:
        SQLite_connect = sqlite3.connect('sqlite3db_BLOB.db')
        cursor = SQLite_connect.cursor()
        print(f'DB connected successfully!!')

        SQLite3_Create_Query = '''
                        CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);'''
        
        cursor.execute(SQLite3_Create_Query)
        SQLite_connect.commit()
        print(f'Database created sucessfully')

        cursor.close()
    except Exception as e:
        print(e)
    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print(f'DB closed sucessfully!!')

def insertBLOB(empID, name, photo, resumeFile):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db_BLOB.db')
        cursor = SQLite_connect.cursor()
        print(f'DB connected successfully!!')

        SQLite3_Create_Query = '''
                        INSERT INTO NEW_EMPLOYEE
                        (ID, NAME, PHOTO, RESUME)
                        VALUES
                        (?, ?, ?, ?);'''
        
        empPhoto = convertToBinary(photo)
        resume = convertToBinary(resumeFile)

        # Convert data into a tuple
        data_tuple = (empID, name, empPhoto, resume)

        cursor.execute(SQLite3_Create_Query, data_tuple)
        SQLite_connect.commit()
        print(f'Data added sucessfully')

        cursor.close()
    except Exception as e:
        print(e)
    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print(f'DB closed sucessfully!!')

insertBLOB(1, 'Smith', "PXL_20230505_103914098.jpg", "resume_1.txt")
insertBLOB(2, 'David', "IMG_20230910_131236.jpg", "resume_2.txt")
