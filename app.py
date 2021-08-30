from tkinter import *
from tkinter import messagebox
from main import Home
import dbhelper


class SMS(Home):
    def __init__(self):
        self.methods = {
            "loginHandler": self.loginHandler,
            "editHandler": self.editHandler,
            "anncHandler": self.anncHandler,
            "viewStdHandler": self.viewStdHandler,
            "addStudentHandler": self.addStudentHandler,
            "fetchSubjects": self.fetchSubjects,
            "delStdHandler": self.delStdHandler,
            "updateStudentHandler": self.updateStudentHandler,
            "updateStdHandler": self.updateStdHandler,
            "updateStdDetailsHandler": self.updateStdDetailsHandler,
            "updateMarksHandler": self.updateMarksHandler
        }
        self._dbObject = dbhelper.DB()
        super().__init__(self.methods)

    def loginHandler(self, person, firstInput, password):
        print('login')
        if person == "admin":
            self.adminResponse = self._dbObject.search("Admin", "email", firstInput, "password", password, "LIKE")
            # print(self.adminResponse)
            self.anncHandler("get", "")      # ..........................+++++++++++++++++++++.........................

            if len(self.adminResponse) > 0:
                self.adminWindow(self.methods)
            else:
                messagebox.showerror("Login failed!", "You have entered invalid login credentials")
        else:
            self.studentResponse = self._dbObject.search("Student", "rollNo", firstInput, "password", password, "LIKE")

            if len(self.studentResponse) > 0:
                student = {
                    'rollNo': self.studentResponse[0][2],
                    'name': self.studentResponse[0][1],
                    'email': self.studentResponse[0][3],
                    'password': self.studentResponse[0][4],
                    'year': self.studentResponse[0][5],
                    'stream': self.studentResponse[0][7],
                    'sem': self.studentResponse[0][8],
                    'mark1': self.studentResponse[0][9],
                    'mark2': self.studentResponse[0][10],
                    'mark3': self.studentResponse[0][11],
                    'mark4': self.studentResponse[0][12],
                    'mark5': self.studentResponse[0][13],
                    'sub1': self.studentResponse[1][0],
                    'sub2': self.studentResponse[1][1],
                    'sub3': self.studentResponse[1][2],
                    'sub4': self.studentResponse[1][3],
                    'sub5': self.studentResponse[1][4]
                }
                self.studentWindow(student, self.methods)
            else:
                messagebox.showerror("Login failed!", "You have entered invalid login credentials")
                print("login failed")

    def viewStdHandler(self, rollNumber):
        if rollNumber.strip() == "" or not(rollNumber.isnumeric()):
            messagebox.showerror("Invalid Entry!", "Please enter a valid Roll Number")
        else:
            rollNumber = int(rollNumber)
            stdDetails = self._dbObject.search("Student", "rollNo", rollNumber, "sID", "-1", "NOT LIKE")
            if len(stdDetails) == 2:
                self.studentDetailsWindow(self.methods, stdDetails[0], stdDetails[1])
            else:
                messagebox.showerror("Search Failed!", "No such student found!!!\nPlease enter a valid Roll Number")

    def delStdHandler(self, rollNumber):
        if rollNumber.strip() == "" or not (rollNumber.isnumeric()):
            messagebox.showerror("Invalid Entry!", "Please enter a valid Roll Number")
        else:
            rollNumber = int(rollNumber)
            response = self._dbObject.search("Student", "rollNo", rollNumber, "sID", "-1", "NOT LIKE")
            if len(response) == 2:
                isDelete = messagebox.askquestion("Delete Student Details", "Are you sure you want to permanently "
                                                                            "delete all details of "+response[0][1]+"?")
                if isDelete == "yes":
                    self._dbObject.delete("Student", "rollNo", rollNumber)
                    messagebox.showinfo("Delete successful!", "The details of "+response[0][1]+" (Roll no.-"+str(response[0][2])
                                        + ") have been deleted successfully")
            else:
                messagebox.showerror("Search Failed!", "No such student found!!!\nPlease enter a valid Roll Number")

    def updateStdHandler(self, rollNumber):
        if rollNumber.strip() == "" or not (rollNumber.isnumeric()):
            messagebox.showerror("Invalid Entry!", "Please enter a valid Roll Number")
        else:
            rollNumber = int(rollNumber)
            stdDetails = self._dbObject.search("Student", "rollNo", rollNumber, "sID", "-1", "NOT LIKE")
            if len(stdDetails) == 2:
                self.updateStudentDetailsWindow(self.methods, stdDetails[0])
            else:
                messagebox.showerror("Search Failed!", "No such student found!!!\nPlease enter a valid Roll Number")

    def updateStdDetailsHandler(self, preStdDetails, email, stream, year, sem):
        changeMarks = True
        year = int(year)
        sem = int(sem)
        rollNumber = preStdDetails[2]
        if preStdDetails[3] == email and preStdDetails[7] == stream and preStdDetails[8] == sem:
            changeMarks = False
        else:
            if preStdDetails[7] != stream or preStdDetails[8] != sem:
                changeMarks = True
            else:
                changeMarks = False
            self._dbObject.updateStudentDetails(email, stream, year, sem, rollNumber)
        stdResponse = self._dbObject.search("Student", "rollNo", rollNumber, "sID", "-1", "NOT LIKE")
        self.updateStudentMarksWindow(self.methods, stdResponse[0], stdResponse[1], changeMarks)

    def updateMarksHandler(self, rollNumber, mark1, mark2, mark3, mark4, mark5):
        if mark1 == "" or mark2 == "" or mark3 == "" or mark4 == "" or mark5 == "":
            messagebox.showerror("Error!", "All fields have to be filled with valid inputs")
        elif mark1.isnumeric() and mark2.isnumeric() and mark3.isnumeric() and mark4.isnumeric() and mark5.isnumeric():
            mark1 = int(mark1)
            mark2 = int(mark2)
            mark3 = int(mark3)
            mark4 = int(mark4)
            mark5 = int(mark5)
            if mark1 in range(0, 101) and mark2 in range(0, 101) and mark3 in range(0, 101) and mark4 in range(0, 101) and mark5 in range(0, 101):
                self._dbObject.updateMarks(rollNumber, mark1, mark2, mark3, mark4, mark5)
                messagebox.showinfo("Marks updated!", "Marks have been updated successfully")
                self.updateStudentWindow(self.methods)
            else:
                messagebox.showerror("Error!", "Marks should be an integer between 0 and 100!!!")
        else:
            messagebox.showerror("Error!", "Marks should be an integer between 0 and 100!!!")

    def anncHandler(self, type, anncStr):
        if type == "get":
            response = self._dbObject.selectAnnouncements()
            if response == None:
                messagebox.showerror("Connection Failed", "Failed to Connect to the Database!!!")
            print(response)
            return response
        elif type == "insert":
            if anncStr.strip() == "":
                messagebox.showerror("", "Announcement cannot be blank")
            else:
                response = self._dbObject.search("announcement", "aName", anncStr, "aID", "-1", "NOT LIKE")
                if len(response) == 0:
                    self._dbObject.insertAnnouncement(anncStr)
                    messagebox.showinfo("Announcement Added", "Announcement has been added successfully")
                    self.anncInput.delete("1.0", END)
                else:
                    messagebox.showerror("", "This announcement is already in the announcement list")
        elif type == "delete":
            isDelete = messagebox.askquestion("Delete Announcement",
                                              "Are you sure you want to permanently delete this announcement?")
            if isDelete == "yes":
                self._dbObject.delete("Announcement", "aName", anncStr)
                self.removeAnncWindow(self.methods)

    def editHandler(self, type, firstInput, password, secondInput):
        if type == "email":
            oldEmail = firstInput
            newEmail = secondInput
        elif type == "password":
            oldEmail = self.adminResponse[0][0]
            newPassword = secondInput

        response = self._dbObject.search("Admin", "email", oldEmail, "password", password, "LIKE")

        if type == "email":
            if len(response) > 0:
                self._dbObject.updateAdmin("Admin", "email", newEmail)
                self.adminResponse = self._dbObject.search("Admin", "email", newEmail, "password", password, "LIKE")
                messagebox.showinfo("Email Updated!", "Your email-id has been updated successfully")
                self.editProfileWindow(self.methods)
            else:
                messagebox.showerror("Update Failed!", "Failed to update your email-id")
        elif type == "password":
            if len(secondInput) < 6:
                messagebox.showinfo("", "* Password must be at least 6 characters long")
            elif len(response) > 0:
                self._dbObject.updateAdmin("Admin", "password", newPassword)
                messagebox.showinfo("Password Updated!", "Your password has been updated successfully")
                self.editProfileWindow(self.methods)
            else:
                print(response)
                messagebox.showerror("Update Failed!", "Failed to update your password")

    def addStudentHandler(self, details, m1, m2, m3, m4, m5):
        if m1 == "" or m2 == "" or m3 == "" or m4 == "" or m5 == "":
            messagebox.showerror("Error!", "All fields have to be filled")
        else:
            subjectTuple = self._dbObject.search("subject", "stream",details["stream"],"sem",details["sem"],"LIKE")
            subjectID = subjectTuple[0][0]
            print("subject ID = ",subjectID)
            self._dbObject.insertStudent(details,m1,m2,m3,m4,m5,subjectID)
            messagebox.showinfo("Success!", "Student added successfully")

    def fetchSubjects(self, sem, stream):
        subjectTuple = self._dbObject.search("subject", "stream", stream, "sem", sem, "LIKE")
        if len(subjectTuple) != 0:
            print(subjectTuple)

        subjects = {
            "sub1": subjectTuple[0][3],
            "sub2": subjectTuple[0][4],
            "sub3": subjectTuple[0][5],
            "sub4": subjectTuple[0][6],
            "sub5": subjectTuple[0][7]
        }
        return subjects

    def updateStudentHandler(self, email, oldPass, newPass, student):
        roll = student['rollNo']
        if email == '' or oldPass == '' or newPass == '':
            messagebox.showerror("Error!", "All fields have to be filled")
        elif oldPass != student['password']:
            messagebox.showerror("Error!", "Incorrect old password")
        else:
            self._dbObject.updateStudent(roll, email, newPass)
            messagebox.showinfo("Update successful!", "Your details have been updated")
            self.loginWindow("student", self.methods)


if __name__ == "__main__":
    stdMngSys = SMS()
