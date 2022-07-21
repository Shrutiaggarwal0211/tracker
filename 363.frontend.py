from tkinter import *
import backend



def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    backend.delete(selected_row[0])

def view_command():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend.search(date_text.get(),temperature_text.get(),Pulse_text.get(),Respiration_text.get(),BP_text.get(),Weight_text.get()):
        list.insert(END,row)

def add_command():
    backend.insert(date_text.get(),temperature_text.get(),Pulse_text.get(),Respiration_text.get(),BP_text.get(),Weight_text.get())

    list.delete(0,END)
    list.insert(END,(date_text.get(),temperature_text.get(),Pulse_text.get(),Respiration_text.get(),BP_text.get(),Weight_text.get()))

win = Tk()

win.wm_title('Health Records')

l1 = Label(win, text='Date')
l1.grid(row=0,column=0)
l2 = Label(win, text='Temperature')
l2.grid(row=0,column=2)
l3 = Label(win, text='Pulse')
l3.grid(row=1,column=0)
l4 = Label(win, text='Respiration')
l4.grid(row=1,column=2)
l5 = Label(win, text='Blood Pressure')
l5.grid(row=2,column=0)
l6 = Label(win, text='Weight')
l6.grid(row=2,column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0,column=1)

temperature_text = StringVar()
e2 = Entry(win, textvariable=temperature_text)
e2.grid(row=0,column=3)

Pulse_text = StringVar()
e3 = Entry(win, textvariable=Pulse_text)
e3.grid(row=1,column=1)

Respiration_text = StringVar()
e4 = Entry(win, textvariable=Respiration_text)
e4.grid(row=1,column=3)

BP_text = StringVar()
e5 = Entry(win, textvariable=BP_text)
e5.grid(row=2,column=1)

Weight_text = StringVar()
e6 = Entry(win, textvariable=Weight_text)
e6.grid(row=2,column=3)

list = Listbox(win,height=8,width=35)
list.grid(row=3,column=0,rowspan=9,columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(win,text='ADD',width=12,pady=5,command=add_command)
b1.grid(row=3,column=3)

b2 = Button(win,text='Search',width=12,pady=5,command=search_command)
b2.grid(row=4,column=3)

b3 = Button(win,text='Delete date',width=12,pady=5,command=delete_command)
b3.grid(row=5,column=3)

b4 = Button(win,text='View all',width=12,pady=5,command=view_command)
b4.grid(row=6,column=3)

b5 = Button(win,text='Close',width=12,pady=5,command = win.destroy)
b5.grid(row=7,column=3)

win.mainloop()
