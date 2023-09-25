import sqlite3

def getHospitalTable(id):
    try:
        SQLConnect = sqlite3.connect("MedicalDB.db")
        cursor = SQLConnect.cursor()
        #print(f"Connected to MedicalDB successfully.")

        SQL_Query = '''
                    SELECT * FROM Hospital WHERE Hospital_Id = ?;'''
        
        cursor.execute(SQL_Query, (id,))
        data = cursor.fetchall()
        #for row in data:
            #print(f'''
            #        Hospital Id:    {row[0]}
            #        Hospital Name:  {row[1]}
            #        Bed Count:      {row[2]}
            #                            ''')
        cursor.close()
        return data

    except Exception as e:
        print(e)

    finally:
        if SQLConnect:
            SQLConnect.close()
            #print(f"MedicalDB closed.")

getHospitalTable(id)