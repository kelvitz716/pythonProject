import sqlite3

def convertToFile(data, filename):
    # Convert binary to digital.
    with open(filename, 'wb') as file:
        file.write(data)
    print(f'stored BLOB data in {filename}')

def readBLOB(empID):
    try:
        SQLite_connect = sqlite3.connect('sqlite3db_BLOB.db')
        cursor = SQLite_connect.cursor()
        print(f'DB connected successfully!!')

        SQLite3_Read_Query = '''
                        SELECT * FROM NEW_EMPLOYEE
                        WHERE ID = ?;'''
        
        cursor.execute(SQLite3_Read_Query, (empID,))
        record = cursor.fetchall()
        for row in record:
            print(f'''Id = {row[0]}
                    Name = {row[1]}''')
            Name = row[1]
            Photo = row[2]
            Resume = row[3]

            print(f'Storing employees data to disk \n')

            photoPath = Name + ".jpg"
            resumePath = Name + "_resume.txt"

            convertToFile(Photo, photoPath)
            convertToFile(Resume, resumePath)

            
        print(f'Data added sucessfully')

        cursor.close()

    except Exception as e:
        print(e)

    finally:
        if SQLite_connect:
            SQLite_connect.close()
            print(f'DB closed sucessfully!!')

readBLOB(1)
readBLOB(2)
