#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:00:38 2019

@author: vla35123
"""

import tkinter as tk
from tkinter import Entry, LabelFrame, Checkbutton, Label, Button
import random

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
        self.HodnoceniFrame = LabelFrame (self)
        self.HodnoceniFrame. pack (anchor = tk.W)
        
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
        
        Button (self.OperaceFrame, text = 'Spustit', command = self.Start).grid (row = 5, column = 3)
    
    #### Rovnice ####
        self.a = tk.StringVar()
        self.a.set(0)
        self.operant = tk.StringVar()
        self.operant.set (' + ')
        self.b = tk.StringVar()
        self.b.set(0)
        self.vysledek = tk.StringVar()
        self.vysledek.set(0)
        
        Label (self.RovniceFrame, text = 'Rovnice:').grid(row = 6, column = 0)
        
        self.AEntry = Entry (self.RovniceFrame, state = 'readonly', textvariable = self.a, width = 4)
        self.AEntry.grid (row = 7, column = 0)
        
        self.OperantLab = Label (self.RovniceFrame, textvariable = self.operant)
        self.OperantLab.grid (row = 7, column = 1)
        
        self.BEntry = Entry (self.RovniceFrame, state = 'readonly', textvariable = self.b, width = 4)
        self.BEntry.grid (row = 7, column = 2)
        
        self.RovnaseLab = Label (self.RovniceFrame, text = ' = ')
        self.RovnaseLab.grid (row = 7, column = 3)
        
        self.vysledekEntry = Entry (self.RovniceFrame, textvariable = self.vysledek, width = 4)
        self.vysledekEntry.grid (row = 7, column = 4)
        self.bind ('<Return>', self.kontrola)
    
    #### Hodnoceni ####
        Label (self.HodnoceniFrame, text = 'Hodnoceni').grid(row = 8, column = 0)
        self.OKLabel = Label (self.HodnoceniFrame, text = 'Počítej')
        self.OKLabel.grid (row = 9, column = 0)
        self.StatLabel = Label (self.HodnoceniFrame, text = '0 / 0')
        self.StatLabel.grid (row = 9, column = 3)
      
    def Start (self):
        self.dobre = 0
        self.celkem = 0
        self.Priklady()
    def Priklady (self):
        self.vyber = []
        if  self.ScitaniVar.get() == 1:
            self.vyber.append (' + ')
        if self.OdcitaniVar.get() == 1:
            self.vyber.append (' - ')
        if self.NasobeniVar.get ()== 1:
            self.vyber.append (' * ')
        if self.DeleniVar.get ()== 1:
            self.vyber.append (' / ')
        print (self.vyber)   
        operace = random.choice(self.vyber)
        print(operace)
        
        if operace == ' + ':
            self.CisloA = random.randint (1,50)
            self.CisloB = random.randint (1,50)
            self.Vysledek = self.CisloA + self.CisloB
        
        if operace == ' - ':
            self.CisloA = random.randint (1,50)
            self.CisloB = random.randint (1,self.CisloA)
            self.Vysledek = self.CisloA - self.CisloB
           
        if operace == ' * ':
            self.CisloA = random.randint (1,10)
            self.CisloB = random.randint (1,10)
            self.Vysledek = self.CisloA * self.CisloB
        
        if operace == ' / ':
            self.CisloA = random.randint (1,100)
            self.CisloB = random.randint (1,10)
            self.Vysledek = self.CisloA / self.CisloB
        
        self.a.set(self.CisloA)
        self.b.set(self.CisloB)
        self.operant.set (operace)
    
    def kontrola(self, x):
        try:
            if self.Vysledek == int (self.vysledekEntry.get()):
                self.OKLabel.config (text = 'OK')
                self.dobre += 1
            else:
                self.OKLabel.config (text = 'Spíš ne')
            self.celkem += 1
            self.vysledek.set(0)
            self.StatLabel.config (text = '{0} / {1}'.format(self.dobre, self.celkem))
            self.Priklady()
        except:
            self.OKLabel.config (text = 'Počítej')
        
        
            


app = Application()
app.mainloop()