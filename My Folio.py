import tkinter as tk
import webbrowser
root=tk.Tk()
root.geometry("400x400")
root.title("My Instagram")
root.configure(background="black")

label1=tk.Label(text="Hello BUDDY !! ",fg="green",font=("bold",70),background="black")
label1.place(x=300,y=0)

label2=tk.Label(text="-- Rahul Saini --",fg="blue",font=("bold",20),background="black")
label2.place(x=600,y=130)

label3=tk.Label(text="""Thank you to visit my code .
                This code is develop to make a similar website page 
                using python tkinter library .

                It's very simple to make this , just load the module
                and start coding . Add lables , set color of lable
                backgroung, set lables grids or place them suitabely. 
                """,fg="white",font=("bold",20),background="black")
label3.place(x=0,y=250)

lable4=tk.Label(text="MY Information",font=("calibri",40),background="black",fg="purple")
lable4.place(x=1000,y=200)
label5=tk.Label(text="""NAME:  Rahul Saini 
                AGE:  20
                COLLEGE: Arya College Of engineering
                YEAR:  3rd
                BRANCH: Artificial intelligence and data science
                ADDRESS : JAIPUR RAJASTHAN
                """,font=("calibri",20),background="black",fg="white")
label5.place(x=850,y=300)

label6=tk.Label(text="My Instagram :->",fg='yellow',background="black",font=("bold",15))
label6.place(x=700,y=700)
label7=tk.Label(text="My Linkedin :->",fg='yellow',background="black",font=("bold",15))
label7.place(x=700,y=600)
label8=tk.Label(text="My Github Account :->",fg='yellow',background="black",font=("bold",15))
label8.place(x=700,y=650)

label9=tk.Label(text="Thank you to visit ",bg="red",background="green",font=("bold",30))
label9.place(x=0,y=780)
def open1(event):
    webbrowser.open_new(j)
def open2(event):
    webbrowser.open_new(k)
def open3(event):
    webbrowser.open_new(url)
from googlesearch import search 
query1="rahulsaini22222 instagram account"
query2="linkedin rahul saini 283832290"
url="https://github.com/Rahul86190"
label10=tk.Label(text=url,fg="blue",cursor="hand2")
label10.place(x=1000,y=650)
for j in search (query1,stop=1):
    l1=tk.Label(text=j,fg="blue",cursor="hand2")
    l1.place(x=1000,y=700)
for k in search (query2,stop=1):
    l2=tk.Label(text=k,fg="blue",cursor="hand2")
    l2.place(x=1000,y=600)
    
l1.bind("<Button>",open1)
l2.bind("<Button>",open2)
label10.bind("<Button>",open3)
root.mainloop()