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

class Locality:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "LocalityDB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        sector_no = StringVar()
        Area_Name = StringVar()
        Water_Supply_Date = StringVar()
        officer_id = StringVar()
        reservoir_id = StringVar()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def iExit():
            iExit = tkinter.messagebox.askyesno("Locality DB", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.cbosector_no.delete(0, END)
            self.txtArea_Name.delete(0, END)
            self.txtWater_Supply_Date.delete(0, END)
            self.txtofficer_id.delete(0, END)
            self.txtreservoir_id.delete(0, END)

        def addData():
            if sector_no.get() == "" or Area_Name.get() == "" or Water_Supply_Date.get() == "" or officer_id.get() == "" or reservoir_id.get() == "":
                tkinter.messagebox.askyesno("Enter correct Data")
            else:
                backend.addLocality(
                    sector_no.get(),
                    Area_Name.get(),
                    Water_Supply_Date.get(),
                    officer_id.get(),
                    reservoir_id.get()
                )

                displayData()

                super(self.localitylist, self).delete()

                self.localitylist.insert(END,
                (
                    sector_no.get(),
                    Area_Name.get(),
                    Water_Supply_Date.get(),
                    officer_id.get(),
                    reservoir_id.get()
                ))


        def displayData():
            result = backend.viewLocality()
            if len(result)!=0:
                self.localitylist.delete(*self.localitylist.get_children())
                for row in result:
                    self.localitylist.insert('', END, values = row)

        def deleteData():
            if(len(sector_no.get())!= 0):
                backend.delLocality(sector_no.get())
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Data entry form", "Record successfully deleted")

        def localityREC():
            global sd
            iReset()
            viewInfo = self.localitylist.focus()
            learnerData = self.localitylist.Item(viewInfo)
            sd = learnerData['values']

            sector_no.set(sd[1])
            self.txtArea_Name.insert(END,sd[2])
            self.txtWater_Supply_Date.insert(END,sd[3])
            self.txtofficer_id.insert(END,sd[4])
            self.txtreservoir_id.insert(END,sd[5])



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

        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Locality DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 12, height  = 2, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 12, height  = 2, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 12, height  = 2, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 12, height  = 2, command = iReset).grid(row = 0, column = 3, padx = 1)
        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 12, height  = 2, command = iExit).grid(row = 0, column = 4, padx = 1)



##################WIDGETS#############~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.lblsector_no = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Sector No. ', bd = 7, anchor='w', justify=LEFT)
        self.lblsector_no.grid(row=0,column=0,sticky =W,padx=5)
        self.cbosector_no = ttk.Combobox(LeftFrame1, width = 39, font = ('arial', 12, 'bold'), state = 'readonly', textvariable = sector_no)
        self.cbosector_no['values'] = ('','1', '2', '3', '4', '5', '6', '7')
        self.cbosector_no.current(0)
        self.cbosector_no.grid(row = 0, column = 1)


        self.lblArea_Name = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Area Name ', bd = 7, anchor='w', justify=LEFT)
        self.lblArea_Name.grid(row=1,column=0,sticky =W,padx=5)
        self.txtArea_Name = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Area_Name)
        self.txtArea_Name.grid(row=1, column=1)

        self.lblWater_Supply_Date = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Water Supply Date ', bd = 7, anchor='w', justify=LEFT)
        self.lblWater_Supply_Date.grid(row=2,column=0,sticky =W,padx=5)
        self.txtWater_Supply_Date = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Water_Supply_Date)
        self.txtWater_Supply_Date.grid(row=2, column=1)

        self.lblofficer_id = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Officer ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblofficer_id.grid(row=3,column=0,sticky =W,padx=5)
        self.txtofficer_id = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = officer_id)
        self.txtofficer_id.grid(row=3, column=1)


        self.lblreservoir_id = Label(LeftFrame1, font = ('arial',12,'bold'), text = 'Reservoir ID', bd = 7, anchor='w', justify=LEFT)
        self.lblreservoir_id.grid(row=4,column=0,sticky =W,padx=5)
        self.txtreservoir_id = Entry(LeftFrame1, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = reservoir_id)
        self.txtreservoir_id.grid(row=4, column=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TREEVIEW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.localitylist = ttk.Treeview(RightFrame1a, height = 12, columns = ("sector_no", "Area_Name", "Water_Supply_Date", "officer_id", "reservoir_id"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.localitylist.heading("sector_no", text = "Sector No.")
        self.localitylist.heading("Area_Name", text = "Area Name")
        self.localitylist.heading("Water_Supply_Date", text = "Water Supply Date")
        self.localitylist.heading("officer_id", text = "Officer ID")
        self.localitylist.heading("reservoir_id", text = "Reservoir ID")

        self.localitylist['show'] = 'headings'
        self.localitylist.column("sector_no", width = 20)
        self.localitylist.column("Area_Name", width =  150)
        self.localitylist.column("Water_Supply_Date", width = 100)
        self.localitylist.column("officer_id", width = 20)
        self.localitylist.column("reservoir_id", width = 20)

        self.localitylist.pack(fill = BOTH, expand = 1)

        self.localitylist.bind("<ButtonRelease-1>", localityREC)
        displayData()



if __name__=='__main__':
    root = Tk()
    application = Locality(root)
    root.mainloop()
