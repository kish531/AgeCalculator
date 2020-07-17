from tkinter import *
from tkinter import messagebox

root=Tk()
def clearAll():
    day.delete(0, END)
    month.delete(0, END)
    year.delete(0, END)
    givenday.delete(0, END)
    givenmonth.delete(0, END)
    givenyear.delete(0, END)
    resultday.delete(0, END)
    resultmonth.delete(0, END)
    resultyear.delete(0, END)
def checkError():
    if(year.get()>givenyear.get() or (year.get()==givenyear.get() and month.get()>givenmonth.get())or (year.get()==givenyear.get() and month.get()==givenmonth.get() and day.get()>givenday.get())):
        messagebox.showerror("Wrong Input")
        clearAll()
        return -1
def calculateAge():
    global day
    global month
    global year
    value = checkError()
    if value==-1:
        return
    else:
        birth_day=int(day.get())
        birth_month=int(month.get())
        birth_year= int(year.get())

        given_day = int(givenday.get())
        given_month = int(givenmonth.get())
        given_year = int(givenyear.get())
        diffmonth=[30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if(birth_day>given_day):
            given_month=given_month-1
            given_day=given_day + diffmonth[birth_month-1]
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12
        calculated_day=given_day-birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

        resultday.insert(5, str(calculated_day))
        resultmonth.insert(5, str(calculated_month))
        resultyear.insert(5, str(calculated_year))

root.title("Age Calculator")
root.geometry("600x600")
root.config(bg="#ffe7ba")
dob_label=Label(root, text="Date of birth", bg="#00c5cd")
givendate_label=Label(root, text="Given Date", bg="#00c5cd")
dob_label.grid(row=0, column=1)
givendate_label.grid(row=0, column=4)

day_label=Label(root, text="Day", bg="#c1f588")
month_label=Label(root, text="Month", bg="#c1f588")
year_label=Label(root, text="Year", bg="#c1f588")
day=Entry(root)
month=Entry(root)
year=Entry(root)
day_label.grid(row=1, column=0)
month_label.grid(row=2, column=0)
year_label.grid(row=3, column=0)
day.grid(row=1, column=1)
month.grid(row=2, column=1)
year.grid(row=3, column=1)

givenday_label=Label(root, text="Given Day", bg="#c1f588")
givenmonth_label=Label(root, text="Given Month", bg="#c1f588")
givenyear_label=Label(root, text="Given Year", bg="#c1f588")
givenday=Entry(root)
givenmonth=Entry(root)
givenyear=Entry(root)
givenday_label.grid(row=1, column=3)
givenmonth_label.grid(row=2, column=3)
givenyear_label.grid(row=3, column=3)
givenday.grid(row=1, column=4)
givenmonth.grid(row=2, column=4)
givenyear.grid(row=3, column=4)

resultday_label=Label(root, text="Days:", bg="#c1f588")
resultmonth_label=Label(root, text="Months:", bg="#c1f588")
resultyear_label=Label(root, text="Years:", bg="#c1f588")
resultyear=Entry()
resultday=Entry()
resultmonth=Entry()
resultday_label.grid(row=6, column=2)
resultmonth_label.grid(row=7, column=2)
resultyear_label.grid(row=8, column=2)
resultday.grid(row=6, column=3)
resultmonth.grid(row=7, column=3)
resultyear.grid(row=8, column=3)

resultage=Button(root, text="Result", command=calculateAge, bg="#00c5cd")
clearall=Button(root, text="Clear", command=clearAll, bg="#00c5cd")
resultage.grid(row=5, column=3)
clearall.grid(row=9, column=3)


root.mainloop()