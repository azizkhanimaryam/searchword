from tkinter import  *
from tkinter  import ttk
from tkinter import  messagebox
from  bll.blWord import blWord
from be.History import History
import pyodbc

class App(ttk.Frame):
    def __init__(self,screen):
        super().__init__(screen)
        self.master=screen
        self.CreateWidget()
    def CreateWidget(self):
        style=ttk.Style()
        style.theme_use("vista")
        self.frmHistory=Frame(self.master,width=300,bg="#dec9ff",height=400).place(x=0,y=0)
        self.frmSearch=Frame(self.master,width=300,bg="#dec9ff",height=400).place(x=300,y=0)
        self.frmRsult=Frame(self.frmSearch,width=260,bg="silver",height=350).place(x=320,y=40)

    #Search
        self.search = StringVar()
        self.Id = StringVar()
        self.Title = StringVar()
        self.En = StringVar()
        self.Text = StringVar()
        self.btnSearch=ttk.Button(self.frmSearch,text="جستجو",command=self.OnClickSearch).place(x=320,y=10)
        self.txtSearch=ttk.Entry(self.frmSearch,textvariable=self.search,justify="center").place(x=400,y=10,height=26,width=180)
        self.txtId = Entry(self.frmSearch, textvariable=self.Id).place_forget()

        self.lblTitle = Label(self.frmRsult, textvariable=self.Title, text="عنوان", bg="#c272fc", fg="white",
                              font="nazanin 12 bold", anchor="e", width=24).place(x=330, y=50)
        self.lblEn = Label(self.frmRsult, textvariable=self.En, text="تلفظ", bg="#c272fc", fg="white",
                           font="nazanin 12 bold", anchor="e", width=24).place(x=330, y=80)
        self.lblText = Label(self.frmRsult, wraplength=250, textvariable=self.Text, text="نتیجه", bg="#c272fc",
                             fg="white", font="nazanin 12 bold", anchor="e", width=24).place(x=330, y=110)

        #History
        self.tbl = ttk.Treeview(self.frmHistory, columns=("c1", "c2", "c3"), show="headings", height=17)
        self.tbl.heading("# 3", text="شماره")
        self.tbl.column("# 3", width=30, anchor=E)

        self.tbl.heading("# 2", text="عنوان")
        self.tbl.column("# 2", width=80, anchor=E)

        self.tbl.heading("# 1", text="نتیجه")
        self.tbl.column("# 1", width=190, anchor=E)

        self.tbl.bind("<Button-1>", self.SelectRowIntbl)

        self.tbl.place(x=10,y=20)

        self.BtnDelete = ttk.Button(self.frmRsult, text="حذف", command=self.OnClickDelete)

        self.BtnDelete.place_forget()

        self.LoadDataInTable()
    def OnClickSearch(self):
        self.BtnDelete.place_forget()
        querySearch=self.search.get()
        objGetWord=blWord()
        result=objGetWord.GetWord(querySearch)
        if result["Search"]=="":
            self.Title.set("نتیجه ای یافت نشد")
        else:
            objHis=History(result["Search"],result["Text"])
            objGetWord.SaveHistory(objHis)
            self.Reload()
            self.Title.set(result["Search"])
            # self.En.set(result["en"])
            self.Text.set(result["Text"])

    def LoadDataInTable(self):
        objbl=blWord()
        listHistory=objbl.GetDataHistory()
        for item in listHistory:
            self.tbl.insert('',"end",text=item.hs_id,values=[item.hs_Text, item.hs_Title,item.hs_id])

    def SelectRowIntbl(self,e):
        objbl = blWord()
        selectionRow=self.tbl.selection()
        if selectionRow!=():
            IdRow=self.tbl.item(selectionRow)["values"][2]
            self.Id.set(IdRow)
            result=objbl.GetDataById(IdRow)
            self.Title.set(result.hs_Title)
            self.Text.set(result.hs_Text)
            self.BtnDelete.place(x=330,y=360)

    def OnClickDelete(self):
        Id=self.Id.get()
        objbl = blWord()
        result=objbl.DeleteRow(Id)
        if result:
            self.BtnDelete.place_forget()
            messagebox.showinfo("انجام شد","با موفقیت از لیست نتایج حذف شد")
            self.Reload()
        else:
            messagebox.showerror("انجام نشد","  حذف نشد")

    def Reload(self):
        self.ClearTbl()
        self.LoadDataInTable()

    def ClearTbl(self):
        for item in self.tbl.get_children():
            sel=(str(item),)
            self.tbl.delete(sel)