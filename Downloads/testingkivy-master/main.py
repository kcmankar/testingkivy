# python2
# -*- coding: utf-8 -*-
"""

@author: kcmankar
"""

from kivy.app import App
from kivy import Config
Config.set('graphics', 'multisamples', '0')
from tkFileDialog import askopenfilename  
""" Tkinters askopenfile is used as it is easy to use and stores the path of the file which is then later used by numpy genfromtext"""
from kivy.uix.screenmanager import ScreenManager , Screen, FadeTransition 
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import numpy as np
import matplotlib.pyplot as plt
global f
f = 0
global f1
f1 =0
class MyScreen(ScreenManager):
    def Inputval(self):
        global f 
        f = f+1
        if f==1:
"""The if statement and the global variables are declared because when the program ran the askopenfile opened atomatically without clicking on the button used for asking the address of the file whoch contains our numbers. """
            x=askopenfilename()
"""This x variable stores the address of our file which contains numbers."""
            global X1
            X1=np.genfromtxt(x,delimiter=',')#this X1 now generates an array of numbers from the 
            #text file we selected and it is a csv(comma seperated values) file.
            print(X1)
        
    def InputYval(self):
        global f1
        f1 = f1 +1
        if f1==1:
            y=askopenfilename()"""Same thing is repeated for y to get numbers from a text file.""""
            global Y1
            Y1=np.genfromtxt(y,delimiter=',')
            print(Y1)
    def graphcreation(self):#This is where graph is created and saved.
        plt.xlabel("X Axis")
        plt.ylabel("Y axis")
        plt.plot(X1,Y1)#It is a line plot.
        plt.savefig('graph.pdf')
	
    
    def Graphscatter(self):#This is used for scatter plot
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
# This loads our main kv file i.e root.kv
class RootApp(App):
    def build(self):
        #Main app 
        
            
        return r
    
if __name__ == "__main__":
    RootApp().run()        
