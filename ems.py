from tkinter import*
from tkinter.messagebox import*
from pymongo import*
from tkinter.scrolledtext import*
import matplotlib.pyplot as plt
import re
from requests import *
     
def f1():
    mw.withdraw()
    aw.deiconify()

def f2():
    mw.withdraw()
    vw.deiconify()

def f3():
    mw.withdraw()
    uw.deiconify()

def f4():
    mw.withdraw()
    dw.deiconify()

def f6():
    aw.withdraw()
    mw.deiconify()

def f7():
    vw.withdraw()
    mw.deiconify()

def f8():
    uw.withdraw()
    mw.deiconify()

def f9():
    dw.withdraw()
    mw.deiconify()

def f10():
    mw.withdraw()
    cw.deiconify()

def f5():
    cw.withdraw()
    mw.deiconify()


mw = Tk()
mw.title("E.M.S")
mw.geometry("700x700+100+50")
f = ("Times New Roman", 20, "bold")

add_btn = Button(mw, text="Add", width="15", font=f, command=f1)
add_btn.pack(pady=20)

view_btn = Button(mw, text="View", width="15", font=f, command=f2)
view_btn.pack(pady=20)

update_btn = Button(mw, text="Update", width="15", font=f, command=f3)
update_btn.pack(pady=20)

delete_btn = Button(mw, text="Delete", width="15", font=f, command=f4)
delete_btn.pack(pady=20)

chart_btn = Button(mw, text="Charts", width="15", font=f, command=f10)
chart_btn.pack(pady=20)

def temperauture5():
    url = "https://api.openweathermap.org/data/2.5/weather?q=kalyan&appid=b64af53b051f87a4e6457582c489b950"
    try:
       res = get(url)
       data = res.json()
       temper =  data['main']['temp']
       temper2 = temper - 273.15
       temperature01.configure(text=f"{temper2:.2f}°C")
    
    except Exception as e:
        showerror("Issue", e)

temperature00 = Label(mw, text="Temperature:", font=f)
temperature00.place(y=550, x=380)
temperature01 = Label(mw, font=f, wraplength=500)
temperature01.place(y=550, x=568)
temperauture5()

def loc():
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q=kalyan&appid=b64af53b051f87a4e6457582c489b950"
        res = get(url)
        data = res.json()
        city_name = data['name']
        location_info = f"{city_name}"
        location1.configure(text=location_info)

    except Exception as e:
        showerror("Issue", e)

location = Label(mw, text="Location:", font=f)
location.place(y=550, x=40)
location1 = Label(mw, font=f, wraplength=500)
location1.place(y=550, x=175)
loc()


aw = Tk()
aw.title("Add Emp")
aw.geometry("700x700+100+50")
f = ("Times New Roman", 20, "bold")


emp_id = Label(aw, text="Enter the employee id", font=f)
emp_id.pack(pady=20)

emp_id_btnt = Entry(aw, font=f)
emp_id_btnt.pack(pady=10)

emp_name = Label(aw, text="Enter employee name", font=f)
emp_name.pack(pady=20)

emp_name_btn = Entry(aw,  font=f)
emp_name_btn.pack(pady=10)

emp_salary = Label(aw, text="Enter employee salary", font=f)
emp_salary.pack(pady=20)

emp_salary_btn = Entry(aw,  font=f)
emp_salary_btn.pack(pady=10)

def save():
    try:
        con = MongoClient("localhost", 27017)
        db = con["28oct"]
        coll = db["emp"]

        emp_id1 = emp_id_btnt.get()
        emp_name_btn1 = emp_name_btn.get()
        emp_salary_btn1 = emp_salary_btn.get()

        if emp_id1 == "":
            showerror("Issue", "Do not leave the employee ID empty")

        elif emp_name_btn1 == "":
            showerror("Issue", "Do not leave the employee name empty")

        elif emp_salary_btn1 == "":
            showerror("Issue", "Do not leave the employee salary empty")

        elif re.search(r'[!@#$%^&*()]', emp_id1):
            showerror("Issue", "Special characters are not allowed in employee ID")

        elif not emp_id1.isdigit():
            showerror("Issue", "Do not enter alphabets in employee ID")

        elif re.search(r'[!@#$%^&*()]', emp_name_btn1):
            showerror("Issue", "Special characters are not allowed in employee name")

        elif re.search(r'[!@#$%^&*()]', emp_salary_btn1):
            showerror("Issue", "Special characters are not allowed in employee salary")

        elif emp_name_btn1.isdigit():
            showerror("Issue", "Employee Name should not contain numbers")

        elif coll.find_one({"id_number": emp_id1}):
            showinfo("Employee Exists", "Employee already exists")

        else:
            doc = {"id_number": emp_id1, "name": emp_name_btn1, "salary": emp_salary_btn1}
            coll.insert_one(doc)
            showinfo("Created", "Record Created")

        emp_id_btnt.delete(0, END)
        emp_name_btn.delete(0, END)
        emp_salary_btn.delete(0, END)
        emp_id_btnt.focus()

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()


save_button = Button(aw, text="Save", width="15", font=f, command=save)
save_button.pack(pady=20)

back_button = Button(aw, text="Back", width="15", font=f, command=f6)
back_button.pack(pady=20)
aw.withdraw()

vw = Tk()
vw.title("view Employee")
vw.geometry("700x700+100+50")
f = ("Times New Roman", 20, "bold")


view_emp_data = ScrolledText(vw, font=f, width=28, height=15)
view_emp_data.pack(pady=10)

def view():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["28oct"]
        col = db["emp"]
        data = col.find()
        view_emp_data.delete(1.0, END)
        view_emp_data.focus()

        for d in data:

            view_emp_data.insert(END, f"Employee ID: {d['id_number']}\n")
            view_emp_data.insert(END, f"Employee Name: {d['name']}\n")
            view_emp_data.insert(END, f"Employee Salary: {d['salary']}\n \n")     

    except Exception as e:
        showerror("Error", e)
    finally:
        if con is not None:
            con.close()

view_button = Button(vw, text="View", width="15", font=f, command=view)
view_button.pack(pady=20)

back_button = Button(vw, text="Back", width="15", font=f, command=f7)
back_button.pack(pady=20)
vw.withdraw()

uw = Tk()
uw.title("update Employee")
uw.geometry("700x700+100+50")
f = ("Times New Roman", 20, "bold")

def update_emp():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["28oct"]
        col = db["emp"]

        empid = emp_id_btn66.get()
        empname = emp_nameooo_btn.get()
        empsalary = emp_salary_btnc.get()

        if empid == "":
            showerror("issue", "Do not keep the employee Id empty")
        elif empname == "":
            showerror("issue", "Do not keep the employee name empty")
        elif empsalary == "":
            showerror("issue", "Do not keep the employee salary empty")
        elif (empid=="") or (empname=="") or (empsalary==""):
            showerror("issue", "Do not keep any of the employee details empty")
        elif any(char in "!@#$%^&*()" for char in empsalary):
            showerror("Issue", "Do not enter the special characters in employee salary")
        elif any(char in "!@#$%^&*()" for char in empname):
            showerror("Issue", "Do not enter the special characters in employee name")
        elif any(char in "!@#$%^&*()" for char in empid):
            showerror("Issue", "Do not enter the special characters in employee ID")
        elif not empid.isdigit():
            showerror("Issue", "Do not enter the alphabets in employee ID")
        elif not empname.isalpha():
            showerror("Issue", "Do not enter the numbers in employee name")

        else:
            existing_employee = col.find_one({"id_number": empid})
            if existing_employee:
                col.update_one({"id_number": empid}, {"$set": {"name": empname, "salary": empsalary}})
                showinfo("Updated", "Employee details updated successfully")
            else:
                showinfo("Issue", "Employee not found")
    
        emp_id_btn66.delete(0, END)
        emp_nameooo_btn.delete(0, END)
        emp_salary_btnc.delete(0, END)
        emp_id_btn66.focus()

    except Exception as e:
        showerror("issue", e)
    
    finally:
        if con is not None:
            con.close()

        
emp_id = Label(uw, text="Enter the employee id", font=f)
emp_id.pack(pady=20)

emp_id_btn66 = Entry(uw, font=f)
emp_id_btn66.pack(pady=10)

emp_nameooo = Label(uw, text="Enter employee name", font=f)
emp_nameooo.pack(pady=20)

emp_nameooo_btn= Entry(uw,  font=f)
emp_nameooo_btn.pack(pady=10)

emp_salary = Label(uw, text="Enter employee salary", font=f)
emp_salary.pack(pady=20)

emp_salary_btnc = Entry(uw,  font=f)
emp_salary_btnc.pack(pady=10)

update_button = Button(uw, text="update", width="15", font=f, command=update_emp)
update_button.pack(pady=20)

back_button = Button(uw, text="Back", width="15", font=f, command=f8)
back_button.pack(pady=20)
uw.withdraw()

dw = Tk()
dw.title("Delete Employee")
dw.geometry("700x700+100+50")
f = ("Times New Roman", 20, "bold")
 

emp_id_label = Label(dw, text="Enter the employee id", font=f)
emp_id_label.pack(pady=20)

emp_id_btn123 = Entry(dw, font=f)
emp_id_btn123.pack(pady=10)

def delete():
    try:
        con = MongoClient("localhost", 27017)
        db = con["28oct"]
        coll = db["emp"]
        emp_id1 = emp_id_btn123.get()

        if emp_id1 == "":
            showerror("Issue", "Do not keep the employee ID empty")
        elif  any(char in "!@#$%^&*()" for char in emp_id1):
            showerror("Issue", "Do not enter the special characters in employee ID")
        elif not emp_id1.isdigit():
            showerror("Issue", "Do not enter alphabets in employee ID")

        else:
            count = coll.count_documents({"id_number": emp_id1})
            if count == 1:
                coll.delete_one({"id_number": emp_id1})
                showinfo("Info", "Employee Deleted")
            else:
                showinfo("Issue", "Employee with this ID not found")

        emp_id_btn123.delete(0, END)
        emp_id_btn123.focus()

    except Exception as e:
        showerror("Error", e)
    finally:
        if con is not None:
            con.close()

emp_delete = Button(dw, text="Delete", width="15", font=f, command=delete)
emp_delete.pack(pady=20)
  
back_button = Button(dw, text="Back", width="15", font=f, command=f9)
back_button.pack(pady=20)
dw.withdraw()

cw = Tk()
cw.title("Top five salaried Employees")
cw.geometry("700x700+100+50")
f = ("Times New Roman", 20, "bold")

def gen_chart():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["28oct"]
        col = db["emp"]

        top_employees = list(col.find().sort("salary",-1).limit(5)) 

        employee_names = [employee["name"] for employee in reversed(top_employees)]
        employee_salaries = [employee["salary"] for employee in reversed(top_employees)]

        plt.figure(figsize=(8, 6))
        plt.bar(employee_names, employee_salaries) 
        plt.xlabel("Emp Names")
        plt.ylabel("Salary")
        plt.title("Top 5 Salaried Employees")

        plt.tight_layout()
        plt.show()

    except Exception as e:
        showerror("Error", e)
    finally:
        if con is not None:
            con.close()


show_button = Button(cw, text="Show Chart", width="15", font=f, command=gen_chart)
show_button.pack(pady=20)

back_button = Button(cw, text="Back", width="15", font=f, command=f5)
back_button.pack(pady=20)
cw.withdraw()


def close():
    if askokcancel("Quit", "Do you want to exit?"):
        mw.destroy()
        aw.destroy()
        vw.destroy()
        dw.destroy()
        uw.destroy()
        cw.destroy()

mw.protocol("WM_DELETE_WINDOW", close)
aw.protocol("WM_DELETE_WINDOW", close)
vw.protocol("WM_DELETE_WINDOW", close)
dw.protocol("WM_DELETE_WINDOW", close)
uw.protocol("WM_DELETE_WINDOW", close)
cw.protocol("WM_DELETE_WINDOW", close)

mw.mainloop()