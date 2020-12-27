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


class officer(object):
    def  __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "OfficerDB")
        self.root.geometry("1920x1080+0+0")

        id = StringVar()
        Name = StringVar()
        sector_no = StringVar()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def iExit():
            iExit = tkinter.messagebox.askyesno("Officer DB", "Confirm if you want to eXiT")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.txtid.delete(0, END)
            self.txtName.delete(0, END)
            self.cbosector_no.delete(0, END)

        def addData():
            if id.get() == "" or Name.get == "" or sector_no.get() == "":
                tkinter.messagebox.askyesno("Enter correct Data")
            else:
                backend.addOfficer(
                    id.get(),
                    Name.get(),
                    sector_no.get()
                )
                displayData()
                super(self.officerlist, self).delete()

                self.officerlist.insert(END,
                    (
                    id.get(),
                    Name.get(),
                    sector_no.get()
                    ))

        def displayData():
            result = backend.viewOfficer()
            if len(result)!=0:
                self.officerlist.delete(*self.officerlist.get_children())
                for row in result:
                    self.officerlist.insert('', END, values = row)

        def deleteData():
            if(len(id.get())!= 0):
                backend.delOfficer(id.get())
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Data entry form", "Record successfully dEleted")

        def officerREC():
            global sd
            iReset()
            viewInfo = self.officerlist.focus()
            learnerData = self.officerlist.Item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[1])
            self.txtName.insert(END,sd[2])
            sector_no.set(sd[3])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Frames~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        MainFrame = Frame(self.root, bd = 10, width = 1920, height = 1080, relief = RIDGE, bg = "red")
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd = 5, width = 1920, height = 50, relief = RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady = 8)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1920, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame3 = Frame(MainFrame, bd = 5, width = 1920, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 1920, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 1920, height = 180, padx = 2, pady = 4, relief = RIDGE)
        LeftFrame1.pack(side = TOP, padx = 0, pady = 4)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 1920, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        RightFrame1.pack(side = RIGHT)

        RightFrame1a = Frame(RightFrame1, bd = 5, width = 1920, height = 200, padx = 2, pady = 2, relief = RIDGE)
        RightFrame1a.pack(side = TOP)

        ################Title###############
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Officer DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)

        ##################WIDGETS#############

        self.lblid = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'ID: ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblName = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Officer Name: ', bd = 7, anchor='w', justify=LEFT)
        self.lblName.grid(row=1,column=0,sticky =W,padx=5)
        self.txtName = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Name)
        self.txtName.grid(row=1, column=1)

        self.lblsector_no = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Sector no: ', bd = 7, anchor='w', justify=LEFT)
        self.lblsector_no.grid(row=2,column=0,sticky =W,padx=5)
        self.cbosector_no = ttk.Combobox(LeftFrame1, width = 39, font = ('arial', 12, 'bold'), state = 'readonly', textvariable = sector_no)
        self.cbosector_no['values'] = ('homeless','1', '2', '3', '4', '5', '6', '7')
        self.cbosector_no.current(0)
        self.cbosector_no.grid(row = 2, column = 1)

#        self.txtsector_no = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = sector_no)
#        self.txtsector_no.grid(row=2, column=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TREEVIEW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.officerlist = ttk.Treeview(RightFrame1a, height = 12, columns = ("id", "Name", "sector_no"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.officerlist.heading("id", text = "id")
        self.officerlist.heading("Name", text = "Name")
        self.officerlist.heading("sector_no", text = "sector_no")

        self.officerlist['show'] = 'headings'
        self.officerlist.column("id", width = 20)
        self.officerlist.column("Name", width =  150)
        self.officerlist.column("sector_no", width = 100)

        self.officerlist.pack(fill = BOTH, expand = 1)

        self.officerlist.bind("<ButtonRelease-1>", officerREC)
        displayData()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 12, height  = 2, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 12, height  = 2, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 12, height  = 2, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 12, height  = 2, command = iReset).grid(row = 0, column = 3, padx = 1)
        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 12, height  = 2, command = iExit).grid(row = 0, column = 4, padx = 1)


if __name__=='__main__':
    root = Tk()
    application = officer(root)
    root.mainloop()
