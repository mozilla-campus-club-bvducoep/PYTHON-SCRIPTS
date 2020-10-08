from tkinter import messagebox
import webbrowser
import time
import random
import os
        
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
i=0
while i<20:
    sites = random.choice(['google.com','youtube.com','facebook.com'])
    visit = 'http://{}'.format(sites)
    webbrowser.open_new_tab(visit)
    try:
        c = webbrowser.get('chrome')
        c.open_new(visit)
    except:
        pass
    seconds=random.randrange(2)
    time.sleep(seconds)
    i = i+1
    
x=messagebox.showinfo('Alert','Do you wish to shutdown your computer ?')
if x == False:
    exit() 
else:
    os.system("shutdown /s /t 1") 

