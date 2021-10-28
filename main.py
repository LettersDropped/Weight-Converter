from tkinter import *

##Setting up the name and geometry
root = Tk()
root.title("Weight Converter")
root.geometry("600x400")

##Adding text in the windows
head_label = Label(text="Weight Converter", font=('Verdana', 10), bg='skyblue')
head_label.place(x=235,y=10)

label1 = Label(root, text="Enter weight in Kilograms :", font=('Verdana'))
label1.place(x=50,y=50)

label2 = Label(root, text="Weight in Pounds :", font=('Verdana'))
label2.place(x=50,y=100)

label3 = Label(root, text="Weight in Grams :", font=('Verdana'))
label3.place(x=50,y=150)

##Creating the Entry widget
user_entry = Entry(root, width=20)  
user_entry.place(x=300,y=54) 

##Label for the results
#Pound Section Result
label4 = Label(root, text=" ", font="10")
label4.place(x=300, y=103)

#Grams section result
label5 = Label(root, text=" ", font="10")
label5.place(x=300, y=155)

##Defining Functions
def kgbtn_click():
    ##Value converted to pounds
    kg = round(float(user_entry.get()) * 2.2)
    label4.configure(text= str(kg) + ' Pounds')

    ##Value converted to grams
    kg = round(float(user_entry.get()) * 1000)
    label5.configure(text= str(kg) + ' Grams')

##Adding the button to perform the function
btn = Button(root, text="Click to convert", command=kgbtn_click, bg="red", width=30)
btn.place(x=200, y=280)

##Footer
footer = Label(text="Made with 🧠 by Letters Dropped")
footer.place(x=215, y=350)


root.mainloop()

