# sendmail_gui.py - GUI for sending mail.

import tkinter as tk
from tkinter import END
import smtplib
import imaplib
import email
import html2text

def sendmail_gui():
    root = tk.Tk()
    host_label = tk.Label(root, text="SMTP Host: ")
    host_label.grid(row=0, column=0)
    host_entry = tk.Entry(root)
    host_entry.grid(row=0, column=1)
    port_label = tk.Label(root, text="Port: ")
    port_label.grid(row=1, column=0)
    port_entry = tk.Entry(root)
    port_entry.grid(row=1, column=1)
    address_label = tk.Label(root, text="Email address: ")
    address_label.grid(row=2, column=0)
    address_entry = tk.Entry(root)
    address_entry.grid(row=2, column=1)
    pwd_label = tk.Label(root, text="Password: ")
    pwd_label.grid(row=3, column=0)
    pwd_entry = tk.Entry(root, show="•")
    pwd_entry.grid(row=3, column=1)
    target_label = tk.Label(root, text="Target: ")
    target_label.grid(row=4, column=0)
    target_entry = tk.Entry(root)
    target_entry.grid(row=4, column=1)
    content_label = tk.Label(root, text="Content: ")
    content_label.grid(row=5, column=0)
    content_entry = tk.Entry(root)
    content_entry.grid(row=5, column=1)
    def smtp_send():
        host = host_entry.get()
        port = port_entry.get()
        email_address = address_entry.get()
        user_pwd = pwd_entry.get()
        target = target_entry.get()
        content = content_entry.get()
        mail = smtplib.SMTP(str(host), int(port))
        mail.ehlo()
        mail.starttls()
        mail.login(email_address,user_pwd)
        mail.sendmail(email_address,target, content)
        host_entry.delete(0, END)
        port_entry.delete(0, END)
        address_entry.delete(0, END)
        pwd_entry.delete(0, END)
        target_entry.delete(0, END)
        content_entry.delete(0, END)
        mail.close()
    sendmail = tk.Button(text="Send", command=smtp_send)
    sendmail.grid(row=6, column=0)
    root.mainloop()