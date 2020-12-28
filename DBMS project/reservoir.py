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


class reservoir:
    def  __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "ReservoirDB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        id = StringVar()
        Name = StringVar()
        Water_level = StringVar()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.txtid.delete(0, END)
            self.txtName.delete(0, END)
            self.txtWater_level.delete(0, END)

        def addData():
            if id.get() == "" or Name.get() == "" or Water_level.get() == "":
                tkinter.messagebox.askyesno("Insert Error", "Enter the correct data")
            else:
                backend.addReservoir(
                    id.get(),
                    Name.get(),
                    Water_level.get()
                )

                displayData()

                super(self.reservoirlist, self).delete()

                self.reservoirlist.insert(END,
                    (
                    id.get(),
                    Name.get(),
                    Water_level.get()
                    ))

        def displayData():
            result = backend.viewReservoir()
            if len(result)!=0:
                self.reservoirlist.delete(*self.reservoirlist.get_children())
                for row in result:
                    self.reservoirlist.insert('', END, values = row)

        def deleteData():
            if(len(id.get())!= 0):
                backend.delReservoir(id.get())
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Delete","Record successfully deleted")

        def ReservoirREC():
            global sd
            iReset()
            viewInfo = self.reservoirlist.focus()
            learnerData = self.reservoirlist.Item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[1])
            self.txtName.insert(END,sd[2])
            self.txtWater_level.insert(END,sd[3])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Frames~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

        ################Title###############
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Reservoir DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)

        ##################WIDGETS#############

        self.lblid = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Reservoir ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblName = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Reservoir Name ', bd = 7, anchor='w', justify=LEFT)
        self.lblName.grid(row=1,column=0,sticky =W,padx=5)
        self.txtName = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Name)
        self.txtName.grid(row=1, column=1)

        self.lblWater_level = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Water level ', bd = 7, anchor='w', justify=LEFT)
        self.lblWater_level.grid(row=2,column=0,sticky =W,padx=5)
#        self.cboWater_level = ttk.Combobox(LeftFrame1, width = 39, font = ('arial', 12, 'bold'), state = 'readonly', textvariable = Water_level)
#        self.cboWater_level['values'] = ('homeless','1', '2', '3', '4', '5', '6', '7')
#        self.cboWater_level.current(0)
#        self.cboWater_level.grid(row = 2, column = 1)
        self.txtWater_level = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Water_level)
        self.txtWater_level.grid(row=2, column=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TREEVIEW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.reservoirlist = ttk.Treeview(RightFrame1a, height = 12, columns = ("id", "Name", "Water_level"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.reservoirlist.heading("id", text = "Reservoir ID")
        self.reservoirlist.heading("Name", text = "Reservoir Name")
        self.reservoirlist.heading("Water_level", text = "Water level")

        self.reservoirlist['show'] = 'headings'
        self.reservoirlist.column("id", width = 70)
        self.reservoirlist.column("Name", width =  120)
        self.reservoirlist.column("Water_level", width = 80)

        self.reservoirlist.pack(fill = BOTH, expand = 1)

        self.reservoirlist.bind("<ButtonRelease-1>", ReservoirREC)
        displayData()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 12, height  = 2, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 12, height  = 2, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 12, height  = 2, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 12, height  = 2, command = iReset).grid(row = 0, column = 3, padx = 1)
        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 12, height  = 2, command = iExit).grid(row = 0, column = 4, padx = 1)


if __name__=='__main__':
    root = Tk()
    application = reservoir(root)
    root.mainloop()
