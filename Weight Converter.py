# Create a GUI with an entry box
# entry box is for people to type their weight inLBS
# entry should have a label called "Enter Weight in LBS"
# a button named "Submit"
# button should trigger a conversion for LBS to KG
# 1 lbs = .453592

# tkinter allows for GUI
from tkinter import *

# Main GUI window
root = Tk()
root.geometry('700x300')
root.title('Weight Converter')
root.configure(background='cornflowerblue')

# Label for Entry Box
Boxed = Label(root, text='Enter Weight in LBS:', font=("Courier 12 bold"))
Boxed.place(x=100, y=80) #main GUI positioning

# Label for Result Box
Boxed1 = Label(root, text='LBS in Kg:', font=("Courier 12 bold"))
Boxed1.place(x=100, y=110)

# Entry Box
Entry = Entry(root, width=21, justify=CENTER, font=("Courier 10"), relief=SOLID)
Entry.place(x=370, y=80)

# Result Box
Result = Label(root, width=21, justify=CENTER, font=("Courier 10 bold"), relief=SOLID)
Result.place(x=370, y=110)

# Condition for converting lbs to kg
def LbsToKg():
    pounds = round(float(Entry.get()) * 0.453592,4)  # rounds converted pounds to the 4th decimal
    Result.configure(text=str(pounds) + ' Kg')

# Submit button connected to def
Submit = Button(root, text='Submit Button', width=20, height=2, font=("Courier 15 bold"), command=LbsToKg)
Submit.place(x=250, y=150)

# Runs program
root.mainloop()

