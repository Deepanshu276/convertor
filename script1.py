from tkinter import *

window=Tk()

#function 1
def km_to_miles():
    miles=float(e1_value.get())*1.6
    t1.insert(END, miles)

b1=Button(window,text="Km to miles", command=km_to_miles)
b1.grid(row=0,column=0)#use rowspan for expanding button in more than 1 row

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=0,width=20)
t1.grid(row=0,column=2)

#function2
def meter_to_cm():
    cm=float(e2_value.get())*100
    t2.insert(END, cm)

b2=Button(window,text="meter to cm", command=meter_to_cm)
b2.grid(row=3, column=0)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value)
e2.grid(row=3, column=1)

t2=Text(window,height=0,width=20)
t2.grid(row=3,column=2)

#function3
def meter_to_millimeter():
    millimeter=float(e3_value.get())*1000
    t3.insert(END, millimeter)

b3=Button(window,text="meter to millimeter", command=meter_to_millimeter)
b3.grid(row=5, column=0)

e3_value=StringVar()
e3=Entry(window, textvariable=e3_value)
e3.grid(row=5, column=1)

t3=Text(window,height=0,width=20)
t3.grid(row=5,column=2)

#function4
def meter_to_micrometer():
    micrometer=float(e4_value.get())*1000000
    t4.insert(END, micrometer)

b4=Button(window,text="meter to micrometer", command=meter_to_micrometer)
b4.grid(row=7, column=0)

e4_value=StringVar()
e4=Entry(window, textvariable=e4_value)
e4.grid(row=7, column=1)

t4=Text(window,height=0,width=20)
t4.grid(row=7,column=2)

#function5
def meter_to_nanometer():
    nanometer=float(e5_value.get())*1000000000
    t5.insert(END, nanometer)

b5=Button(window,text="meter to nanometer", command=meter_to_nanometer)
b5.grid(row=9, column=0)

e5_value=StringVar()
e5=Entry(window, textvariable=e5_value)
e5.grid(row=9, column=1)

t5=Text(window,height=0,width=20)
t5.grid(row=9,column=2)

window.mainloop()
