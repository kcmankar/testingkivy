#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:21:16 2018

@author: kanishka
"""

from kivy.app import App
from tkFileDialog import askopenfilename
from kivy.uix.screenmanager import ScreenManager , Screen, FadeTransition 
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import numpy as np
import matplotlib.pyplot as plt
global X
X=np.array([])
global Y
Y=np.array([])
global f
f = 0
global f1
f1 =0
class MyScreen(ScreenManager):
    def Inputval(self):
        global f 
        f = f+1
        if f==1:
            x=askopenfilename()
            global X1
            X1=np.genfromtxt(x,delimiter=',')
            print(X)
        
    def InputYval(self):
        global f1
        f1 = f1 +1
        if f1==1:
            y=askopenfilename()
            global Y1
            Y1=np.genfromtxt(y,delimiter=',')
            print(Y)
    def graphcreation(self):
        plt.xlabel("X Axis")
        plt.ylabel("Y axis")
        plt.plot(X1,Y1)
        plt.savefig('graph.pdf')
	
    
    def Graphscatter(self):
        plt.xlabel("X Axis")
        plt.ylabel("Y axis")
        plt.scatter(X1,Y1)
        plt.savefig('graphscatter.pdf')
        
        
    

class MainScreen(Screen):
    pass
    
   
class InpScreen(Screen):
    
    pass
   
     
    
   
class SelectScreen(Screen):
    pass
r = Builder.load_file("root.kv")

class RootApp(App):
    def build(self):
        
        
            
        return r
    
if __name__ == "__main__":
    RootApp().run()        