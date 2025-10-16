"""                                        *Tkinter *                  
"""
""" they are 3 types of the Tkinter 
 1. pack 
 2. place 
 3. grid 
 
 """


# import tkinter as tk 
# window = tk.Tk()
# window.geometry("1500x600")
# window.config(background='#27F59C')
# label1=tk.Label(text="This Is The My First App",font=('BOLD',25),bg='#F5276C')
# label1.place(x=100,y=150)

# window.mainloop()


"part 2"
# import tkinter as tk 
# window = tk.Tk()
# window.geometry("1500x600")
# window.config(background='#27F59C')
# label1=tk.Label(text="This Is The My First App",font=('BOLD',25),bg='#F5276C')
# # label1.place(x=100,y=150)
# label1.grid(row=2 , column=2)


# window.mainloop()



"pack 3"
" This is the click function are the implimentation "



# import tkinter as tk 
# from tkinter import messagebox

# window = tk.Tk()
# window.geometry("1500x600")
# window.config(background='#27F59C')

# # Label
# label1 = tk.Label(window, text="This Is My First App", font=('Arial', 25, 'bold'), bg='#861043')
# label1.place(x=500, y=150)

# # button
# def action1():
#     messagebox.showinfo("Success","Button Clicked")
# button = tk.Button(window, text='Click Me', font=('BOLD',25),bg='lightgreen',command=action1)
# button.place(x=700, y=220)

# window.mainloop()



"Part 4"



# import tkinter as tk 
# from tkinter import messagebox

# window = tk.Tk()
# window.geometry("1500x600")
# window.config(background='#1C2833')

# # Label
# label1 = tk.Label(window, text="This Is My First App", font=('Arial', 25, 'bold'), bg='hotpink')
# label1.place(x=500, y=150)

# # calculator 
# entry1=tk.Entry(window,font=('BOLD',25),bg='yellow')
# entry1.place(x=500,y=200)
# entry2=tk.Entry(window,font=('BOLD',25),bg='yellow')
# entry2.place(x=500,y=300)

# #Radio button

# # button
# def action1():
#     n1=int(entry1.get())
#     n2=int(entry2.get())
#     result=n1+n2
#     label3=tk.Label(text=f'your result is : {result}',font = ('BOLD',25),fg='BLUE')
#     label3.place(x=500,y=400)
    
#     messagebox.showinfo("Success","Button Clicked")
# button = tk.Button(window, text='Click Me', font=('BOLD',25),bg='lightgreen',command=action1)
# button.place(x=700, y=500)



# window.mainloop()




"part 5 Radio button and "


# import tkinter as tk 
# from tkinter import messagebox

# window = tk.Tk()
# window.geometry("1500x600")
# window.config(background='#1C2833')

# # Label
# label1 = tk.Label(window, text="This Is My First App", font=('Arial', 25, 'bold'), bg='hotpink')
# label1.place(x=500, y=150)

# # calculator 
# entry1=tk.Entry(window,font=('BOLD',25),bg='yellow')
# entry1.place(x=500,y=200)
# entry2=tk.Entry(window,font=('BOLD',25),bg='yellow')
# entry2.place(x=500,y=300)

# #Radio button
# def display():
#     print(var.get())
# var=tk.StringVar()



# radio1=tk.Radiobutton(window,text='Male',variable=var,value='hello',font=('BOLD',25),bg='skyblue',command=display )
# radio1.place(x=100,y=200)

# radio2=tk.Radiobutton(window,text='Female',variable=var,value='hyy',font=('BOLD',25),bg='skyblue',command=display )
# radio2.place(x=100,y=300)


# # button
# def action1():
#     n1=int(entry1.get())
#     n2=int(entry2.get())
#     result=n1+n2
#     label3=tk.Label(text=f'your result is : {result}',font = ('BOLD',25),fg='BLUE')
#     label3.place(x=500,y=400)
    
#     messagebox.showinfo("Success","Button Clicked")
# button = tk.Button(window, text='Calculated', font=('BOLD',25),bg='lightgreen',command=action1)
# button.place(x=700, y=400)



# window.mainloop()





" Part 5      Check Box "



import tkinter as tk 
from tkinter import messagebox

window = tk.Tk()
window.geometry("1500x600")
window.config(background='#1C2833')

# Label
label1 = tk.Label(window, text="This Is My First App", font=('Arial', 25, 'bold'), bg='hotpink')
label1.place(x=500, y=150)

# calculator 
entry1=tk.Entry(window,font=('BOLD',25),bg='yellow')
entry1.place(x=500,y=200)
entry2=tk.Entry(window,font=('BOLD',25),bg='yellow')
entry2.place(x=500,y=300)

# Radio button
def display_radio():
    print(var.get())

var = tk.StringVar()
radio1 = tk.Radiobutton(window, text='Male', variable=var, value='Male', font=('BOLD',25), bg='skyblue', command=display_radio)
radio1.place(x=100, y=200)

radio2 = tk.Radiobutton(window, text='Female', variable=var, value='Female', font=('BOLD',25), bg='skyblue', command=display_radio)
radio2.place(x=100, y=300)


# button
def action1():
    n1=int(entry1.get())
    n2=int(entry2.get())
    result=n1+n2
    label3=tk.Label(text=f'your result is : {result}',font = ('BOLD',25),fg='BLUE')
    label3.place(x=500,y=400)
    
    messagebox.showinfo("Success","Calculated",)
button = tk.Button(window, text='Calculated', font=('BOLD',25),bg='lightgreen',command=action1)
button.place(x=700, y=500)

#Check box
def display():
    print(option1.get())
    print(option2.get())

option1=tk.BooleanVar()
option2=tk.BooleanVar()

check1=tk.Checkbutton(window, text='CSE',variable=option1, onvalue='True', font=('BOLD',25),bg='lightgreen',command=display)
check1.pack()
check2 = tk.Checkbutton(window, text='ECE',variable=option2, offvalue='False', font=('BOLD',25),bg='lightgreen',command=display)
check2.pack()

button.place(x=700,y=500)
check1.place(x=100,y=400)
check2.place(x=100,y=500)

window.mainloop()


"This is the final code for the starday"

# import tkinter as tk 
# from tkinter import messagebox

# window = tk.Tk()
# window.geometry("1500x600")
# window.config(background='#1C2833')

# # Label
# label1 = tk.Label(window, text="This Is My First App", font=('Arial', 25, 'bold'), bg='hotpink')
# label1.place(x=500, y=150)

# # calculator 
# entry1 = tk.Entry(window, font=('BOLD', 25), bg='yellow')
# entry1.place(x=500, y=200)
# entry2 = tk.Entry(window, font=('BOLD', 25), bg='yellow')
# entry2.place(x=500, y=300)

# # Radio button
# def display_radio():
#     print(var.get())

# var = tk.StringVar()
# radio1 = tk.Radiobutton(window, text='Male', variable=var, value='hello', font=('BOLD',25), bg='skyblue', command=display_radio)
# radio1.place(x=100, y=200)
# radio2 = tk.Radiobutton(window, text='Female', variable=var, value='hyy', font=('BOLD',25), bg='skyblue', command=display_radio)
# radio2.place(x=100, y=300)

# # Button
# def action1():
#     n1 = int(entry1.get())
#     n2 = int(entry2.get())
#     result = n1 + n2
#     label3 = tk.Label(text=f'Your result is : {result}', font=('BOLD',25), fg='BLUE', bg='#1C2833')
#     label3.place(x=500, y=400)
#     messagebox.showinfo("Success", "Button Clicked")

# button = tk.Button(window, text='Calculate', font=('BOLD',25), bg='lightgreen', command=action1)
# button.place(x=700, y=500)

# # Check box
# option1 = tk.BooleanVar()
# option2 = tk.BooleanVar()

# def display_checkbox():
#     if option1.get() or option2.get():
#         if option1.get():
#             print("CSE := True")
#         if option2.get():
#             print("ECE : = True")
#     else:
#         print("All are False")

# check1 = tk.Checkbutton(window, text='CSE', variable=option1, onvalue=True, offvalue=False,font=('BOLD',25), bg='lightgreen', command=display_checkbox)
# check1.place(x=100, y=400)

# check2 = tk.Checkbutton(window, text='ECE', variable=option2, onvalue=True, offvalue=False, font=('BOLD',25), bg='lightgreen', command=display_checkbox)
# check2.place(x=300, y=400)

# window.mainloop()