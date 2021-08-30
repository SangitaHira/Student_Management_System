import mysql.connector


class DB:
    def __init__(self):
        # This constructor is used to connect with the student_management_system database
        try:
            self._connection = mysql.connector.connect(host="127.0.0.1", user="root", password="",
                                                       database="student_management_system")
            self._mycursor = self._connection.cursor()
            print("Database connected successfully...")
        except:
            print("Failed to connect to the database!!!")

    def search(self, table, key1, value1, key2, value2, type2):
        self._mycursor.execute("SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` {} '{}'".format(table, key1, value1,
                                                                                                 key2, type2, value2))
        response = self._mycursor.fetchall()
        if table == "Student" and key1 == "rollNo" and len(response) > 0:
            self._mycursor.execute("SELECT `sub1`,`sub2`,`sub3`,`sub4`,`sub5` FROM `subject` WHERE `subjectID` = "
                                   "(SELECT `subjectID` FROM `student` WHERE `rollNo` = {})".format(value1))
            response2 = self._mycursor.fetchone()
            response.append(response2)
        return response

    def selectAnnouncements(self):
        try:
            self._mycursor.execute("SELECT * FROM `announcement`")
            response = self._mycursor.fetchall()
            return response
        except:
            print("Failed to show announcements!!")
            return None

    def insertAnnouncement(self, anncStr):
        self._mycursor.execute("INSERT INTO `announcement`(`aName`) VALUES ('{}')".format(anncStr))
        self._connection.commit()

    def delete(self, table, key, value):
        self._mycursor.execute("DELETE FROM `{}` WHERE `{}` LIKE '{}'".format(table, key, value))
        self._connection.commit()

    def insertStudent(self, details, m1, m2, m3, m4, m5, subjectID):
        self._mycursor.execute("INSERT INTO `student` (`sID`, `sName`, `rollNo`, `email`, `password`, `year`, `subjectID`, `stream`, `sem`, `sMark1`, `sMark2`, `sMark3`, `sMark4`, `sMark5`) "
                               "VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(details["name"],details["roll"],details["email"],
                                                                                                                                    details["roll"],details["year"],subjectID,
                                                                                                                                    details["stream"],details["sem"],
                                                                                                                                    m1,m2,m3,m4,m5))
        self._connection.commit()

    def updateAdmin(self, table, key, value):
        self._mycursor.execute("UPDATE `{}` SET `{}` = '{}'".format(table, key, value))
        self._connection.commit()

    def updateStudent(self, roll, email, password):
        self._mycursor.execute(
            "UPDATE student SET email = '{}', password = '{}' WHERE student.rollNo = {}".format(email, password, roll))
        self._connection.commit()

    def updateStudentDetails(self, email, stream, year, sem, rollNo):
        self._mycursor.execute("UPDATE student SET email = '{}', stream = '{}', year = '{}', sem = '{}', "
                               "subjectID = (SELECT subjectID FROM `subject` WHERE stream = '{}' AND sem = '{}') "
                               "WHERE rollNo = {}".format(email, stream, year, sem, stream, sem, rollNo))
        self._connection.commit()

    def updateMarks(self, rollNo, mark1, mark2, mark3, mark4, mark5):
        self._mycursor.execute("UPDATE student SET sMark1 = {}, sMark2 = {}, sMark3 = {}, sMark4 = {}, sMark5 = {} "
                               "WHERE rollNo = {}".format(mark1, mark2, mark3, mark4, mark5, rollNo))
        self._connection.commit()
