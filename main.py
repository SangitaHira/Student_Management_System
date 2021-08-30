from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import time


class Home:
    def __init__(self, methods):
        self.root = Tk()
        self.root.iconbitmap("icons/main_icon.ico")
        self.root.title("Student Management System")
        self.root.minsize(1200, 800)
        self.root.resizable(False, False)
        self.root.geometry('+360+110')

        # Adding a background image
        self.backgroundImage = Image.open("images/background.png")
        self.backgroundImage = self.backgroundImage.resize((1200, 800))
        self.backgroundImage = ImageTk.PhotoImage(self.backgroundImage)

        self.canvas1 = Canvas(self.root)
        self.canvas1.create_image(0, 0, image=self.backgroundImage, anchor="nw")
        self.canvas1.config(bg="white", width=1200, height=800)

        # Texts for Date and Time
        self.clockText = self.canvas1.create_text(1105, 30, text="time", font=("Times", 22, "bold"), fill="white")
        self.dateText = self.canvas1.create_text(1105, 60, text="date", font=("Times", 13, "bold"), fill="white")
        self.tick()
        self.canvas1.pack(expand=True, fill=BOTH)

        self.heading = None
        self.heading2 = None
        self.canvasText = []
        self.animation = None
        self.drawBox = None

        self.homeWindow(methods)

        self.root.mainloop()

    def clearCanvas(self):
        self.canvas1.delete(self.heading)
        self.canvas1.delete(self.heading2)
        self.canvas1.delete(self.drawBox)
        for text in self.canvasText:
            self.canvas1.delete(text)

    def clearWindow(self):
        for widget in self.root.pack_slaves():
            if widget != self.canvas1:
                widget.destroy()

        for widget in self.root.place_slaves():
            widget.destroy()

    def tick(self):         # Function which automatically updates Time and Date
        self.time_string = time.strftime("%I:%M:%S %p")
        self.date_string = time.strftime("%a, %d %B %Y")
        self.canvas1.delete(self.clockText)
        self.canvas1.delete(self.dateText)
        self.clockText = self.canvas1.create_text(1105, 30, text=self.time_string, font=("Times", 22, "bold"),
                                                  fill="white")
        self.dateText = self.canvas1.create_text(1105, 60, text=self.date_string, font=("Times", 13, "bold"),
                                                 fill="white")
        self.canvas1.after(500, self.tick)

    def animateHeading(self):
        if self.index >= len(self.headingText):
            self.text = ""
            self.index = 0
        else:
            self.text += self.headingText[self.index]
            self.index += 1
        self.canvas1.delete(self.heading2)
        self.heading2 = self.canvas1.create_text(600, 150, text=self.text, font=("Times", 40, "bold"), fill="white")
        self.animation = self.canvas1.after(150, self.animateHeading)

    def homeWindow(self, methods):         # Function for displaying home window elements
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(620, 80, text="Welcome to", font=("Times", 40, "bold"), fill="white")
        self.headingText = "Student Management System"
        self.index = 0
        self.text = ""
        self.heading2 = self.canvas1.create_text(600, 150, text="", font=("Times", 40, "bold"), fill="white")
        self.animateHeading()

        self.admLoginBtn = Button(self.root, text="ADMIN LOGIN", font=("Arial", 22, 'bold'), bg='#FFBB00', fg='white',
                                  command=lambda: self.loginWindow("admin", methods))
        self.admLoginBtn.place(relx=0.3, rely=0.32, relwidth=0.4, relheight=0.08)

        self.stdLoginBtn = Button(self.root, text="STUDENT LOGIN", font=("Arial", 22, 'bold'), bg='#FFBB00', fg='white',
                                  command=lambda: self.loginWindow("student", methods))
        self.stdLoginBtn.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.08)

        # Frame for Announcements
        self.frame1 = Frame(self.root, bg="#FFBB00", bd=3)
        self.frame1.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.25)

        self.frame2 = Frame(self.frame1, bg='#FFD86B')
        self.frame2.place(relx=0.007, rely=0.015, relwidth=0.985, relheight=0.97)

        self.labelAnncHead = Label(self.frame2, text="LATEST ANNOUNCEMENTS", bg='#FFD86B', fg="red",
                                   font=('Arial', 16, 'bold'))
        self.labelAnncHead.pack(pady=10)

        self.scrollBar = ttk.Scrollbar(self.frame1, orient="vertical")
        self.scrollBar.pack(side=RIGHT, fill="y")

        self.anncList = methods["anncHandler"]("get", "")   # ------ This list is getting announcements from the database ------ #
        if self.anncList == None:
            self.anncList = [[0, "Failed to show the Announcements due to Database Connection Problem!!!"]]
        elif len(self.anncList) == 0:
            self.anncList = [[0, "No Announcements!!!"]]

        self.anncText = Text(self.frame2, font=("Times", 14), yscrollcommand=self.scrollBar.set, bg="#FFD86B", bd=0,
                             width=75)

        for i in range(len(self.anncList)-1, -1, -1):
            self.anncText.insert(END, " \u2055 " + self.anncList[i][1] + "\n")
        self.anncText.configure(state="disabled")
        self.anncText.pack(side=TOP)
        self.scrollBar.config(command=self.anncText.yview)

    def loginWindow(self, person, methods):
        self.clearWindow()
        self.clearCanvas()
        self.canvas1.after_cancel(self.animation)

        if person == "admin":
            self.heading = self.canvas1.create_text(600, 130, text='ADMIN LOGIN ', font=("Times", 40, "bold"),
                                                    fill="white")
        else:
            self.heading = self.canvas1.create_text(600, 130, text='STUDENT LOGIN ', font=("Times", 40, "bold"),
                                                    fill="white")

        frame1 = Frame(self.root, bg="#FFD86B")
        frame1.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.5)

        if person == "admin":
            self.labelEntEmail = Label(frame1, text="Enter your Email-id", bg="#FFD86B", fg="#00005D", anchor=W,
                                       font=('Arial', 18, 'bold'))
            self.labelEntEmail.place(relx=0.2, rely=0.2, relwidth=0.6)

            self.emailInput = Entry(frame1, bg='white', fg='black', font=('Arial', 18, 'bold'))
            self.emailInput.place(relx=0.2, rely=0.3, relwidth=0.6)
        else:
            self.labelEntRoll = Label(frame1, text="Enter your Roll Number", bg="#FFD86B", fg="#00005D", anchor=W,
                                      font=('Arial', 18, 'bold'))
            self.labelEntRoll.place(relx=0.2, rely=0.2, relwidth=0.6)

            self.rollInput = Entry(frame1, bg='white', fg='black', font=('Arial', 18, 'bold'))
            self.rollInput.place(relx=0.2, rely=0.3, relwidth=0.6)

        self.labelEntPass = Label(frame1, text="Enter your Password", bg="#FFD86B", fg="#00005D", anchor=W,
                                  font=('Arial', 18, 'bold'))
        self.labelEntPass.place(relx=0.2, rely=0.45, relwidth=0.6)

        self.passwordInput = Entry(frame1, bg='white', fg='black', font=('Arial', 18, 'bold'), show="\u2022")
        self.passwordInput.place(relx=0.2, rely=0.55, relwidth=0.6)

        self.loginBtn = Button(frame1, text="LOGIN", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'))
        if person == "admin":
            self.loginBtn.configure(command=lambda: methods["loginHandler"](person, self.emailInput.get(), self.passwordInput.get()))
        else:
            self.loginBtn.configure(command=lambda: methods["loginHandler"](person, self.rollInput.get(), self.passwordInput.get()))
        self.loginBtn.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.1)

        self.backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                              command=lambda: self.homeWindow(methods))
        self.backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def adminWindow(self, methods):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(615, 80, text="Welcome ADMIN", font=("Times", 40, "bold"), fill="white")

        addStdBtn = Button(self.root, text="ADD STUDENT", bg='#FFBB00', fg='white', font=("Arial Bold", 16),
                           command=lambda: self.addStudentWindow(methods))
        addStdBtn.place(relx=0.15, rely=0.25, relwidth=0.3, relheight=0.08)

        viewStdBtn = Button(self.root, text="VIEW STUDENT", bg='#FFBB00', fg='white', font=("Arial Bold", 16),
                            command=lambda: self.viewStudentWindow(methods))
        viewStdBtn.place(relx=0.55, rely=0.25, relwidth=0.3, relheight=0.08)

        delStdBtn = Button(self.root, text="DELETE STUDENT", bg='#FFBB00', fg='white', font=("Arial Bold", 16),
                           command=lambda: self.delStudentWindow(methods))
        delStdBtn.place(relx=0.15, rely=0.4, relwidth=0.3, relheight=0.08)

        updateStdBtn = Button(self.root, text="UPDATE STUDENT", bg='#FFBB00', fg='white', font=("Arial Bold", 16),
                              command=lambda: self.updateStudentWindow(methods))
        updateStdBtn.place(relx=0.55, rely=0.4, relwidth=0.3, relheight=0.08)

        addAnncBtn = Button(self.root, text="ADD ANNOUNCEMENT", bg='#FFBB00', fg='white', font=("Arial Bold", 16),
                            command=lambda: self.addAnncWindow(methods))
        addAnncBtn.place(relx=0.15, rely=0.55, relwidth=0.3, relheight=0.08)

        removeAnncBtn = Button(self.root, text="REMOVE ANNOUNCEMENT", bg='#FFBB00', fg='white', font=("Arial Bold", 16),
                               command=lambda: self.removeAnncWindow(methods))
        removeAnncBtn.place(relx=0.55, rely=0.55, relwidth=0.3, relheight=0.08)

        editProfileBtn = Button(self.root, text="EDIT PROFILE", bg='#FFBB00', fg='white', font=("Arial Bold", 16),
                                command=lambda: self.editProfileWindow(methods))
        editProfileBtn.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.08)

        # logoutImg = PhotoImage(file="images/main_icon.png", master=self.root)
        btnAdmLogout = Button(self.root, text="LOGOUT", bg='#FFBB00', fg='white', font=("Arial Bold", 16),
                              command=lambda: self.loginWindow("admin", methods), compound=RIGHT)
        btnAdmLogout.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.08)

        print('Admin')

    def semClick(self, event):
        if self.yearInput.get() == '1' or self.yearInput.get() == '2' or self.yearInput.get() == '3' or self.yearInput.get() == '4':
            event.widget.config(values=(2 * int(self.yearInput.get()) - 1, 2 * int(self.yearInput.get())))
        else:
            messagebox.showerror("Year not selected!", "Select year first")

    def addStudentWindow(self, methods):
        self.clearWindow()
        self.clearCanvas()
        self.heading = self.canvas1.create_text(600, 130, text='ADD STUDENT', font=("Times", 40, "bold"), fill="white")

        self.canvasText.append(self.canvas1.create_text(320, 250, text="Enter Roll Number", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 300, text="Enter Name", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 350, text="Enter Email id", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 400, text="Enter Stream", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 450, text="Enter Year", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 500, text="Enter Semester", fill="white", font=('Times', 18, 'bold'), anchor="nw"))

        self.rollInput = Entry(self.root, font=('Arial', 16, 'bold'))
        self.rollInput.place(relx=0.45, rely=0.305, relwidth=0.25, relheight=0.04)

        self.nameInput = Entry(self.root, font=('Arial', 16, 'bold'))
        self.nameInput.place(relx=0.45, rely=0.37, relwidth=0.25, relheight=0.04)

        self.emailInput = Entry(self.root, font=('Arial', 16, 'bold'))
        self.emailInput.place(relx=0.45, rely=0.43, relwidth=0.25, relheight=0.04)

        self.streamInput = ttk.Combobox(self.root, values=("Computer Science & Engineering", "Information Technology"), font=('Arial', 16, 'bold'))
        self.streamInput.place(relx=0.45, rely=0.495, relwidth=0.25, relheight=0.04)

        self.yearInput = ttk.Combobox(self.root, values=(1, 2, 3, 4), font=('Arial', 16, 'bold'))
        self.yearInput.place(relx=0.45, rely=0.557, relwidth=0.25, relheight=0.04)

        self.semInput = ttk.Combobox(self.root, font=('Arial', 16, 'bold'))
        self.semInput.place(relx=0.45, rely=0.62, relwidth=0.25, relheight=0.04)
        self.semInput.bind("<Button-1>", self.semClick)

        btnAddSubMarks = Button(self.root, text="ADD SUBJECT\nMARKS", bg="black", fg='white',
                                font=("Arial", 18, 'bold'), relief=RIDGE,
                                command=lambda: self.addSubMarksWindow(self.rollInput.get(), self.nameInput.get(),
                                                                       self.emailInput.get(), self.streamInput.get(),
                                                                       self.yearInput.get(), self.semInput.get(),
                                                                       methods))
        btnAddSubMarks.place(relx=0.41, rely=0.75, relwidth=0.18, relheight=0.085)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.adminWindow(methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def addSubMarksWindow(self, roll, name, email, stream, year, sem, methods):
        if roll == "" or name == "" or email == "" or stream == "" or year == "" or sem == "":
            messagebox.showerror("Error!", "All the fields need to be filled")
        else:
            self.clearWindow()
            self.clearCanvas()

            subjects = methods["fetchSubjects"](sem, stream)
            print(subjects)
            details = {
                "roll": roll,
                "name": name,
                "email": email,
                "stream": stream,
                "year": year,
                "sem": sem
            }

            self.canvasText.append(self.canvas1.create_text(600, 120, text='ADD SUBJECT MARKS', font=("Times", 40, "bold"), fill="white"))
            self.canvasText.append(self.canvas1.create_text(120, 180, text="STUDENT NAME:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(330, 180, text=name, fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(120, 220, text="ROLL NUMBER:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(320, 220, text=roll, fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(700, 180, text="STREAM:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(820, 180, text=stream, fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(700, 220, text="SEMESTER:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(850, 220, text=sem, fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(120, 300, text="ENTER THE MARKS OBTAINED:", fill="white", font=('Times', 20, 'bold'),
                                   anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(150, 375, text=subjects["sub1"], fill="white", anchor="nw", font=('Times', 18, 'bold')))
            self.canvasText.append(self.canvas1.create_text(150, 425, text=subjects["sub2"], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(150, 475, text=subjects["sub3"], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(150, 525, text=subjects["sub4"], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(self.canvas1.create_text(150, 575, text=subjects["sub5"], fill="white", anchor="nw", font=('Times', 18, 'bold')))

            self.mark1Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
            self.mark1Input.place(relx=0.70, rely=0.465, relwidth=0.06, relheight=0.04)
            self.mark2Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
            self.mark2Input.place(relx=0.70, rely=0.528, relwidth=0.06, relheight=0.04)
            self.mark3Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
            self.mark3Input.place(relx=0.70, rely=0.591, relwidth=0.06, relheight=0.04)
            self.mark4Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
            self.mark4Input.place(relx=0.70, rely=0.654, relwidth=0.06, relheight=0.04)
            self.mark5Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
            self.mark5Input.place(relx=0.70, rely=0.715, relwidth=0.06, relheight=0.04)

            self.canvasText.append(
                self.canvas1.create_text(920, 375, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(
                self.canvas1.create_text(920, 425, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(
                self.canvas1.create_text(920, 475, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(
                self.canvas1.create_text(920, 525, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
            self.canvasText.append(
                self.canvas1.create_text(920, 575, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))

            btnSubmit = Button(self.root, text="SUBMIT", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                               command=lambda: methods["addStudentHandler"](details, self.mark1Input.get(),
                                                                            self.mark2Input.get(),
                                                                            self.mark3Input.get(),
                                                                            self.mark4Input.get(),
                                                                            self.mark5Input.get()))
            btnSubmit.place(relx=0.44, rely=0.8, relwidth=0.12, relheight=0.05)

            backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                             command=lambda: self.addStudentWindow(methods))
            backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def viewStudentWindow(self, methods):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 130, text='VIEW STUDENT', font=("Times", 40, "bold"), fill="white")

        frame1 = Frame(self.root, bg="#FFD86B")
        frame1.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.5)

        labelEntRoll = Label(frame1, text="Enter Roll Number", bg='#FFD86B', fg='#00005D', font=('Arial', 22, 'bold'),
                             anchor=W)
        labelEntRoll.place(relx=0.2, rely=0.25, relwidth=0.6)

        rollInput = Entry(frame1, bg='white', fg='black', font=('Arial', 18, 'bold'))
        rollInput.place(relx=0.2, rely=0.36, relwidth=0.6)

        viewBtn = Button(frame1, text="VIEW", bg="#FFBB00", fg="white", font=('Arial', 18, 'bold'),
                         command=lambda: methods["viewStdHandler"](rollInput.get()))
        viewBtn.place(relx=0.2, rely=0.54, relwidth=0.6, relheight=0.1)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.adminWindow(methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def studentDetailsWindow(self, methods, stdDetails, subjects):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 80, text='STUDENT DETAILS', font=("Times", 35, "bold"),
                                                fill="white")

        rollInput = Entry(self.root, bg='white', fg='grey', font=('Times', 15))
        rollInput.place(relx=0.32, rely=0.17, relwidth=0.25, relheight=0.04)
        rollInput.insert(0, "Enter Roll Number here")

        def clearPlaceHolder(event):
            event.widget.delete(0, END)
            event.widget.config(fg='black')

        rollInput.bind("<FocusIn>", clearPlaceHolder)
        searchBtn = Button(self.root, text="Search", font=('Arial', 15, 'bold'), bg="#FFBB00", fg="white",
                           command=lambda: methods["viewStdHandler"](rollInput.get()))
        searchBtn.place(relx=0.575, rely=0.17, relwidth=0.1, relheight=0.042)

        self.canvasText.append(self.canvas1.create_text(120, 200, text="STUDENT NAME:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(330, 200, text=stdDetails[1], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(120, 240, text="ROLL NUMBER:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 240, text=stdDetails[2], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(120, 280, text="EMAIL:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(220, 280, text=stdDetails[3], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(700, 200, text="STREAM:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(820, 200, text=stdDetails[7], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(700, 240, text="YEAR:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(785, 240, text=stdDetails[5], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(700, 280, text="SEMESTER:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(850, 280, text=stdDetails[8], fill="white", font=('Times', 18, 'bold'), anchor="nw"))

        marks = stdDetails[9:]
        percent = (marks[0] + marks[1] + marks[2] + marks[3] + marks[4]) / 5
        if marks[0] >= 40 and marks[1] >= 40 and marks[2] >= 40 and marks[3] >= 40 and marks[4] >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        # Table for visualizing the Marks with the corresponding Subjects
        Label(self.root, text="SUBJECT NAME", font=('Times', 22, 'bold'), bg="#FFBB00").place(relx=0.11, rely=0.45,
                                                                                              relwidth=0.53,
                                                                                              relheight=0.06)
        Label(self.root, text="MARKS OUT OF 100", font=('Times', 22, 'bold'), bg="#FFBB00").place(relx=0.643, rely=0.45,
                                                                                                  relwidth=0.25,
                                                                                                  relheight=0.06)
        for row in range(5):
            l1 = Label(self.root, text=subjects[row], font=('Times', 18, 'bold'), bg="#FFECB7", anchor=W)
            l2 = Label(self.root, text=marks[row], font=('Times', 18, 'bold'), bg="#FFECB7")
            if row % 2 == 1:
                l1.config(bg="#FFDC7B")
                l2.config(bg="#FFDC7B")
            l1.place(relx=0.11, rely=0.51 + 0.05 * row, relwidth=0.53, relheight=0.05)
            l2.place(relx=0.643, rely=0.51 + 0.05 * row, relwidth=0.25, relheight=0.05)

        Label(self.root, text="Percentage = " + str(percent) + "%", font=('Times', 18, 'bold'), bg="#FFDC7B",
              anchor=W).place(relx=0.11, rely=0.765, relwidth=0.39, relheight=0.05)
        Label(self.root, text="Result : " + result, font=('Times', 18, 'bold'), bg="#FFDC7B",
              anchor=W).place(relx=0.503, rely=0.765, relwidth=0.39, relheight=0.05)
        # End of the Table

        closeBtn = Button(self.root, text="CLOSE", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                          command=lambda: self.adminWindow(methods))
        closeBtn.place(relx=0.45, rely=0.9, relwidth=0.1, relheight=0.05)

    def delStudentWindow(self, methods):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 130, text='DELETE STUDENT', font=("Times", 40, "bold"), fill="white")

        frame1 = Frame(self.root, bg="#FFD86B")
        frame1.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.5)

        labelEntRoll = Label(frame1, text="Enter Roll Number", bg='#FFD86B', fg='#00005D', font=('Arial', 22, 'bold'),
                             anchor=W)
        labelEntRoll.place(relx=0.2, rely=0.25, relwidth=0.6)

        rollInput = Entry(frame1, bg='white', fg='black', font=('Arial', 18, 'bold'))
        rollInput.place(relx=0.2, rely=0.36, relwidth=0.6)

        delBtn = Button(frame1, text="DELETE", bg="#FFBB00", fg="white", font=('Arial', 18, 'bold'),
                        command=lambda: methods["delStdHandler"](rollInput.get()))
        delBtn.place(relx=0.2, rely=0.54, relwidth=0.6, relheight=0.1)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.adminWindow(methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def updateStudentWindow(self, methods):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 130, text='UPDATE STUDENT', font=("Times", 40, "bold"),
                                                fill="white")

        frame1 = Frame(self.root, bg="#FFD86B")
        frame1.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.5)

        labelEntRoll = Label(frame1, text="Enter Roll Number", bg='#FFD86B', fg='#00005D', font=('Arial', 22, 'bold'),
                             anchor=W)
        labelEntRoll.place(relx=0.2, rely=0.25, relwidth=0.6)

        rollInput = Entry(frame1, bg='white', fg='black', font=('Arial', 18, 'bold'))
        rollInput.place(relx=0.2, rely=0.36, relwidth=0.6)

        goBtn = Button(frame1, text="GO", bg="#FFBB00", fg="white", font=('Arial', 18, 'bold'),
                           command=lambda: methods["updateStdHandler"](rollInput.get()))
        goBtn.place(relx=0.2, rely=0.54, relwidth=0.6, relheight=0.1)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.adminWindow(methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def updateStudentDetailsWindow(self, methods, stdDetails):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 80, text='UPDATE STUDENT DETAILS', font=("Times", 35, "bold"),
                                                fill="white")
        self.canvasText.append(self.canvas1.create_text(320, 200, text="STUDENT NAME", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 250, text="ROLL NUMBER", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 300, text="EMAIL", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 350, text="STREAM", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 400, text="YEAR", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 450, text="SEMESTER", fill="white", font=('Times', 18, 'bold'), anchor="nw"))

        studNameInput = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
        studNameInput.place(relx=0.45, rely=0.24, relwidth=0.25, relheight=0.04)
        studNameInput.insert(0, stdDetails[1])
        studNameInput.config(state="disabled")

        rollInput = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
        rollInput.place(relx=0.45, rely=0.305, relwidth=0.25, relheight=0.04)
        rollInput.insert(0, stdDetails[2])
        rollInput.config(state="disabled")

        emailInput = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
        emailInput.place(relx=0.45, rely=0.37, relwidth=0.25, relheight=0.04)
        emailInput.insert(0, stdDetails[3])

        streamInput = ttk.Combobox(self.root, values=("Computer Science & Engineering", "Information Technology"),
                                   font=('Arial', 16, 'bold'))
        streamInput.current(["Computer Science & Engineering", "Information Technology"].index(stdDetails[7]))
        streamInput.place(relx=0.45, rely=0.43, relwidth=0.25, relheight=0.04)

        self.yearInput = ttk.Combobox(self.root, values=(1, 2, 3, 4), font=('Arial', 16, 'bold'))
        self.yearInput.current(stdDetails[5]-1)
        self.yearInput.place(relx=0.45, rely=0.495, relwidth=0.25, relheight=0.04)

        semInput = ttk.Combobox(self.root, text=stdDetails[8], values=(2 * int(self.yearInput.get()) - 1, 2 * int(self.yearInput.get())),
                                font=('Arial', 16, 'bold'))
        semInput.current(1 - stdDetails[8] % 2)
        semInput.place(relx=0.45, rely=0.56, relwidth=0.25, relheight=0.04)
        semInput.bind("<Button-1>", self.semClick)

        updateMarksBtn = Button(self.root, text="UPDATE\nSUBJECT MARKS", bg="#FFBB00", fg='white',
                                font=("Arial", 18, 'bold'), command=lambda: methods["updateStdDetailsHandler"](stdDetails, emailInput.get(),
                                                                                                               streamInput.get(),
                                                                                                               self.yearInput.get(),
                                                                                                               semInput.get()))
        updateMarksBtn.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.08)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.updateStudentWindow(methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def updateStudentMarksWindow(self, methods, stdDetails, subjects, changeMarks):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 80, text='UPDATE SUBJECT MARKS', font=("Times", 35, "bold"),
                                                fill="white")

        self.canvasText.append(self.canvas1.create_text(120, 180, text="STUDENT NAME:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(330, 180, text=stdDetails[1], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(120, 220, text="ROLL NUMBER:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(320, 220, text=stdDetails[2], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(700, 180, text="STREAM:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(820, 180, text=stdDetails[7], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(700, 220, text="SEMESTER:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(850, 220, text=stdDetails[8], fill="white", font=('Times', 18, 'bold'), anchor="nw"))

        self.canvasText.append(self.canvas1.create_text(120, 300, text="ENTER THE MARKS OBTAINED:", fill="white", font=('Times', 20, 'bold'),
                                                        anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(150, 375, text=subjects[0], fill="white", anchor="nw",font=('Times', 18, 'bold')))
        self.canvasText.append(self.canvas1.create_text(150, 425, text=subjects[1], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(150, 475, text=subjects[2], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(150, 525, text=subjects[3], fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(150, 575, text=subjects[4], fill="white", anchor="nw", font=('Times', 18, 'bold')))

        mark1Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
        mark1Input.place(relx=0.70, rely=0.465, relwidth=0.06, relheight=0.04)
        mark2Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
        mark2Input.place(relx=0.70, rely=0.528, relwidth=0.06, relheight=0.04)
        mark3Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
        mark3Input.place(relx=0.70, rely=0.591, relwidth=0.06, relheight=0.04)
        mark4Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
        mark4Input.place(relx=0.70, rely=0.654, relwidth=0.06, relheight=0.04)
        mark5Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="center")
        mark5Input.place(relx=0.70, rely=0.715, relwidth=0.06, relheight=0.04)

        if changeMarks == False:
            marks = stdDetails[9:]
            mark1Input.insert(0, marks[0])
            mark2Input.insert(0, marks[1])
            mark3Input.insert(0, marks[2])
            mark4Input.insert(0, marks[3])
            mark5Input.insert(0, marks[4])

        self.canvasText.append(self.canvas1.create_text(920, 375, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(920, 425, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(920, 475, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(920, 525, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(self.canvas1.create_text(920, 575, text="/ 100", fill="white", font=('Times', 18, 'bold'), anchor="nw"))

        updateBtn = Button(self.root, text="UPDATE", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                           command=lambda: methods["updateMarksHandler"](stdDetails[2], mark1Input.get(), mark2Input.get(),
                                                                         mark3Input.get(), mark4Input.get(), mark5Input.get()))
        updateBtn.place(relx=0.44, rely=0.8, relwidth=0.12, relheight=0.05)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.updateStudentDetailsWindow(methods, stdDetails))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def addAnncWindow(self, methods):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 130, text='ADD ANNOUNCEMENT', font=("Times", 40, "bold"),
                                                fill="white")

        self.anncInput = Text(self.root, bg='white', fg='black', font=('Arial', 18, 'bold'))
        self.anncInput.place(relx=0.25, rely=0.36, relwidth=0.5, relheight=0.2)

        addAnncBtn = Button(self.root, text="ADD ANNOUNCEMENT", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                            command=lambda: methods["anncHandler"]("insert", self.anncInput.get("1.0", END)))
        addAnncBtn.place(relx=0.35, rely=0.65, relwidth=0.3, relheight=0.055)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.adminWindow(methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def removeAnncWindow(self, methods):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 130, text='REMOVE ANNOUNCEMENT', font=("Times", 40, "bold"),
                                                fill="white")
        self.anncList = methods["anncHandler"]("get", "")

        def strShortner(string):
            return string[:45] + "..."

        cntLines = 1

        def breakString(string, label, frame):
            global cntLines
            if len(string) >= 50:
                index = 50  # Assuming standard
                while string[index] != ' ' and string[index] != '-' and string[index] != '\n':
                    index -= 1
                cntLines += 1
                if cntLines > 3:
                    label.config(height=cntLines)
                    frame.config(height=29 * cntLines - (cntLines - 3) * 2)
                newString = string[:index + 1] + "\n     " + breakString(string[index + 1:], label, frame)
                return newString
            else:
                return string

        def viewAndHideAnnc(type, anncStr, label, frame, btn):
            global cntLines
            if type == "show":
                cntLines = 1
                label.config(text=breakString(anncStr, label, frame))
                btn.config(text="VIEW LESS", command=lambda: viewAndHideAnnc("hide", anncStr, label, frame, btn))
                cntLines = 1
            elif type == "hide":
                label.config(text=strShortner(anncStr), height=3)
                frame.config(height=87)
                btn.config(text="VIEW MORE", command=lambda: viewAndHideAnnc("show", anncStr, label, frame, btn))

        frame1 = Frame(self.root, bg="#FFBB00")
        frame1.place(relx=0.16, rely=0.3, relwidth=0.68, relheight=0.5)

        canvas2 = Canvas(frame1)

        scrollbar = ttk.Scrollbar(frame1, orient="vertical", command=canvas2.yview)
        frame2 = Frame(canvas2, bg="#FFBB00")
        frame2.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))

        canvas2.create_window((0, 0), window=frame2, anchor="nw")
        canvas2.configure(yscrollcommand=scrollbar.set)

        lblAnncTxt = []
        frame_i = []
        btnView = []
        btnDelete = []
        for row in range(len(self.anncList)):
            lblAnncTxt.append(Label(frame2, font=('Times', 18), bg="#FFECB7", anchor="nw", justify="left", width=40,
                                    height=3))
            lblAnncTxt[row].config(text=strShortner(" " + str(row + 1) + ". " + self.anncList[row][1]))
            lblAnncTxt[row].grid(row=row, column=0)
            frame_i.append(Frame(frame2, bg="#FFECB7", width=260, height=87))
            frame_i[row].grid(row=row, column=1)

            if row % 2 == 1:
                lblAnncTxt[row].config(bg="#FFDC7B")
                frame_i[row].config(bg="#FFDC7B")

            btnView.append(Button(frame_i[row], text="VIEW MORE", font=('Times', 13, 'bold'), bg="#FFBB00", fg="white"))
            btnView[row].config(command=lambda row=row:
                                viewAndHideAnnc("show", " " + str(row + 1) + ". " + self.anncList[row][1],
                                                lblAnncTxt[row], frame_i[row], btnView[row]))
            btnView[row].place(relx=0.08, rely=0.3)
            btnDelete.append(Button(frame_i[row], text="DELETE", font=('Times', 13, 'bold'), bg="#FFBB00", fg="white"))
            btnDelete[row].config(command=lambda row=row: methods["anncHandler"]("delete", self.anncList[row][1]))
            btnDelete[row].place(relx=0.6, rely=0.3)

        canvas2.place(relx=0.006, rely=0.01, relwidth=0.967, relheight=0.98)
        scrollbar.pack(side="right", fill="y")

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.adminWindow(methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def editProfileWindow(self, methods):
        self.clearWindow()
        self.clearCanvas()

        self.oldEmailInput = Entry()
        self.newEmailInput = Entry()
        self.passwordInput = Entry()
        self.oldPasswordInput = Entry()
        self.newPasswordInput = Entry()

        self.heading = self.canvas1.create_text(600, 130, text='EDIT YOUR PROFILE', font=("Times", 40, "bold"),
                                                fill="white")

        self.drawBox = self.canvas1.create_line(200, 200, 980, 200, 980, 650, 200, 650, 200, 200, fill="#FFBB00", width=3)

        self.chngMailBtn = Button(self.root, text="Change Email-id", font=('Arial', 12, 'bold'), bg="#FFBB00",
                                  fg='white', relief=SUNKEN, command=lambda: self.editEmailWindow(methods))
        self.chngMailBtn.place(relx=0.19, rely=0.235, relwidth=0.13, relheight=0.04)

        self.chngPasswordBtn = Button(self.root, text="Change Password", font=('Arial', 12, 'bold'), bg="#FFBB00",
                                      fg='white', command=lambda: self.editPasswordWindow(methods))
        self.chngPasswordBtn.place(relx=0.315, rely=0.235, relwidth=0.13, relheight=0.04)

        self.editEmailWindow(methods)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.adminWindow(methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)

    def editEmailWindow(self, methods):
        for text in self.canvasText:
            self.canvas1.delete(text)
        self.oldPasswordInput.destroy()
        self.newPasswordInput.destroy()

        self.chngMailBtn.config(relief=SUNKEN)
        self.chngPasswordBtn.config(relief=RAISED)

        self.canvasText.append(
            self.canvas1.create_text(250, 270, text="OLD EMAIL ID :", fill="white", font=('Times', 20, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(250, 370, text="NEW EMAIL ID :", fill="white", font=('Times', 20, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(250, 470, text="PASSWORD :", fill="white", font=('Times', 20, 'bold'),
                                     anchor="nw"))

        self.oldEmailInput = Entry(self.root, font=('Arial', 16, 'bold'), justify="left")
        self.oldEmailInput.place(relx=0.45, rely=0.33, relwidth=0.3, relheight=0.04)

        self.newEmailInput = Entry(self.root, font=('Arial', 16, 'bold'), justify="left")
        self.newEmailInput.place(relx=0.45, rely=0.453, relwidth=0.3, relheight=0.04)

        self.passwordInput = Entry(self.root, font=('Arial', 16, 'bold'), justify="left", show="\u2022")
        self.passwordInput.place(relx=0.45, rely=0.58, relwidth=0.3, relheight=0.04)

        updateBtn = Button(self.root, text="UPDATE", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                           command=lambda: methods["editHandler"]("email", self.oldEmailInput.get(),
                                                                  self.passwordInput.get(), self.newEmailInput.get()))
        updateBtn.place(relx=0.40, rely=0.7, relwidth=0.2, relheight=0.05)

    def editPasswordWindow(self, methods):
        for text in self.canvasText:
            self.canvas1.delete(text)
        self.oldEmailInput.destroy()
        self.newEmailInput.destroy()
        self.passwordInput.destroy()

        self.chngMailBtn.config(relief=RAISED)
        self.chngPasswordBtn.config(relief=SUNKEN)

        self.canvasText.append(
            self.canvas1.create_text(250, 300, text="OLD PASSWORD :", fill="white", font=('Times', 20, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(250, 420, text="NEW PASSWORD :", fill="white", font=('Times', 20, 'bold'),
                                     anchor="nw"))

        self.oldPasswordInput = Entry(self.root, font=('Arial', 16, 'bold'), justify="left", show="\u2022")
        self.oldPasswordInput.place(relx=0.45, rely=0.37, relwidth=0.3, relheight=0.04)

        self.newPasswordInput = Entry(self.root, justify="left", font=('Arial', 16, 'bold'))
        self.newPasswordInput.place(relx=0.45, rely=0.52, relwidth=0.3, relheight=0.04)

        updateBtn = Button(self.root, text="UPDATE", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                           command=lambda: methods["editHandler"]("password", "", self.oldPasswordInput.get(),
                                                                  self.newPasswordInput.get()))
        updateBtn.place(relx=0.40, rely=0.7, relwidth=0.2, relheight=0.05)

    def studentWindow(self, student, methods):
        self.clearWindow()
        self.clearCanvas()
        if student['stream'] == 'Computer Science & Engineering':
            stream = "Computer Science & Engg."
        else:
            stream = student['stream']

        self.heading = self.canvas1.create_text(600, 80, text='WELCOME {}'.format(student['name'].split()[0].upper()),
                                                font=("Times", 35, "bold"), fill="white")
        self.canvasText.append(
            self.canvas1.create_text(140, 200, text="STUDENT NAME:", fill="white", font=('Times', 18, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(350, 200, text=student['name'], fill="white", font=('Times', 18, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(140, 240, text="ROLL NUMBER:", fill="white", font=('Times', 18, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(340, 240, text=student['rollNo'], fill="white", font=('Times', 18, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(140, 280, text="EMAIL:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(240, 280, text=student['email'], fill="white", font=('Times', 18, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(700, 200, text="STREAM:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(820, 200, text=stream, fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(700, 240, text="YEAR:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(785, 240, text=student['year'], fill="white", font=('Times', 18, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(700, 280, text="SEMESTER:", fill="white", font=('Times', 18, 'bold'), anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(850, 280, text=student['sem'], fill="white", font=('Times', 18, 'bold'),
                                     anchor="nw"))

        # Table for visualizing the Marks with the corresponding Subjects
        self.labelSubName = Label(self.root, text="SUBJECT NAME", font=('Times', 22, 'bold'), bg="#FFBB00").place(
            relx=0.11, rely=0.45,
            relwidth=0.53, relheight=0.06)
        self.labelMarks = Label(self.root, text="MARKS OUT OF 100", font=('Times', 22, 'bold'), bg="#FFBB00").place(
            relx=0.643, rely=0.45,
            relwidth=0.25, relheight=0.06)
        subjects = [student['sub1'], student['sub2'], student['sub3'], student['sub4'], student['sub5']]
        marks = [student['mark1'], student['mark2'], student['mark3'], student['mark4'], student['mark5']]

        percent = (marks[0] + marks[1] + marks[2] + marks[3] + marks[4]) / 5
        result = ''
        if marks[0] >= 40 and marks[1] >= 40 and marks[2] >= 40 and marks[3] >= 40 and marks[4] >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        for row in range(5):
            self.l1 = Label(self.root, text=subjects[row], font=('Times', 18, 'bold'), bg="#FFECB7", anchor=W)
            self.l2 = Label(self.root, text=marks[row], font=('Times', 18, 'bold'), bg="#FFECB7")
            if row % 2 == 1:
                self.l1.config(bg="#FFDC7B")
                self.l2.config(bg="#FFDC7B")
            self.l1.place(relx=0.11, rely=0.51 + 0.05 * row, relwidth=0.53, relheight=0.05)
            self.l2.place(relx=0.643, rely=0.51 + 0.05 * row, relwidth=0.25, relheight=0.05)

        Label(self.root, text="Percentage = " + str(percent), font=('Times', 18, 'bold'), bg="#FFDC7B",
              anchor=W).place(relx=0.11, rely=0.765, relwidth=0.39, relheight=0.05)
        Label(self.root, text="Result : " + result, font=('Times', 18, 'bold'), bg="#FFDC7B",
              anchor=W).place(relx=0.503, rely=0.765, relwidth=0.39, relheight=0.05)
        # End of the Table

        self.btnEditDetails = Button(self.root, text="EDIT DETAILS", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                                     command=lambda: self.editDetails(methods, student))
        self.btnEditDetails.place(relx=0.11, rely=0.9, relwidth=0.18, relheight=0.05)

        self.logout_Btn = Button(self.root, text="LOGOUT", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                                 command=lambda: self.loginWindow("student", methods))
        self.logout_Btn.place(relx=0.8, rely=0.9, relwidth=0.1, relheight=0.05)

    def editDetails(self, methods, student):
        self.clearWindow()
        self.clearCanvas()

        self.heading = self.canvas1.create_text(600, 80, text='EDIT YOUR DETAILS', font=("Times", 35, "bold"),
                                                fill="white")
        self.canvasText.append(
            self.canvas1.create_text(250, 225, text="NEW EMAIL :", fill="white", font=('Times', 20, 'bold'), anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(250, 325, text="OLD PASSWORD :", fill="white", font=('Times', 20, 'bold'),
                                     anchor="nw"))
        self.canvasText.append(
            self.canvas1.create_text(250, 425, text="NEW PASSWORD :", fill="white", font=('Times', 20, 'bold'),
                                     anchor="nw"))

        self.email_Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="left")
        self.email_Input.place(relx=0.45, rely=0.285, relwidth=0.3, relheight=0.04)
        self.old_pass_Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="left", show="\u2022")
        self.old_pass_Input.place(relx=0.45, rely=0.410, relwidth=0.3, relheight=0.04)
        self.new_pass_Input = Entry(self.root, font=('Arial', 16, 'bold'), justify="left")
        self.new_pass_Input.place(relx=0.45, rely=0.530, relwidth=0.3, relheight=0.04)

        btnUpdate = Button(self.root, text="UPDATE", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                           command=lambda: methods['updateStudentHandler'](self.email_Input.get(),
                                                                           self.old_pass_Input.get(),
                                                                           self.new_pass_Input.get(), student))
        btnUpdate.place(relx=0.44, rely=0.7, relwidth=0.12, relheight=0.05)

        backBtn = Button(self.root, text="BACK", bg="#FFBB00", fg='white', font=("Arial", 18, 'bold'),
                         command=lambda: self.studentWindow(student, methods))
        backBtn.place(relx=0.05, rely=0.87, relwidth=0.1, relheight=0.05)