"""Automatic Ping and Traceroute Program by Varoon Doone"""""

import sys
import os
import subprocess
from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import re


# Declaring variables
programName = "notepad.exe"
# google_ip is variable used in tracert function.
google_ip = "-d 8.8.8.8" # "-d"; To not resolve ip addresses to hostnames.
dash_n = " -n 15" # for ping command/function, NOT the single_ping() function


def update(msg): # to update progress bar window
    task_progress.set(msg)
    window.update()


def resource_path(relative_path):  # used to get path for cmd_icon.png; program icon
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def tracert(num, manual_ad):
    pb['value'] += 50
    update("Running Tracert command")
    window.after(1000)
    if manual_ad != "":
        cmd = "tracert " + manual_ad
        tracert_msg = "IP Address(" + manual_ad + ")"
    else:
        cmd = "tracert " + google_ip
        tracert_msg = "Google's DNS Server Address(8.8.8.8)"
    result = subprocess.check_output(cmd, shell=True)
    result = result.decode('UTF-8').rstrip()
    if num == 0:
        f = open(path, 'w')
    else:
        f = open(path, 'a')
    f.write("\nResults for Traceroute to " + tracert_msg + ":\n")
    f.write("\n------------------------------------------------------- \n")  # adding a seperator
    f.write(result)
    f.write("\n\n------------------------------------------------------- \n")  # adding a seperator
    f.close()  # close file when finish
    pb.config(mode='determinate')
    pb['value'] += 50


def ping(num):
    pb['value'] += 25
    update("Running Ping command")
    window.after(1000)
    loopback_ip = "127.0.0.1"
    update("Pinging Loopback Address(" + loopback_ip + ")")
    cmd = "ping " + loopback_ip + dash_n
    result = subprocess.check_output(cmd, shell=True)  # runs command and returns result in Bytes
    result = result.decode('UTF-8').rstrip()  # converts results from Bytes into a String
    if num == 0:
        f = open(path, 'w')
    else:
        f = open(path, 'a')
    f.write("\nResults for Computer's Loopback Address(127.0.0.1):\n")
    f.write("\n------------------------------------------------------- \n")  # adding a seperator
    f.write(result)  # write result to file
    f.write("\n\n------------------------------------------------------- \n")  # adding a seperator
    f.close()  # close file when finish


# ----------------Default gateway-----------------------------------

    # Try to get default gateway; gate_ip
    cmd = "ipconfig /all"
    result = subprocess.check_output(cmd, shell=True)
    result = result.decode('UTF-8').rstrip()
    try:
        gate_ip = re.search('Default Gateway . . . . . . . . . : (.+?)\n', result)
        gate_ip = gate_ip.group(1)
        f = open(path, 'a')  # 'w' as in write to file
        f.write("\nDefault Gateway: " + gate_ip)
        f.write("\n------------------------------------------------------- \n")  # adding a seperator
    except Exception:
        gate_ip = "1.1.1.1"  # set 1.1.1.1 as default ip address if Default Gateway not found
        f = open(path, 'a')
        f.write("\nDefault Gateway not found. Using program's substitute IP value: 1.1.1.1\n")
        f.write("\n------------------------------------------------------- \n")  # adding a seperator

    update("Checking for Default Gateway")
    if gate_ip == "1.1.1.1":
        pb['value'] += 25
        update("Default Gateway not found. Using a substitute IP: 1.1.1.1")  # calling update(msg)
        window.after(1000)
        update("Pinging Program's Default Gateway Address(" + gate_ip.strip() + ")")
    else:
        pb['value'] += 25
        update("Default Gateway found. Getting IP Address")
        window.after(1000)
        update("Pinging Default Gateway Address(" + gate_ip.strip() + ")")

    # Default Gateway ping
    cmd = "ping " + gate_ip + dash_n
    result = subprocess.check_output(cmd, shell=True)
    result = result.decode('UTF-8').rstrip()
    f = open(path, 'a')
    if gate_ip == "1.1.1.1":
        f.write("\nResults for Program's Default Gateway Address(" + gate_ip.strip() + "):\n")
    else:
        f.write("\nResults for Default Gateway Address(" + gate_ip.strip() + "):\n")
    # Note: ".strip()" to remove new line space after ip address
    f.write("\n------------------------------------------------------- \n")  # adding a seperator
    f.write(result)
    f.write("\n------------------------------------------------------- \n")  # adding a seperator
    pb['value'] += 25

# ----------------Default gateway-----------------------------------

    # Google DNS Server Ping
    go_ip = "8.8.8.8"
    update("Pinging Google DNS Server Address(" + go_ip + ")")
    cmd = "ping " + go_ip + dash_n
    result = subprocess.check_output(cmd, shell=True)
    result = result.decode('UTF-8').rstrip()
    f = open(path, 'a')
    f.write("\nResults for Google DNS Server Address(8.8.8.8):\n")
    f.write("\n------------------------------------------------------- \n")  # adding a seperator
    f.write(result)
    f.write("\n------------------------------------------------------- \n")  # adding a seperator
    f.close()  # close file when finish
    pb['value'] += 25


def single_ping(num, input_box):
    pb['value'] += 50
    update("Running Ping command")
    cmd = "ping " + input_box
    result = subprocess.check_output(cmd, shell=True)  # runs command and returns result in Bytes
    result = result.decode('UTF-8').rstrip()  # converts results from Bytes into a String
    if num == 0:
        f = open(path, 'w')
    else:
        f = open(path, 'a')
    f.write("\nResults for Ping to IP Address(" + input_box + "):\n")
    f.write("\n------------------------------------------------------- \n")  # adding a seperator
    f.write(result)  # write result to file
    f.write("\n\n------------------------------------------------------- \n")  # adding a seperator
    f.close()  # close file when finish
    pb['value'] += 50


def var_states():
    try:
        pb.grid(column=0, row=9, sticky=W, padx=35)  # Put when a command is called; e.g. Ping or Tracert
        input_box = manual_add.get() # getting data from tk entry box
        if var2.get() == 2 and input_box == "":
            messagebox.showerror(title="Input Error", message="Manual value box cannot be empty")
            return
        try:
            os.remove(path)
        except FileNotFoundError:
            pass

        if var1.get() == 1:
            update("Running Ping command")
            if var2.get() == 2:
                single_ping(0, input_box)
            else:
                ping(0)
            subprocess.Popen([programName, path])
            window.after(250, window.destroy)
        elif var1.get() == 2:
            update("Running Tracert command")
            if var2.get() == 2:
                tracert(0, input_box)
            else:
                tracert(0, "")
            subprocess.Popen([programName, path])
            window.after(250, window.destroy)
        elif var1.get() == 3:
            pb.config(mode='indeterminate')
            update("Running Ping and Traceroute Commands")
            window.after(1000)
            if var2.get() == 2:
                single_ping(1, input_box)
                tracert(1, input_box)
                pb.config(mode='determinate')
                pb['value'] = 100
            else:
                ping(1)
                tracert(1, "")
            subprocess.Popen([programName, path])
            window.after(250, window.destroy)
    except Exception as e:
        messagebox.showerror(title="Unknown Error",
                             message="Automatic Ping and Traceroute Program was closed or was unable to run")
        directory_e = os.getcwd()
        path_e = directory_e.replace("\\", "\\\\") + "\\\\ping_traceroute_error_log.txt"
        f = open(path_e, 'w')
        f.write('\nSee Errors Below: \n\n%s' % e)
        f.close()
        window.after(250, window.destroy)


# ----------For user input------------
def click(*args):
    manual_add.config(fg="black", state='normal')
    if manual_add.get() == "Enter IP Address":
        manual_add.delete(0, 'end')


def display_input():
    if var2.get() == 1:
        if manual_add.get() == "":
            manual_add.insert(0, "Enter IP Address")
            manual_add.config(fg="#808080")
        manual_add.config(state='disabled')
        manual_add.grid_remove()
    elif var2.get() == 2:
        manual_add.bind("<Button-1>", click)
        manual_add.grid(column=0, row=7, sticky=W, pady=6, padx=35)


# ----------End of section for user input------------

# -------------------root window ------------------------------------------------------------------------------

window = Tk()
window.title("Automatic Ping and Traceroute")
window.geometry("340x360")
window.resizable(False, False)  # This code helps to disable windows from resizing
window.eval('tk::PlaceWindow . center')

icon = PhotoImage(file=resource_path("cmd_icon.png"))
window.iconphoto(True, icon)  # assign converted image to window

task_progress = StringVar()

directory = os.getcwd() # Get current working directory
path = directory.replace("\\", "\\\\") + "\\\\ping_traceroute_results.txt" # append text file name to store output

spaceLabel = Label(window, text="Please select a command below:", font=('Helvetica', 12, 'bold'))
spaceLabel.grid(column=0, row=0, padx= 2, pady=5, sticky= W)

var1 = IntVar()
check1 = Radiobutton(window, text="Ping", variable=var1, value=1, font=('Segoe UI', 10))
check1.grid(column=0, row=1, sticky=W, padx = 11)
check1.invoke()

check2 = Radiobutton(window, text="Traceroute", variable=var1, value=2, font=('Segoe UI', 10))
check2.grid(column=0, row=2, sticky=W, padx = 11)

check3 = Radiobutton(window, text="Both Ping & Traceroute Commands", variable=var1, value=3, font=('Segoe UI', 10))
check3.grid(column=0, row=3, sticky=W, padx= 11)

# ----------------------------------------------------------
# Adding manual input
spaceLabel = Label(window, text="Type of IP Address:", font=('Helvetica', 12, 'bold'))
spaceLabel.grid(column=0, row=4, sticky=W, pady= 11, padx= 2)


var2 = IntVar()
manual_add = tk.Entry(window, width=28, font=('Segoe UI', 10)) # manual value text input window

check4 = Radiobutton(window, text="Automatic; Use Program's Values", variable=var2, value=1,
                     command=display_input, font=('Segoe UI', 10))
check4.grid(column=0, row=5, sticky=W, padx= 11)
check4.invoke()

check5 = Radiobutton(window, text="Manual; Use a Custom Value", variable=var2, value=2,
                     command=display_input, font=('Segoe UI', 10))
check5.grid(column=0, row=6, sticky=W, padx= 11)

# ----------------------------------------------------------

submit_button = Button(window, text=' Submit ', command=var_states, font=('Segoe UI', 10),
                       relief='solid', border=1)
submit_button.grid(column=0, row=8, sticky= W, pady=15, padx=120)


# progressbar
pb = Progressbar(window, orient='horizontal', mode='determinate', length=250)

taskLabel = Label(window, textvariable=task_progress, font=('Segoe UI', 10))
taskLabel.grid(column=0, row=10, sticky='', pady= 5, padx=35)


window.mainloop()

