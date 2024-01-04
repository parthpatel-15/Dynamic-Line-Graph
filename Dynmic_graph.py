#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 1 15:34:50 2022

@author: Parth Patel
studnet number : 301207843
"""

import threading 
from tkinter import Canvas, Frame, BOTH
import tkinter as tk
import random 
import time 



class DynamicGraph(Frame):
    entry = "0"
    height = 600
    rList =[]
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.update()
    
    def initUI(self):
        self.master.title(' Dyanmic Line Graph')
        self.pack(fill=BOTH , expand =1)
        
        canvas = Canvas(self)
        
        for x in range (50):
            self.rList.append(int(random.randint(10, 60)))
            
        def sButton():
            start = threading.Thread(target = randValue())
            start.setDaemon(True)
            
        def randValue():
            
            for x in range (10,1000):
                self.rList.pop(0)
                self.rList.append(int(random.randint(10,200 )))
                
                p1 = (self.height)-self.rList[0]*random.uniform(1,2)
                p2 = (self.height)-self.rList[1]*random.uniform(1,2)
                p3 = (self.height)-self.rList[2]*random.uniform(1,2)
                p4 = (self.height)-self.rList[3]*random.uniform(1,2)
                p5 = (self.height)-self.rList[4]*random.uniform(1,2)
                p6 = (self.height)-self.rList[5]*random.uniform(1,3)
                p7 = (self.height)-self.rList[6]*random.uniform(1,2)
                p8 = (self.height)-self.rList[7]*random.uniform(1,2)
                p9 = (self.height)-self.rList[8]*random.uniform(1,2)
                p10 = (self.height)-self.rList[9]*random.uniform(1,2)
                p11 = (self.height)-self.rList[10]*random.uniform(1,2)
                
                
                
                canvas.coords(line1, 200,p2,150,p1)
                canvas.coords(line2, 250,p3,200,p2)
                canvas.coords(line3, 300,p4,250,p3)
                canvas.coords(line4, 350,p5,300,p4)
                canvas.coords(line5, 400,p6,350,p5)
                canvas.coords(line6, 450,p7,400,p6)
                canvas.coords(line7, 500,p8,450,p7)
                canvas.coords(line8, 550,p9,500,p8)
                canvas.coords(line9, 600,p10,550,p9)
                canvas.coords(line10, 650,p11,600,p10)
                
                time.sleep(0.60)
                
                
                root.update()
                
                
        btn = tk.Button(text = ' Go', width=20, command =lambda: sButton())
        canvas.create_window(400, 20 , window = btn)
        
        line1 = canvas.create_line(200,0,150,0, fill= "green", dash=(4,2))
        line2 = canvas.create_line(250,0,200,0, fill= "green", dash=(4,2)) 
        line3 = canvas.create_line(300,0,250,0, fill= "green", dash=(4,2)) 
        line4 = canvas.create_line(350,0,300,0, fill= "green", dash=(4,2)) 
        line5 = canvas.create_line(400,0,350,0, fill= "green", dash=(4,2)) 
        line6 = canvas.create_line(450,0,400,0, fill= "green", dash=(4,2)) 
        line7 = canvas.create_line(500,0,450,0, fill= "green", dash=(4,2))
        line8 = canvas.create_line(550,0,500,0, fill= "green", dash=(4,2))
        line9 = canvas.create_line(600,0,550,0, fill= "green", dash=(4,2))
        line10 = canvas.create_line(650,0,600,0, fill= "green", dash=(4,2))
        
        
        
        
        canvas.create_line(150,20,150,600, fill= "black")
        canvas.create_line(150,600, 700, 600 , fill= "black")
        canvas.create_text(140, 575, text="25-", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(140, 550, text="50-", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(135, 500, text="100-", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(135, 400, text="200-", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(135, 300, text="300-", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(135, 200, text="400-", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(135, 100, text="500-", fill="black", font=('Helvetica 15 bold'))
        
        
        label = canvas.create_text(100, 10, text="number of people", fill="black", font=('Helvetica 15 bold'))
       
       
        canvas.pack(fill = BOTH , expand =1)

root = tk.Tk()

ex = DynamicGraph()

root.geometry('800x650+300+300')

root.mainloop()              
                
                
            