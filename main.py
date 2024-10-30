####IMPORT##############################################
import tkinter as tk
from keep_alive import keep_alive
import secrets, sys, os, time, register, login
from replit import db
from pprint import pprint
########################################################

####INITIALIZE##########################################
key = os.environ['Key']
Software_Unlock = os.environ['Software_Unlock']
runLoadingDots = True
userinputfocused = 0
passinputfocused = 0
usemongodb = 0
displaywidget = 1
class Error(Exception):
    """Base class for other exceptions"""
    pass
class KeyInvalidError(Error):
    """Error: code; 1; Key Invalid."""
    pass
class basicerror(Error):
    """An unknown error occured."""
    pass
#######################################################
def registernewuser():
  print("created new user!!")

def deleteallcookies():
  global db
  cookiesExist = True
  while cookiesExist:
    cookies = db.keys()
    if any("cookie" in string for string in cookies):
      matching = [s for s in cookies if "cookie" in s]
      del db[matching[0]]
    else:
      cookiesExist = False

def addds():
  global db
  db[" id"] = "1"

def waithere(waitTime, window):
  var = tk.IntVar()
  window.after(waitTime, var.set, 1)
  window.wait_variable(var)

def start(nameOfWindow, window):
  window.title(nameOfWindow)
  window.geometry("540x300")


def fadeText(textToFade):
  text = textToFade
  fadingtext1pt1 = tk.Label(
  text=text,
  foreground="#000000",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt2 = tk.Label(
  text=text,
  foreground="#191919",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt3 = tk.Label(
  text=text,
  foreground="#323232",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt4 = tk.Label(
  text=text,
  foreground="#4B4B4B",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt5 = tk.Label(
  text=text,
  foreground="#646464",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt6 = tk.Label(
  text=text,
  foreground="#7D7D7D",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt7 = tk.Label(
  text=text,
  foreground="#969696",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt8 = tk.Label(
  text=text,
  foreground="#AFAFAF",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt9 = tk.Label(
  text=text,
  foreground="#C8C8C8",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt10 = tk.Label(
  text=text,
  foreground="#E1E1E1",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt11 = tk.Label(
  text=text,
  foreground="#FAFAFA",
  background="white",
  width=60,
  height=16
  )
  fadingtext1pt12 = tk.Label(
  text=text,
  foreground="#FFFFFF",
  background="white",
  width=60,
  height=16
  )

  
  ####FADE-EFFECT#######################################
  fadingtext1pt1.pack()
  waithere(200,loadingwindow)
  fadingtext1pt1.pack_forget()
  fadingtext1pt2.pack()
  waithere(200,loadingwindow)
  fadingtext1pt2.pack_forget()
  fadingtext1pt3.pack()
  waithere(200,loadingwindow)
  fadingtext1pt3.pack_forget()
  fadingtext1pt4.pack()
  waithere(200,loadingwindow)
  fadingtext1pt4.pack_forget()
  fadingtext1pt5.pack()
  waithere(200,loadingwindow)
  fadingtext1pt5.pack_forget()
  fadingtext1pt6.pack()
  waithere(200,loadingwindow)
  fadingtext1pt6.pack_forget()
  fadingtext1pt7.pack()
  waithere(200,loadingwindow)
  fadingtext1pt7.pack_forget()
  fadingtext1pt8.pack()
  waithere(200,loadingwindow)
  fadingtext1pt8.pack_forget()
  fadingtext1pt9.pack()
  waithere(200,loadingwindow)
  fadingtext1pt9.pack_forget()
  fadingtext1pt10.pack()
  waithere(200,loadingwindow)
  fadingtext1pt10.pack_forget()
  fadingtext1pt11.pack()
  waithere(200,loadingwindow)
  fadingtext1pt11.pack_forget()
  fadingtext1pt12.pack()
  waithere(200,loadingwindow)
  fadingtext1pt12.pack_forget()
  """
  #000000
  #191919
  #323232
  #4B4B4B
  #646464
  #7D7D7D.
  #969696
  #AFAFAF
  #C8C8C8
  #E1E1E1
  #FAFAFA
  #FFFFFF
  """



def loadingdots(text):
  loadingtext1pt1 = tk.Label(
  text=text + " ..",
  foreground="#000000",
  background="white",
  width=60,
  height=16
  )
  loadingtext1pt2 = tk.Label(
  text=text + ". .",
  foreground="#191919",
  background="white",
  width=60,
  height=16
  )
  loadingtext1pt3 = tk.Label(
  text=text + ".. ",
  foreground="#323232",
  background="white",
  width=60,
  height=16
  )
  loadingtext1pt4 = tk.Label(
  text=text + "...",
  foreground="#323232",
  background="white",
  width=60,
  height=16
  )
  loadingtext1pt1.pack()
  waithere(300,loadingwindow)
  loadingtext1pt1.pack_forget()
  loadingtext1pt2.pack()
  waithere(300,loadingwindow)
  loadingtext1pt2.pack_forget()
  loadingtext1pt3.pack()
  waithere(300,loadingwindow)
  loadingtext1pt3.pack_forget()
  loadingtext1pt4.pack()
  waithere(300,loadingwindow)
  loadingtext1pt4.pack_forget()

loadingwindow = tk.Tk()
start("T&B Media - Loading", loadingwindow)
fadeText("Welcome, to T&B Media")

for x in range(0, 5):
  loadingdots("Loading")

if key == Software_Unlock:
  print("Pass: code; 1; Key valid.")
  
else:
  start("Key Invalid", loadingwindow)
  keyinvalidtext1pt1 = tk.Label(
  text="Your key is invalid, please try a diffrent key or buy a license.",
  foreground="#000000",
  background="white",
  width=60,
  height=16
  )
  keyinvalidtext1pt1.pack()
  print("An error has occured.")
  raise KeyInvalidError

loadingwindow.destroy()
login.makeloginwindow("T&B - Login")
#addds()
deleteallcookies()
keep_alive() 

register.startregistration()
