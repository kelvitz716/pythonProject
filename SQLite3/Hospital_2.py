import sqlite3
from Hospital_3 import getHospitalTable

def getDoctorTable():
    try:
        SQLConnect = sqlite3.connect("MedicalDB.db")
        cursor = SQLConnect.cursor()
        print(f"Connected to MedicalDB successfully.")

        SQL_Query = '''
                    SELECT * FROM Doctor WHERE Salary >= 30000;'''
        
        cursor.execute(SQL_Query)
        data = cursor.fetchall()
        count = 0
    
        for row in data:
            hospital_id = int(row[2])
            hospital_data = getHospitalTable(hospital_id)
            

            for i in hospital_data:
                
                print(f"----------------------------------------------------------------------------------------")
                print(f'''
                        Id:             {row[0]}
                        Name:           {row[1]}
                        Hospital Id:    {row[2]}
                        Hospital Name:  {i[1]}
                        Joining Date:   {row[3]}
                        type            {type(row[3])}
                        Speciality:     {row[4]}
                        Salary:         {row[5]}
                        type            {type(row[5])}
                        ''')
                count += 1

        print(f"{count} rows shown") 
        cursor.close()

    except Exception as e:
        print(e)

    finally:
        if SQLConnect:
            SQLConnect.close()
            print(f"----------------------------------------------------------------------------------------")
            print(f"MedicalDB closed.")
            print(f"----------------------------------------------------------------------------------------")

getDoctorTable()