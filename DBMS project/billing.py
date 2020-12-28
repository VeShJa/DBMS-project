import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
import b as backend
import pymysql
import datetime
import time
import tempfile, os

class Billing:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "BillingDB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        customer_id = StringVar()
        id = StringVar()
        Payments_Due = StringVar()
        due_Date = StringVar()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        def iExit():
            iExit = tkinter.messagebox.askyesno("Billing DB", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.txtid.delete(0, END)
            self.txtcustomer_id.delete(0, END)
            self.txtPayments_Due.delete(0, END)
            self.txtdue_Date.delete(0, END)

        def addData():
            if id.get() == "" or customer_id.get() == "" or Payments_Due.get() == "" or due_Date.get == "":
                tkinter.messagebox.askyesno("Enter correct Data")
            else:
                backend.addBill(
                    id.get(),
                    customer_id.get(),
                    Payments_Due.get(),
                    due_Date.get(),
                )

                displayData()

                super(self.billinglist, self).delete()

                self.billinglist.insert(END,
                (
                    id.get(),
                    customer_id.get(),
                    Payments_Due.get(),
                    due_Date.get(),
                ))

        def displayData():
            result = backend.viewBill()
            if len(result)!=0:
                self.billinglist.delete(*self.billinglist.get_children())
                for row in result:
                    self.billinglist.insert('', END, values = row)

        def deleteData():
            if(len(id.get())!= 0):
                backend.delBill(id.get())
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Data entry form", "Record successfully deleted")

        def billingREC():
            global sd
            iReset()
            viewInfo = self.billinglist.focus()
            learnerData = self.billinglist.Item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[1])
            self.txtcustomer_id.insert(END,sd[2])
            self.txtPayments_Due.insert(END,sd[3])
            self.txtdue_Date.insert(END,sd[4])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Frames~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#################################~~~~~~~~~~~~~~~~~~~~

        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd = 5, width = 1340, height = 100, relief = RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady = 8)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1340, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame3 = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 1340, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 300, height = 180, padx = 2, pady = 4, relief = RIDGE)
        LeftFrame1.pack(side = TOP, padx = 0, pady = 4)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 320, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        RightFrame1.pack(side = RIGHT)

        RightFrame1a = Frame(RightFrame1, bd = 5, width = 310, height = 200, padx = 2, pady = 2, relief = RIDGE)
        RightFrame1a.pack(side = TOP)

################Title###############~~~~~~~~~~~~~~~~~~~~#################################~~~~~~~~~~~~~~~~~~~~


        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Billing DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 12, height  = 2, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 12, height  = 2, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 12, height  = 2, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 12, height  = 2, command = iReset).grid(row = 0, column = 3, padx = 1)
        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 12, height  = 2, command = iExit).grid(row = 0, column = 4, padx = 1)

##################WIDGETS#############~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.lblid = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Bill ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblcustomer_id = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Customer ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblcustomer_id.grid(row=1,column=0,sticky =W,padx=5)
        self.txtcustomer_id = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = customer_id)
        self.txtcustomer_id.grid(row=1, column=1)

        self.lblPayments_Due = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Payment Due ', bd = 7, anchor='w', justify=LEFT)
        self.lblPayments_Due.grid(row=2,column=0,sticky =W,padx=5)
        self.txtPayments_Due = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Payments_Due)
        self.txtPayments_Due.grid(row=2, column=1)

        self.lbldue_Date = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Due Date', bd = 7, anchor='w', justify=LEFT)
        self.lbldue_Date.grid(row=3,column=0,sticky =W,padx=5)
        self.txtdue_Date = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = due_Date)
        self.txtdue_Date.grid(row=3, column=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TREEVIEW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.billinglist = ttk.Treeview(RightFrame1a, height = 12, columns = ("id", "customer_id", "Payments_Due", "due_Date"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.billinglist.heading("id", text = "Bill ID")
        self.billinglist.heading("customer_id", text = "Customer ID")
        self.billinglist.heading("Payments_Due", text = "Payemt Due")
        self.billinglist.heading("due_Date", text = "Due Date")

        self.billinglist['show'] = 'headings'
        self.billinglist.column("id", width = 30)
        self.billinglist.column("customer_id", width =  30)
        self.billinglist.column("Payments_Due", width = 80)
        self.billinglist.column("due_Date", width = 120)

        self.billinglist.pack(fill = BOTH, expand = 1)

        self.billinglist.bind("<ButtonRelease-1>", billingREC)
        displayData()

if __name__=='__main__':
    root = Tk()
    application = Billing(root)
    root.mainloop()
