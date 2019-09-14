'''
Programming Project #7: Payroll Shuffle
Noah Schill
CS1400-X01
28 April 2019

You are creating part of the payroll program for an Internet electronics store named "FluffShuffle Electronics". The owner of FluffShuffle has given you the following requirements: FluffShuffle employs six (6) people. The owner doesn't expect significant growth in his company, but to be on the safe side he would like the program to handle a maximum of ten (10) employees.

All of the employee data (name, address, etc.) is kept in a text file on your disk. Your program will read this employee data from the file and use that data to calculate the payroll for company employees. The program will have to calculate the payroll deductions for each employee and their net pay.

If you encounter errors while reading a data file, print an error message to the console, and close the file. Your program should not exit, since you might choose another file with correct data.

Suppose that your programming team has come up with a design for this program. In this design the data for each employee on the payroll will be held in an object of the Employee class.
'''


from tkinter import *
import os


class Employee:  # defines the employee object
    def __init__(self, number, name, address, payInfo):
        self.number = number
        self.name = name
        self.address = address
        self.wage = float(payInfo[0])
        self.hoursWorked = int(payInfo[1])

    def calc_salary(self):
        self.grossPay = self.wage * self.hoursWorked
        if self.hoursWorked > 40:  # calculate overtime
            self.overtime = self.hoursWorked - 40
            self.grossPay = self.grossPay + self.overtime*1.5  # add overtime
        fedTax = self.grossPay * 0.2
        stateTax = self.grossPay * 0.075
        self.netPay = round(self.grossPay - fedTax - stateTax, 2)
        return '${:,.2f}'.format(self.netPay)


class EmployeeData:

    employeeList = []

    def __init__(self):
        self.dir = input("Enter a file directory: ")
        if os.path.isfile(self.dir):
            self.makeEmployees(dir)
        else:
            print("File not found")


    def makeEmployees(self, dir):

        doc = open(self.dir, "r")
        line_list = []
        with doc as fileobj:
            for line in fileobj:
                line_list.append(line)
        doc.close()

        employeeRawList = [line_list[i: i+4] for i in range(0, len(line_list), 4)]

        for i in employeeRawList:
            self.addEmployee(i)

    def addEmployee(self, employeeInfo):
        number = int(employeeInfo[0])
        name = employeeInfo[1]
        address = employeeInfo[2]
        payInfo = tuple(employeeInfo[3].rstrip('\n').split(" "))
        employee = Employee(number, name, address, payInfo)
        self.employeeList.append(employee)

    def getEmployeeList(self):
        return self.employeeList


class Window:
    def __init__(self):

        master = Tk()

        # build header/icons
        headerFrame = Frame(master)
        canvas = Canvas(headerFrame, height=100)
        canvas.grid(row=0, columnspan=3)
        img = PhotoImage(file="./fluff.png")
        canvas.create_image(200, 50, image=img)
        headerFrame.grid(row=0)

        # build mainFrame in gui
        mainFrame = Frame(master)

        # Data Fields
        nameLabel = Label(mainFrame, text="Name: ", font='Helvetica 18')
        nameLabel.grid(row=0, sticky=W)
        self.nameField = Label(mainFrame, font='Helvetica 12 bold')
        self.nameField.grid(row=0, column=2, sticky=E)

        addressLabel = Label(mainFrame, text="Address: ", font='Helvetica 18')
        addressLabel.grid(row=1, sticky=W)
        self.addressField = Label(mainFrame, font='Helvetica 12 bold')
        self.addressField.grid(row=1, column=2, sticky=E)

        payLabel = Label(mainFrame, text="Net Pay: ", font='Helvetica 18')
        payLabel.grid(row=3, sticky=W)
        self.payField = Label(mainFrame, font='Helvetica 12 bold')
        self.payField.grid(row=3, column=2, sticky=E)

        # Buttons
        lastButton = Button(mainFrame, text="<--Last", command=self.goBack)
        lastButton.grid(row=4, sticky=E)
        nextButton = Button(mainFrame, text="Next-->", command=self.goForward)
        nextButton.grid(row=4, column=3, sticky=E)

        # populate text forms
        self.d = EmployeeData()
        self.currentIndex = 0
        self.updateText()

        # mainframe and window configs
        mainFrame.grid(row=1, columnspan=4)
        mainFrame.columnconfigure(2, minsize=200)
        master.resizable(False, False)
        master.mainloop()

    def goBack(self):
        self.currentIndex = self.currentIndex - 1
        if self.currentIndex < 0:
            self.currentIndex = 0
        self.updateText()

    def goForward(self):
        self.currentIndex = self.currentIndex + 1
        if self.currentIndex >= len(self.d.employeeList):
            self.currentIndex = len(self.d.employeeList) - 1
        self.updateText()

    def updateText(self):
        self.nameField['text']=self.d.employeeList[self.currentIndex].name
        self.addressField['text']=self.d.employeeList[self.currentIndex].address
        self.payField['text']=self.d.employeeList[self.currentIndex].calc_salary()


def main():
    w = Window()  # init window


main()
