from tkinter import *
from datetime import datetime

def time_diff():
    start_=start.get()
    end_=end.get()
    t1 = datetime.strptime(start_, "%H:%M")
    t2 = datetime.strptime(end_, "%H:%M")
    value = str((t2 - t1).total_seconds() / 3600).split(".")
    hours = value[0]
    minutes = int(float('0.' + value[1]) * 60)
    time_=f'{hours}:{minutes} godzin'
    Label4.config(text=time_)


window=Tk()
window.minsize(width=200,height=100)
window.title("Ile dzisiaj przepracowałem")
window.config(padx=30, pady=50)

start=Entry(width=10)
start.grid(column=2, row=0)
start.insert(0, string=":")

end=Entry(width=10)
end.grid(column=2, row=1)
end.insert(0, string=":")

Label1=Label(text='Czas rozpoczęcia pracy(h:m): ')
Label1.grid(column=0, row=0)

Label2=Label(text='Czas zakończenia pracy(h:m): ')
Label2.grid(column=0, row=1)
Label2.config(pady=10)

Label3=Label(text="Przepracowany czas w dniu dzisiejszym: ")
Label3.grid(column=0,row=3)

Label4 = Label(text='')
Label4.grid(column=1, row=3)

button=Button(text='Ile dzisiaj przepracowałeś', command=time_diff)
button.grid(column=2, row=4)


window.mainloop()