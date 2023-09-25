import  sqlite3

def hospitalTable():
    try:
        SQLiteconnect = sqlite3.connect("MedicalDB.db")
        Cursor = SQLiteconnect.cursor()
        print(f"MedicalDB connected successfully.")

        SQLite_Query = '''
                CREATE TABLE Hospital 
                (Hospital_Id INTERGER NOT NULL PRIMARY KEY,
                Hospital_Name TEXT NOT NULL,
                Bed_Count INTERGER NOT NULL
                );
                INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
                VALUES 
                ('1', 'Mayo Clinic', 200), 
                ('2', 'Cleveland Clinic', 400), 
                ('3', 'Johns Hopkins', 1000), 
                ('4', 'UCLA Medical Center', 1500);
                CREATE TABLE Doctor 
                (Doctor_Id INTERGER NOT NULL PRIMARY KEY,
                Doctor_Name TEXT NOT NULL,
                Hospital_Id INTERGER NOT NULL REFERENCES Hospital (Hospital_Id),
                Joining_Date DATE NOT NULL,
                Speciality TEXT NOT NULL,
                Salary INTERGER NOT NULL,
                Experience INTERGER 
                );
                INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
                VALUES 
                ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
                ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
                ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
                ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
                ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
                ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
                ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
                ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);'''
        
        Cursor.executescript(SQLite_Query)
        SQLiteconnect.commit()
        print(f"MedicalDB successfully populated.")
        Cursor.close()
   
    except Exception as e:
        print(e)

    finally:
        if SQLiteconnect:
            SQLiteconnect.close()
            print(f"MedicalDB clossed sucessfully.")

hospitalTable()