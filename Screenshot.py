import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
root.title('Screenshot')
can = tk.Canvas(root, width=230,height=50, bg="black")
root.attributes('-topmost', 'true')
root.resizable(False,False)
can.pack()

def takeScreenshot():
    SS = pyautogui.screenshot()
    save_path = asksaveasfilename()
    SS.save(save_path+'.png')

ssButton = tk.Button(text="Take Screenshot", command=takeScreenshot,font=10)
can.create_window(111,30,window=ssButton,)

root.mainloop()