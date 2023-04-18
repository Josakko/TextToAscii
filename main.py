import pyfiglet
import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
import pyperclip


root = ctk.CTk()

window_width = 600
window_hight = 650

monitor_width = root.winfo_screenwidth()
monitor_hight = root.winfo_screenheight()

x = (monitor_width / 2) - (window_width / 2)
y = (monitor_hight / 2) - (window_hight / 2)

root.geometry(f'{window_width}x{window_hight}+{int(x)}+{int(y)}')
root.iconbitmap("JK.ico")
root.title("Text to Ascii Converter")
root.resizable(False, False)

font = "standard"

text = ""
ascii = ""
def convert():
    global ascii
    text = text_entry.get()
    if asciiarea.get(1.0, "end-1c"):
      if not messagebox.askyesnocancel("Warning", "Are you sure you want to lose previously converted text?"):
          return
      else:
          pass
    try:
        ascii = pyfiglet.figlet_format(text, font=font)
        #print(ascii)
        asciiarea.config(state="normal")
        asciiarea.delete("1.0", "end")
        asciiarea.insert("1.0", ascii)
        asciiarea.config(state="disabled")
    except:
        messagebox.showerror("Error", "Please make sure you don't have \nany special characters in your text!")


def copy():
    if ascii != "":
        pyperclip.copy(ascii)
        messagebox.showinfo("Info", "Ascii successfully copied!                         ")
    else:
        messagebox.showerror("Error", "Please convert some text before trying to copy it!")

entry_lbl = ctk.CTkLabel(root, text="Enter text to convert:", font=("Arial", 20))
entry_lbl.pack(ipady=5, anchor="n")

text_entry = ctk.CTkEntry(root, width=300, font=("Arial", 20))
text_entry.pack(pady=15)

confirm_btn = ctk.CTkButton(root, text="Convert", width=300, font=("Arial", 16), command=convert)
confirm_btn.pack(pady=15)

output_frame = ctk.CTkFrame(root)
output_frame.pack(pady=40)

y_scrollbar = Scrollbar(output_frame)
y_scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
        
x_scrollbar = Scrollbar(output_frame, orient=HORIZONTAL)
x_scrollbar.pack(side=ctk.BOTTOM, fill=ctk.X)

asciiarea = Text(output_frame, width=50, height=13, bg="#dbdbdb", font=("Arial", 15), wrap=ctk.NONE, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set, state="disabled")
asciiarea.pack()

y_scrollbar.config(command=asciiarea.yview)
x_scrollbar.config(command=asciiarea.xview)

copy_bnt = ctk.CTkButton(root, text="Copy Ascii", width=300, font=("Arial", 16), command=copy)
copy_bnt.pack()


root.mainloop()
