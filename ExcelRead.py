from lib2to3.pgen2.pgen import DFAState
import pandas as pd 
from tkinter import *
from tkinter import ttk, filedialog
import os


#tkinter


'''
#code1
file = []

for  i in range(1,13):
      for j in range(17,21):
         
          if int(i) <= 9 :
              i = str(i)
              j = str(j)
              file.append('09AHRPM2422Q1ZN_0'+i+'20'+j+'_R2A.xlsx')
          else:
             i = str(i)
             j = str(j)
             file.append('09AHRPM2422Q1ZN_'+i+'20'+j+'_R2A.xlsx')


#code2
B2B = []
for i in range(0,48):
     if  os.path.isfile(file[i]) == True:
            B2B.append(pd.read_excel(file[i], sheet_name = 1, index_col = 0)) 


#code3
B = []
for i in range(0,len(B2B)):
     B.append(B2B[i].dropna(axis=0,how='all'))


#code4
frames = []

for i in range(0,len(B2B)):
      frames.append(B[i]) 
result = pd.concat(frames)


#code5
fResult = result[result["Unnamed: 2"].str.contains("-Total") == True]


#res = fResult.groupby("Unnamed: 2")
fResult[['Unnamed: 5','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 15','Unnamed: 18','Unnamed: 19','Unnamed: 20']] = fResult[['Unnamed: 5','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 15','Unnamed: 18','Unnamed: 19','Unnamed: 20']].astype(str)
FinalResult =  fResult.groupby('Unnamed: 1')[['Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20']].agg('#'.join).reset_index()
#res.size().sort_values(ascending=False)
'''
#tkinter



# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

# Add a Canvas widget
canvas = Canvas(win, background= "white")

# Draw a rectangle in Canvas and inherit the background color of Canvas
canvas.create_rectangle(50,50,350,190, outline="black", fill= canvas["background"])
canvas.pack()
win.mainloop()