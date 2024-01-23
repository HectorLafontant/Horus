import sqlite3

class students_database():
    def create_students_table():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute (
            "CREATE TABLE IF NOT EXISTS students ( \
                id INTEGER PRIMARY KEY, \
                first_name text, \
                last_name text, \
                identification text \
            )"
        )
        con.commit()
        con.close()

    def add_student_record(first_name, last_name, identification):
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("INSERT INTO students VALUES (NULL, ?, ?, ?)", (first_name, last_name, identification))
        con.commit()
        con.close()

    def query_students():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        records = cur.fetchall()
        con.close()
        return records

    def delete_students_records():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("DELETE FROM students")
        con.commit()
        con.close()

    create_students_table()

class days_database():
    def create_days_table():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS days ( \
                id INTEGER PRIMARY KEY, \
                day text, \
                month text \
            )"
        )
        con.commit()
        con.close()

    def add_day_record(day, month):
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("INSERT INTO days VALUES (NULL, ?, ?)", (day, month))
        con.commit()
        con.close()

    def query_days():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM days")
        records = cur.fetchall()
        con.close()
        return records

    def delete_days_records():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("DELETE FROM days")
        con.commit()
        con.close()

    create_days_table()

class attendance_database():
    def create_attendances_table():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS attendances ( \
                id INTEGER PRIMARY KEY, \
                day_id INTEGER NOT NULL, \
                student_id INTEGER NOT NULL, \
                FOREIGN KEY(day_id) REFERENCES days(id), \
                FOREIGN KEY(student_id) REFERENCES students(id) \
            )"
        )
        con.commit()
        con.close()
    
    def add_attendance_record(day, student):
        con = sqlite3.connect('horus.db')
        con.execute("PRAGMA foreign_keys = ON")
        cur = con.cursor()
        cur.execute("INSERT INTO attendances(id, day_id, student_id) VALUES (NULL, ?, ?)", (day, student))
        con.commit()
        con.close()
    
    def query_foreign_keys():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM attendances")
        records = cur.fetchall()
        con.close()
        return records

    def query_attendances():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("SELECT students.*, days.* FROM students JOIN attendances ON students.id = attendances.student_id JOIN days ON days.id = attendances.day_id")
        records = cur.fetchall()
        con.close()
        return records

    def query_attendance_by_id(id):
        con = sqlite3.connect('horus.db')
        con.execute("PRAGMA foreign_keys = ON")
        cur = con.cursor()
        cur.execute("SELECT students.*, days.* FROM students JOIN attendances ON students.id = attendances.student_id JOIN days ON days.id = attendances.day_id WHERE attendances.id = ?", (id, ))
        attendance = cur.fetchone()
        con.close()
        return attendance
    
    def delete_attendances_records():
        con = sqlite3.connect('horus.db')
        cur = con.cursor()
        cur.execute("DELETE FROM attendances")
        con.commit()
        con.close()
    
    create_attendances_table()