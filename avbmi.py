from Tkinter import *
import webbrowser

def callback():
    webbrowser.open_new(r"https://www.cigna.com/takecontrol/tc/bmi/")

#webbrowser.open("https://www.cigna.com/takecontrol/tc/bmi/")

window = Tk()
window.title("BEST BMI APP")

def calculate():
    feet= float(varheight.get())
    inches =float(varinches.get())
    height = (feet*12)+inches
    weight= float(varweight.get())
    bmimass= str("%.2f" %(weight*703/height**2))
    message = "YOUR BODY MASS IS: " + str(bmimass)
    massresult.config(text=message)




varweight = DoubleVar()
varheight = DoubleVar()
varinches = DoubleVar()

labl1 = Label(window, text="Welcome To The Only Place Where You Can Calculate Your BMI !!",
              font=("arial bold", 15))

lbel_weig = Label(window, text="Enter Weight")
txtweig = Entry(window, textvariable= varweight, width=15, text="Weight input goes here")
lbel_heig = Label(window, text="Enter Feet")
txtheig = Entry(window,textvariable= varheight, width=15, text="Feet input goes here")
lbel_inch = Label(window, text="Enter Inches")
txtinch = Entry(window,textvariable= varinches, width=15, text="Inches input goes here")
massresult = Label(window, text="bmi will show here")
bttn1 = Button(window, bg="green", text="Submit", command=calculate)

#text= Label(window, text="To Maintain A Healthy BMI Click Here")
lbl = Label(window, text="To Maintain A Healthy BMI Click Here", fg="blue", cursor="hand2")
lblbut= Button(window,text="Click Here", command=callback)

labl1.grid(row=0, column=1)
lbel_weig.grid(row=6, column=0)
txtweig.grid(row=6, column=1)
lbel_heig.grid(row=10, column=0)
txtheig.grid(row=10, column=1)
lbel_inch.grid(row=11,column=0)
txtinch.grid(row=11,column=1)
bttn1.grid(row=25, column=1)
massresult.grid(row=40, column=1)
#text.grid(row=43, column= 1)
lbl.grid(row=45,column=1)
lblbut.grid(row=50, column=1)



window.geometry('600x300')
window.mainloop()
