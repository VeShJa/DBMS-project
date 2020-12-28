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

class Customer:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Customer DB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        id = StringVar()
        Name = StringVar()
        Address = StringVar()
        sector_no = StringVar()
        officer_id = StringVar()
        reservoir_id = StringVar()
        bill_id = StringVar()
        no_of_connection = StringVar()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.txtid.delete(0, END)
            self.txtName.delete(0, END)
            self.txtAddress.delete(0, END)
            self.cbosector_no.current(0)
            self.txtofficer_id.delete(0, END)
            self.txtreservoir_id.delete(0, END)
            self.txtbill_id.delete(0, END)
            self.txtno_of_connection.delete(0, END)

        def addData():
            if id.get() == "" or Name.get() == "" or Address.get() == "" or sector_no.get() == "" or officer_id.get() == "" or reservoir_id.get() == "" or bill_id.get() == "" or no_of_connection.get() == "":
                tkinter.messagebox.askyesno("Error", "Please enter the correct Data")
            else:
                backend.addCustomer(
                    id.get(),
                    Name.get(),
                    Address.get(),
                    sector_no.get(),
                    officer_id.get(),
                    reservoir_id.get(),
                    bill_id.get(),
                    no_of_connection.get()
                )

                displayData()

                super(self.customerlist, self).delete()

                self.customerlist.insert(END,
                (
                    id.get(),
                    Name.get(),
                    Address.get(),
                    sector_no.get(),
                    officer_id.get(),
                    reservoir_id.get(),
                    bill_id.get(),
                    no_of_connection.get()
                ))


        def displayData():
            result = backend.viewCustomer()
            if len(result)!=0:
                self.customerlist.delete(*self.customerlist.get_children())
                for row in result:
                    self.customerlist.insert('', END, values = row)

        def deleteData():
            if(len(id.get())!= 0):
                backend.delCustomer(sd[0])
                displayData()
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Delete", "Record successfully deleted")
            displayData()
        #~~~~~~~~~~~~~~~~~~~~~~~UPDATE FUNCTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def update():
            if(len(id.get()) != 0):
                backend.delCustomer(sd[0])

            if(len(id.get()) != 0):
                backend.addCustomer(id.get(), Name.get(), Address.get(), sector_no.get(), officer_id.get(), reservoir_id.get(), bill_id.get(), no_of_connection.get())

            displayData()



        def customerREC(event):
            global sd
            iReset()
            viewInfo = self.customerlist.focus()
            learnerData = self.customerlist.item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[0])
            self.txtName.insert(END,sd[1])
            self.txtAddress.insert(END,sd[2])
            sector_no.set(sd[3])
            self.txtofficer_id.insert(END,sd[4])
            self.txtreservoir_id.insert(END,sd[5])
            self.txtbill_id.insert(END,sd[6])
            self.txtno_of_connection.insert(END,sd[7]



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

        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Customer DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 8, height  = 1, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 8, height  = 1, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 8, height  = 1, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnUpdate = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Update" ,padx = 24, width = 8, height  = 1, command = update).grid(row = 0, column = 3, padx = 1)
        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 8, height  = 1, command = iReset).grid(row = 0, column = 4, padx = 1)
        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 8, height  = 1, command = iExit).grid(row = 0, column = 5, padx = 1)


##################WIDGETS#############~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        self.lblid = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Customer ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblName = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Customer Name ', bd = 7, anchor='w', justify=LEFT)
        self.lblName.grid(row=1,column=0,sticky =W,padx=5)
        self.txtName = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Name)
        self.txtName.grid(row=1, column=1)

        self.lblAddress = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Address ', bd = 7, anchor='w', justify=LEFT)
        self.lblAddress.grid(row=2,column=0,sticky =W,padx=5)
        self.txtAddress = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Address)
        self.txtAddress.grid(row=2, column=1)

        self.lblsector_no = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Sector No ', bd = 7, anchor='w', justify=LEFT)
        self.lblsector_no.grid(row=3,column=0,sticky =W,padx=5)
        self.cbosector_no = ttk.Combobox(LeftFrame1, width = 39, font = ('arial', 12, 'bold'), state = 'readonly', textvariable = sector_no)
        self.cbosector_no['values'] = ('','1', '2', '3', '4', '5', '6', '7')
        self.cbosector_no.current(0)
        self.cbosector_no.grid(row = 3, column = 1)

        self.lblofficer_id = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Officer ID', bd = 7, anchor='w', justify=LEFT)
        self.lblofficer_id.grid(row=4,column=0,sticky =W,padx=5)
        self.txtofficer_id = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = officer_id)
        self.txtofficer_id.grid(row=4, column=1)

        self.lblreservoir_id = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Reservoir ID', bd = 7, anchor='w', justify=LEFT)
        self.lblreservoir_id.grid(row=5,column=0,sticky =W,padx=5)
        self.txtreservoir_id = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = reservoir_id)
        self.txtreservoir_id.grid(row=5, column=1)

        self.lblbill_id = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Bill ID', bd = 7, anchor='w', justify=LEFT)
        self.lblbill_id.grid(row=6,column=0,sticky =W,padx=5)
        self.txtbill_id = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = bill_id)
        self.txtbill_id.grid(row=6, column=1)

        self.lblno_of_connection = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'No. of connections', bd = 7, anchor='w', justify=LEFT)
        self.lblno_of_connection.grid(row=7,column=0,sticky =W,padx=5)
        self.txtno_of_connection = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = no_of_connection)
        self.txtno_of_connection.grid(row=7, column=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TREEVIEW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.customerlist = ttk.Treeview(RightFrame1a, height = 12, columns = ("id", "Name", "Address", "sector_no", "officer_id", "reservoir_id", "bill_id", "no_of_connection"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.customerlist.heading("id", text = "Customer ID")
        self.customerlist.heading("Name", text = "Customer Name")
        self.customerlist.heading("Address", text = "Customer Address")
        self.customerlist.heading("sector_no", text = "Sector No")
        self.customerlist.heading("officer_id", text = "Officer ID")
        self.customerlist.heading("reservoir_id", text = "Reservoir ID")
        self.customerlist.heading("bill_id", text = "Bill ID")
        self.customerlist.heading("no_of_connection", text = "No. of conns.")

        self.customerlist['show'] = 'headings'
        self.customerlist.column("id", width = 20)
        self.customerlist.column("Name", width =  120)
        self.customerlist.column("Address", width = 180)
        self.customerlist.column("sector_no", width = 20)
        self.customerlist.column("officer_id", width = 20)
        self.customerlist.column("reservoir_id", width = 20)
        self.customerlist.column("bill_id", width = 20)
        self.customerlist.column("no_of_connection", width = 20)

        self.customerlist.pack(fill = BOTH, expand = 1)

        self.customerlist.bind("<ButtonRelease-1>", customerREC)
        displayData()



if __name__=='__main__':
    root = Tk()
    application = Customer(root)
    root.mainloop()
