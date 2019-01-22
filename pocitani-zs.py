#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:00:38 2019

@author: vla35123
"""

import tkinter as tk
from tkinter import Entry, LabelFrame, Checkbutton, Label, Button

class Application (tk.Tk):
    name = 'Počítaní'
    
    def __init__(self):
        super().__init__ (className = self.name)
        self.title(self.name)
        
    #### Frames ####
        self.OperaceFrame = LabelFrame (self)
        self.OperaceFrame.pack (anchor = tk.W)
        self.RovniceFrame = LabelFrame (self)
        self.RovniceFrame.pack (anchor = tk.W)
        
    #### Operace ####
        self.ScitaniVar = tk.BooleanVar()
        self.ScitaniVar.set (1)
        self.OdcitaniVar = tk.BooleanVar()
        self.OdcitaniVar.set (0)
        self.NasobeniVar = tk.BooleanVar()
        self.NasobeniVar.set (0)
        self.DeleniVar = tk.BooleanVar()
        self.DeleniVar.set (0)
        
        Label (self.OperaceFrame, text = 'Operace:').grid(row = 0, column = 0)
        
        Checkbutton (self.OperaceFrame, text = '+  ', variable = self.ScitaniVar).grid(row = 1, column = 0)
        Checkbutton (self.OperaceFrame, text = '-   ', variable = self.OdcitaniVar).grid(row = 2, column = 0)
        Checkbutton (self.OperaceFrame, text = '*   ', variable = self.NasobeniVar).grid(row = 3, column = 0)
        Checkbutton (self.OperaceFrame, text = '/   ', variable = self.DeleniVar).grid(row = 4, column = 0)
        
        Button (self.OperaceFrame, text = 'Spustit', command = self.Priklady).grid (row = 5, column = 2)
    
    #### Rovnice ####
        self.x = tk.StringVar()
        self.x.set(0)
        self.operant = tk.StringVar()
        self.operant.set (' + ')
        self.y = tk.StringVar()
        self.y.set(0)
        self.vysledek = tk.StringVar()
        self.vysledek.set(0)
        
        Label (self.RovniceFrame, text = 'Rovnice:').grid(row = 6, column = 0)
        
        self.AEntry = Entry (self.RovniceFrame, state = 'readonly', textvariable = self.x, width = 4)
        self.AEntry.grid (row = 7, column = 0)
        
        self.OperantLab = Label (self.RovniceFrame, textvariable = self.operant)
        self.OperantLab.grid (row = 7, column = 1)
        
        self.BEntry = Entry (self.RovniceFrame, state = 'readonly', textvariable = self.y, width = 4)
        self.BEntry.grid (row = 7, column = 2)
        
        self.RovnaseLab = Label (self.RovniceFrame, text = ' = ')
        self.RovnaseLab.grid (row = 7, column = 3)
        
        self.vysledekEntry = Entry (self.RovniceFrame, textvariable = self.vysledek, width = 4)
        self.vysledekEntry.grid (row = 7, column = 4)
        
        def Priklady (self):
            pass


app = Application()
app.mainloop()