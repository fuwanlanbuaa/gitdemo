from tkinter import *
import tkinter.messagebox as mb
from pylab import mpl
import matplotlib.pyplot as plt
import webbrowser
import re
mpl.rcParams['font.sans-serif'] = ['SimHei'] 

stoplist1=open('stoplist.txt','r')
stoplist=stoplist1.read()
#the first part of the programme
#include diaoyong shujuku
#important stoplist