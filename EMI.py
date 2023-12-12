import tkinter

def calculate():
    ashol = int(input1.get())
    shomoy = int(input2.get())
    har = int(input3.get())
    I = (ashol * shomoy * har)/100
    Return = (I + ashol)
    YM = shomoy*12
    Monthly = Return/YM
    tkinter.Label(text=f"Monthly Payment: {Monthly}", font=("helvetica", 12)).place(x=0, y=350)
    tkinter.Label(text=f"Total Interest Payable: {I}", font=("helvetica", 12)).place(x=0, y=370)
    tkinter.Label(text=f"Total Payment: {Return}", font=("helvetica", 12)).place(x=0, y=390)

root = tkinter.Tk()
root.geometry('300x500')
root.resizable(False, False)
root.title('EMI Calculator')

label1 = tkinter.Label(root, text="Outstanding Principle: ", font=("Helvetica", 12))
label1.grid(row=0, column=0)
input1 = tkinter.Entry()
input1.grid(row=0, column=1)

label2 = tkinter.Label(root, text="Loan Tenure (Year): ", font=("Helvetica", 12))
label2.grid(row=1, column=0)
input2 = tkinter.Entry()
input2.grid(row=1, column=1)

label3 = tkinter.Label(root, text="Interest Rate: ", font=("Helvetica", 12))
label3.grid(row=2, column=0)
input3 = tkinter.Entry()
input3.grid(row=2, column=1)



btn = tkinter.Button(root, text="Calculate", width=10, height=3, font=("Helvetica", 12), command=calculate).place(x=110, y=200)




root.mainloop()