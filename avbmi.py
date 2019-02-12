from Tkinter import *

window = Tk()
window.title("BEST BMI APP")

def calculate():
    height= float(varheight.get())
    weight= float(varweight.get())
    bmimass= weight*703/height**2
    massresult.config(text=bmimass)
    #print(format(bmimass))



varweight = DoubleVar()
varheight = DoubleVar()

labl1 = Label(window, text="Welcome To The Only Place Where You Can Calculate Your BMI !!",
              font=("arial bold", 15))

lbel_weig = Label(window, text="Enter Weight")
txtweig = Entry(window, textvariable= varweight, width=15, text="Weight input goes here")
lbel_heig = Label(window, text="Enter Height")
txtheig = Entry(window,textvariable= varheight, width=15, text="Height input goes here")
massresult = Label(window, text="bmi will show here")
bttn1 = Button(window, text="Submit", command=calculate)

labl1.grid(row=0, column=1)
lbel_weig.grid(row=6, column=0)
txtweig.grid(row=6, column=1)
lbel_heig.grid(row=10, column=0)
txtheig.grid(row=10, column=1)
bttn1.grid(row=25, column=1)
massresult.grid(row=40, column=1)



window.geometry('600x300')
window.mainloop()
