#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import csv
axisX =[]
axisY =[]

with open("output.csv") as file:
    reader = csv.reader(file)
    for col in reader:
        axisX.append(col[1])
        axisY.append(col[0])
plt.plot(axisX, axisY)
plt.show()


# In[3]:


import tkinter as tk
import matplotlib as plot
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox as mb
from tkinter import ttk 


def callback(event):
        mb.showinfo(title=None, message='files converted'+event,icon='info')


# In[6]:


class IDI(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        tk.Tk.wm_title(self,"Data Analysis")
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in (StartPage,DigiGraphPage,StructuredDataPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)
    
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        


# In[7]:


class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(
        self,
        text="Welcome to\n \n ...",
        foreground="orange",  # Set the text color to white
        background="black" ,  # Set the background color to black
        width=50,
        height=5,
        )
        label.pack()
        
        button1 = tk.Button(
            self,
            width=30,
            height=3,
            text="Digitize Graph",
            command=lambda : controller.show_frame(DigiGraphPage)
        )
        button2 = tk.Button(
            self,
            text="Structured Data",
            width=30,
            height=3,
            command=lambda : controller.show_frame(StructuredDataPage)
        )
        button1.pack(pady=10,padx=10)
        button2.pack(pady=10,padx=10)


# In[8]:


class DigiGraphPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(
        self,
        text="Digitize Graph Section",
        foreground="orange",  # Set the text color to white
        background="black" ,  # Set the background color to black
        width=50,
        height=5,
        )
        label.pack()
        
        button1 = tk.Button(
            self,
            fg="blue",
            text="Digitize Graph",
            width=30,
            height=3,
        )
        button2 = tk.Button(
            self,
            fg="blue",
            text="Main Page",
            width=30,
            height=3,
            command=lambda : controller.show_frame(StartPage)
        )
        button1.pack(pady=10,padx=10)
        button2.pack(pady=10,padx=10)


# In[9]:


class StructuredDataPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(
        self,
        text="Structured Files and Data Section",
        foreground="orange",  # Set the text color to white
        background="black" ,  # Set the background color to black
        width=50,
        height=5,
        )
        label.pack()
        
        button1 = tk.Button(
            self,
            fg="blue",
            text="Digitize Graph",
            width=30,
            height=3,
        )
        
        button2 = tk.Button(
            self,
            fg="blue",
            text="Main Page",
            width=30,
            height=3,
            command=lambda : controller.show_frame(StartPage)
        )
        button1.pack(pady=10,padx=10)
        button2.pack(pady=10,padx=10)


# In[10]:


app = IDI()
app.mainloop()

