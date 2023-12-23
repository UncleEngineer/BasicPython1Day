from tkinter import *
from tkinter import ttk # theme of tk

GUI = Tk()
GUI.geometry('700x600')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')

#widget 
L = ttk.Label(GUI,text='โปรแกรมบันทึกค่าใช้จ่าย',font=('Angsana New',30))
L.pack()
############################

v_expense = StringVar()
L = ttk.Label(GUI,text='รายการค่าใช้จ่าย' ,font=('Angsana New',20))
L.pack(pady=5)

E1 = ttk.Entry(GUI,textvariable=v_expense,font=('Angsana New',30),width=30)
E1.pack()
############################
L = ttk.Label(GUI,text='ประเภท',font=('Angsana New',20))
L.pack(pady=5)

C = ttk.Combobox(GUI,font=('Angsana New',20),width=28)
GUI.option_add('*TCombobox*Listbox.font', ('Angsana New',30))
C.set('ค่าอาหาร')
C['values'] = ['ค่าอาหาร','ค่าเดินทาง','บัตรเครดิต']
C.pack(pady=10)
############################
L = ttk.Label(GUI,text='ค่าใช้จ่าย (บาท)',font=('Angsana New',20))
L.pack(pady=5)

v_price = StringVar()

E2 = ttk.Entry(GUI,font=('Angsana New',30),textvariable=v_price)
E2.pack()

############################
def Save():
    expense = v_expense.get()
    expense_type = C.get()
    price = v_price.get()
    print(expense)
    print(expense_type)
    print(price)


B = ttk.Button(GUI,text='Save',command=Save)
B.pack(ipadx=20,ipady=10,pady=20)

GUI.mainloop()
