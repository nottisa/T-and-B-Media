#IMPORT#################################################
import smtplib,os
import tkinter as tk

#VARIABLES##############################################
key = os.environ['Key']
Software_Unlock = os.environ['Software_Unlock']
class Error(Exception):
    """Base class for other exceptions"""
    pass
class KeyInvalidError(Error):
    """Error: code; 1; Key Invalid."""
    pass
class basicerror(Error):
    """An unknown error occured."""
    pass

#FUNCTIONS##############################################
def startregistration():
  global loadingwindow
  loadingwindow = tk.Tk()
  start("Registration - Loading", loadingwindow)
  for _ in range(7):
    loadingdots("")

def waithere(waitTime, window):
  var = tk.IntVar()
  window.after(waitTime, var.set, 1)
  window.wait_variable(var)

def start(nameOfWindow, window):
  window.title(nameOfWindow)
  window.geometry("540x300")

def user_entry_focus():
  global usernamebox, userinputfocused
  userinputfocused = 1
  usernamebox.delete(0, tk.END)

def pass_entry_focus():
  global passbox, passinputfocused
  passinputfocused = 1
  passbox.delete(0, tk.END)

def repass_entry_focus():
  global repassbox, repassinputfocused
  repassinputfocused = 1
  repassbox.delete(0, tk.END)

def email_entry_focus():
  global emailbox, emailinputfocused
  emailinputfocused = 1
  emailbox.delete(0, tk.END)

def loadingdots(text):
  loadingtext1pt1 = tk.Label(
  text=text + " ..",
  foreground="#000000",
  background="white",
  width=60,
  height=16,
  font=("Arial", 35)
  )
  loadingtext1pt2 = tk.Label(
  text=text + ". .",
  foreground="#191919",
  background="white",
  width=60,
  height=16,
  font=("Arial", 35)
  )
  loadingtext1pt3 = tk.Label(
  text=text + ".. ",
  foreground="#323232",
  background="white",
  width=60,
  height=16,
  font=("Arial", 35)
  )
  loadingtext1pt4 = tk.Label(
  text=text + "...",
  foreground="#323232",
  background="white",
  width=60,
  height=16,
  font=("Arial", 35)
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

def dummy():
  print("this is a dummy")
