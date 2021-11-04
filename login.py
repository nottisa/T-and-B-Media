#IMPORT#################################################
import smtplib,os,secrets, register
import tkinter as tk
from replit import db
usemongodb = False
########################################################

#AUTHLOGIN##############################################
def authlogins():
  global displaywidget
  global usernameinput
  global passwordinput
  global usernamebox
  global passwordbox
  global actualpassword
  global cookie
  global userid
  global loginwindow
  displaywidget = 1
  usernameinput = usernamebox.get()
  passwordinput = passwordbox.get()
  errortext = tk.Label(
  text="The username or password is incorrect.",
  foreground="red",
  background="light gray",
  width=0,
  height=0
  )
  if usemongodb:
    global mongodbclient
    global db
    print("Mongo DB is not currentlly supported, an error may occur.")
    db=mongodbclient.test
  else:
   try:
    actualpassword = db[usernameinput]
    actualpassexists = 1
   except:
      actualpassexists = 0
   if actualpassexists != 0 and actualpassword == passwordinput:
     cookiemake = 1
     while cookiemake == 1:
      userid = db[usernameinput + "id"]
      possiblecookie = secrets.token_urlsafe(38)
      try:
        cookie = db["cookie" + possiblecookie]
      except:
        cookiemake = 0
        cookie = possiblecookie
        db["cookie" + possiblecookie] = possiblecookie
        loginwindow.destroy()
        print("Servers: Connected")
   else:
     if displaywidget == 1:
         errortext.pack()
     displaywidget = displaywidget + 1
########################################################

#WATCHFORFOCUSED########################################
#username WATCHFORFOCUSED
def user_entry_focus(event):
  global usernamebox
  global userinputfocused
  userinputfocused = 1
  usernamebox.delete(0, tk.END)
#password WATCHFORFOCUSED
def pass_entry_focus(event):
  global passwordbox
  global passinputfocused
  passinputfocused = 1
  passwordbox.delete(0, tk.END)
########################################################

#SETUPLOGINWINDOW#######################################
def setuploginwindow():
  global usernamebox
  global passwordbox
  global newuserbutton
  newuserbutton = tk.Button(
    text="Create an Account",
    width=15,
    height=1,
    fg="blue",
    command=register.dummy
)
  logintext1 = tk.Label(
  text="T&B Login:",
  foreground="#000000",
  background="white",
  width=60,
  height=0
  )
  usernamebox = tk.Entry()
  passwordbox = tk.Entry()
  loginbutton = tk.Button(
    text="Login!",
    width=15,
    height=2,
    bg="lightgray",
    fg="black",
    command=authlogins
  )
  logintext1.pack()
  usernamebox.pack()
  passwordbox.pack()
  loginbutton.pack()
  newuserbutton.pack()
  usernamebox.insert(0, "Username")
  passwordbox.insert(0,"Password")
  usernamebox.bind("<FocusIn>", user_entry_focus)
  passwordbox.bind("<FocusIn>", pass_entry_focus)
#MAKEWINDOW######################################
def makeloginwindow(nameOfWindow):
  global loginwindow
  loginwindow = tk.Tk()
  loginwindow.geometry("400x268")
  loginwindow.maxsize(400, 2681)
  loginwindow.title(nameOfWindow)
  loginwindow.geometry("540x300")
  setuploginwindow()