'''
                                    ***Database***

📚 Database Basics
🔹 What is Data?
Data = Raw facts and figures.

Example: "John", 23, "Indore" — these are just values without context.

🔹 What is Raw Data?
Raw Data = Mix of useful and irrelevant information.

It needs cleaning before analysis.

🔄 ETL Process in Data Analytics
ETL is the first step in data analytics. It prepares raw data for storage and analysis.

Step	Meaning	What Happens
E	Extraction	Collect data from sources (files, databases, APIs)
T	Transformation	Clean, format, and structure the data
L	Loading	Save the transformed data into a database (DBMS)
🧠 Think of ETL like cooking:

Extract ingredients → Transform them into a dish → Load it onto a plate.

📊 EDA – Exploratory Data Analysis
After ETL, we use EDA to understand and clean the data further.

🔍 EDA Tasks:
Handle missing values: Fill or remove blanks.

Remove unstructured data: Clean messy formats.

Visualize: Create charts and graphs to find patterns.

Example Workflow:
Raw Data → ETL → Cleaned Data → EDA → Visuals → Insights

---------------------------------------------------------------------------------------------------------------------------------------------------------------

🗃️ What Is a Database?
A database is a system used to store, manage, and retrieve large amounts of data efficiently.

🧱 Types of Data in Databases

1️⃣ Structured Data (Relational)
Stored in tables (rows and columns).

Uses SQL (Structured Query Language).

Examples: Employee records, product inventory.

🔧 Tools:
MySQL: Popular SQL-based database.

SQLite3: Lightweight SQL database used in Python projects.

python
import sqlite3
conn = sqlite3.connect('mydata.db')

2️⃣ Unstructured Data (Non-Relational)
Stored in flexible formats like JSON or XML.

Doesn’t follow table structure.

Uses NoSQL databases.

🔧 Tools:
MongoDB: Stores data as documents (JSON-like).

Ideal for dynamic or nested data.

json
{
  "name": "Arpit",
  "skills": ["Python", "SQL", "DevOps"]
}

⚙️ Summary Table
Type	Format	Language	Example Tool	Use Case
Structured	Tables	SQL	MySQL, SQLite3	Banking, Inventory
Unstructured	JSON, XML	NoSQL	MongoDB	Social Media, Logs

🐍 Python Integration
You're using SQLite3 in Python, which is perfect for:

Small projects

Local storage

Quick prototyping

python
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)"

'''

# import sqlite3
# connection = sqlite3.connect('student.db') # always remember to write the filename with extension
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE if not exists users (id INTEGER, name varchar(30))")
# ''' cursor.execute("INSERT INTO users values(2,'jay verma'),(3,'rohit'),(4,'dhoni')")'''

# # insertion of data using a variable
# id = 5
# name = 'ram'
# cursor.execute("INSERT INTO users values(?,?)",(id,name))
# connection.commit() # used to save the changes 
# connection.close()
# print("success")

# import sqlite3
# connection = sqlite3.connect('student.db') # always remember to write the filename with extension
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE if not exists registration (id INTEGER, name varchar(30), gender varchar(30),course varchar(20))")

# import tkinter as tk 
# from tkinter import messagebox
# from tkinter import ttk

# window = tk.Tk()
# window.geometry("1500x600")
# window.config(background='pink')

# def dropdata(event):
#     global gen
#     gen = com.get()

# def submit():
#     name = cursor.execute(f'select {e1} from registration')
#     print(name)
    
# def login():
#     w2 = tk.Tk()
#     w2.geometry("1500x600")
#     w2.config(background='pink')
#     global e1,e2
#     Llab1 = tk.Label(w2,text='enter the id',font=('Times New Roman','25','bold'),bg='#E6E6FA')
#     Llab1.place(x=500,y=150)
#     e1 = tk.Entry(window, font=('Times New Roman',25,'bold'), bg='#E6E6FA')
#     e1.place(x=850, y=150)
#     Llab2 = tk.Label(w2,text='enter the course',font=('Times New Roman','25','bold'),bg='#E6E6FA')
#     Llab2.place(x=500,y=150)
#     e2 = tk.Entry(window, font=('Times New Roman',25,'bold'), bg='#E6E6FA')
#     e2.place(x=850, y=150)
#     Lid = e1.get()
#     Lcourse = e2.get()
# def clear():
#     entry1.delete()

# def register():  # event is optional
#     id = entry1.get()
#     name = entry2.get()
#     gender = gen
#     course = com.get()
#     cursor.execute("INSERT INTO registration values(?,?,?,?)", (id, name, gender, course))
#     print("Success")
#     messagebox.showinfo("Success", "Registration completed!")
#     clear
#     # window.destroy()
    

# # window 1
# Label1 = tk.Label(window,text="please enter the user id",font=('Times New Roman','25','bold'),bg='#E6E6FA')
# Label1.place(x=500,y=150)
# entry1 = tk.Entry(window, font=('Times New Roman',25,'bold'), bg='#E6E6FA')
# entry1.place(x=850, y=150)
# Label2 = tk.Label(window,text="please enter the name",font=('Times New Roman','25','bold'),bg='#E6E6FA')
# Label2.place(x=500,y=200)
# entry2 = tk.Entry(window, font=('Times New Roman',25,'bold'), bg='#E6E6FA')
# entry2.place(x=850, y=200)

# var = tk.StringVar()
# radio1 = tk.Radiobutton(window, text='Male', variable=var, value='Male', font=(25), bg='skyblue')
# radio1.place(x=500, y=250)
# radio2 = tk.Radiobutton(window, text='Female', variable=var, value='Female', font=(20), bg='skyblue')
# radio2.place(x=700, y=250)

# data = ['CSE','AIML','DS','CSIT']
# com = ttk.Combobox(window,values=data,font=(20))
# com.bind('<<ComboboxSelected>>',dropdata)
# com.place(x=650,y=300)

# button = tk.Button(window,text="register",font=('Times New Roman',25,'bold'),command=register)
# button.place(x=650,y=350)

# button2 = tk.Button(window,text="login",font=('Times New Roman',25,'bold'),command=login)
# button2.place(x=650,y=350)

# window.mainloop()

# connection.commit() # used to save the changes 
# cursor.close()
# connection.close()

'''finding the total number of characters in a string
str = input()
count = 0
for i in str:
    if i != ' ':
        count+=1
print(count)
'''

''' 
This tkinter file can be converted using the pyinstaller,
which is used to convert the file intoo the executable file.
firstly check if the pyinstaller is installed or not 
if it is then you have to open the file 
pyinstaller --onefile filename.py
'''

'''
                                           *** File Handling in Python ***

Python provides two ways to handle files:
1. `open()` method
2. `with open()` context manager

📌 Syntax:
varname = open('filename.extension', 'mode')

📌 Modes:
1. 'w' → Write (overwrites content)
2. 'a' → Append (adds to existing content)
3. 'r' → Read

🛠️ Note:
- Use `write()` for both 'w' and 'a' modes.
- When using `open()`, always close the file using `varname.close()`.
- To delete a file, refer to the code shown below.

'''
# write
# f = open('demofile.text','w')
# f.write("hello world")
# f.close()

# append 
# f = open('demofile.text','a')
# f.write("hello world")
# f.close()

# read all
# f = open('demofile.text','r')
# a = f.read()
# print(a)
# f.close()

# read by line
# f = open('demofile.text','r')
# for i in f:
#     print(i)
# f.close()

# to delete the file
# import os 
# os.remove('demofile.text')

'with open'
# with open('demofile.txt','r') as f:
#     for i in f:
#         print(i)

# with open('demofile.txt','a') as f:
#     f.write('this is the third line')

# with open('demofile.txt','w') as f:
#     f.write('the file got overwritten')

'''
                            *** seek() and tell() in File Handling ***

🔹 seek(offset)  
Used to move the file pointer to a specific position (in bytes) from the beginning of the file.

🔹 tell()  
Returns the current position of the file pointer (in bytes).

🧠 Example:
# f.seek(0) → moves pointer to the beginning
# f.tell() → returns current pointer position

'''
# f = open('demofile.txt','r')
# f.seek(7)
# a = f.read(6)
# print(f.tell())
# print(a)
# f.close()

''' in the exception handling the finally block is used for the program which you want to execute always'''