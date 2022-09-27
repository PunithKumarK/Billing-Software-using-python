from tkinter import*
from tkinter import font
from turtle import width
from PIL import ImageTk,Image
class Bill:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1920x1080+0+0")
      self.root.title("GANA MOPS Billing software")
      bg_color="#074463"
      title=Label(text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",30,"bold")).pack(fill=X)

      #variables

      self.item1=IntVar()

      self.item2=IntVar()

      self.item3=IntVar()

      self.totalprice=IntVar()

      self.customer=StringVar()

      self.phone=StringVar()
       
      #customer detail frame
      F1=LabelFrame(self.root,text="customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
      F1.place(x=0,y=80,relwidth=1)

      cname_lbl=Label(F1,text="customer name",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=10)
      cname_txt=Entry(F1,width=20,textvariable=self.customer,font="arial 15").grid(row=0,column=1)

      phone_lbl=Label(F1,text="phone number",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=5,pady=10)
      phone_txt=Entry(F1,width=20,textvariable=self.phone,font="arial 15").grid(row=1,column=1)
     
      #items entry frame
      F2=LabelFrame(self.root,text="items",font=("times new roman",30,"bold"),fg="gold",bg=bg_color)
      F2.place(x=0,y=250,relwidth=325,height=580)

      cname_lbl=Label(F2,text="item 1",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=10)
      cname_txt=Entry(F2,width=20,textvariable=self.item1,font="arial 15").grid(row=0,column=1)

      cname_lbl=Label(F2,text="item 2",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=5,pady=10)
      cname_txt=Entry(F2,width=20,textvariable=self.item2,font="arial 15").grid(row=1,column=1)

      cname_lbl=Label(F2,text="item 2",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=5,pady=10)
      cname_txt=Entry(F2,width=20,textvariable=self.item3,font="arial 15").grid(row=3,column=1)

      #Bill area

      F5=Frame(self.root,bd=10,relief=GROOVE)
      F5.place(x=1000,y=250,width=380,height=380)
      bill_title=Label(F5,text="Bill area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
      scroll_y=Scrollbar(F5,orient=VERTICAL)
      self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
      scroll_y.pack(side=RIGHT,fill=Y)
      scroll_y.config(command=self.txtarea.yview)
      self.txtarea.pack(fill=BOTH,expand=1)

      #button frame

      F6=LabelFrame(self.root,text="CALCULATIONS",font=("times new roman",30,"bold"),fg="gold",bg=bg_color)
      F6.place(x=0,y=560,relwidth=1,height=140)

      m1_lbl=Label(F6,text="TOTAL",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
      m1_txt=Entry(F6,width=18,textvariable=self.totalprice,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

      btn_F=Frame(F6,bd=7,relief=GROOVE)
      btn_F.place(x=750,width=580,height=105)

      total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=1)

      generate=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=1)

      clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=1)

      exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=1)
      self.welcome_bill()

    def total(self):
      self.item1_price=self.item1.get()*120
      self.item2_price=self.item2.get()*160
      self.item3_price=self.item3.get()*180

      self.total_price=(
        self.item1_price+
        self.item2_price+
        self.item3_price
      )

      self.totalprice.set("Rs "+str(self.total_price))

    def welcome_bill(self):
      self.txtarea.delete('1.0',END)
      self.txtarea.insert(END,"\t Welcome to GANA mops")
      self.txtarea.insert(END,f"\n Customer name : {self.customer.get()}")
      self.txtarea.insert(END,f"\n Phone Number : {self.phone.get()}")
      self.txtarea.insert(END,"\n")
      self.txtarea.insert(END,"\n ***************************************")
      self.txtarea.insert(END,"\nitem name \t\t quantity \t\t price")
      self.txtarea.insert(END,"\n ***************************************")


    def bill_area(self):
      self.welcome_bill()
      if self.item1.get()!=0:
        self.txtarea.insert(END,f"\n item 1 \t\t {self.item1.get()} \t\t {self.item1_price}")

      if self.item2.get()!=0:
        self.txtarea.insert(END,f"\n item 2 \t\t {self.item2.get()} \t\t {self.item2_price}")
      
      if self.item3.get()!=0:
        self.txtarea.insert(END,f"\n item 3 \t\t {self.item3.get()} \t\t {self.item3_price}")
      







      

  
      

      


root=Tk()
obj = Bill(root)
root.mainloop()