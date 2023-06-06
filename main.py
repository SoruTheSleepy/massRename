import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from ttkthemes import ThemedTk
from tkinter import ttk
import subprocess

from src.Tooltip import Tooltip
from src.massRename import mass_rename

def launch_program():
  affected_directory = folder_path.get()
  string_to_remove = string_remove.get()
  string_to_add = string_add.get()
  file_extension = file_format.get()
  open_destination_folder = open_destination_folder_var.get()
  delete_files = delete_files_var.get()

  if not affected_directory:
    messagebox.showerror("Error", "Please select a folder.")
    return

  if not string_to_remove:
    messagebox.showerror("Error", "Please insert a string to remove.")
    return
  
  print(file_extension, type(file_extension))
  if not file_extension == "Everything" and file_extension == "" :
    messagebox.showerror("Error", "The provided file extension is invalid.\nMake sure it is either set to Everything or starts with a dot.\n\nEg: .mp3")
    return

  try:
    infos = mass_rename(affected_directory, string_to_remove, string_to_add, file_extension, delete_files)
    if len(infos["original_files"]) == 0 and len(infos["original_files"]) == 0:
      messagebox.showerror("Error", "No file were renamed.\n\nMake sure the string you want to remove exists in at least one file or there is at least one file with the format you selected.")
      return

    messagebox.showinfo("Success", "The program has been successfully executed.")

    if (open_destination_folder):
      print(infos["destination"])
      subprocess.Popen(r'explorer "' + infos["destination"] + '"')
    return

  except Exception as err:
    messagebox.showerror("Error", err)
    return

def close_program():
  window.destroy()

def select_folder():
  folder_selected = filedialog.askdirectory()
  folder_path.set(folder_selected)

window = ThemedTk(theme="equilux")
window.title("Mass Rename")
window.iconbitmap("src/icon.ico")
window.resizable(False, False)
window.configure(bg="#464646")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12), padding=5)
style.configure("TFrame.Title", background="#292929")
style.configure("TFrame.Title.Label", foreground="white")

program_title = ttk.Label(text="Mass Rename © SoruTheSleepy", style="TLabel")
program_title.grid(row=0, column=1, sticky="we", padx=8, pady=8)

folder_label = ttk.Label(text="Directory", style="TLabel")
folder_label.grid(row=1, column=0, sticky="w", padx=8, pady=8)

folder_path = tk.StringVar(value=os.path.dirname(os.path.abspath(__file__)).replace("\\", "/"))
folder_entry = ttk.Entry(textvariable=folder_path, style="TEntry", width=50)
folder_entry.grid(row=1, column=1, sticky="w", padx=8, pady=8)

select_folder_btn = ttk.Button(text="Browse...", command=select_folder, style="TButton")
select_folder_btn.configure(cursor="hand2")
select_folder_btn.grid(row=1, column=2, sticky="w", padx=8, pady=8)

string_remove_label = ttk.Label(text="String to remove", style="TLabel")
string_remove_label.grid(row=2, column=0, sticky="w", padx=8, pady=8)

string_remove = tk.StringVar()
string_remove_entry = ttk.Entry(textvariable=string_remove, style="TEntry", width=50)
string_remove_entry.grid(row=2, column=1, sticky="w", padx=8, pady=8)

string_add_label = ttk.Label(text="String to add", style="TLabel")
string_add_label.grid(row=3, column=0, sticky="w", padx=8, pady=8)

string_add = tk.StringVar()
string_add_entry = ttk.Entry(textvariable=string_add, style="TEntry", width=50)
string_add_entry.grid(row=3, column=1, sticky="w", padx=8, pady=8)

file_format_label = ttk.Label(text="Format to affect", style="TLabel")
file_format_label.grid(row=4, column=0, sticky="w", padx=8, pady=8)

file_format = tk.StringVar()
file_format_selectbox = ttk.Combobox(textvariable=file_format, width=49)
file_format_selectbox.grid(row=4, column=1, sticky="w", padx=8, pady=8)
file_format_selectbox['values'] = [
  'All',
  '.ai',
  '.avi',
  '.bmp',
  '.css',
  '.csv',
  '.dat',
  '.doc',
  '.docx',
  '.exe',
  '.flac',
  '.gif',
  '.html',
  '.ico',
  '.js',
  '.json',
  '.jpg',
  '.jpeg',
  '.log',
  '.m4a',
  '.mdb',
  '.mov',
  '.mp3',
  '.mp4',
  '.pdf',
  '.php',
  '.png',
  '.ppt',
  '.pptx',
  '.psd',
  '.py',
  '.rar',
  '.svg',
  '.tar',
  '.tgz',
  '.tif',
  '.tiff',
  '.txt',
  '.wav',
  '.webm',
  '.wma',
  '.wmv',
  '.xls',
  '.xlsx',
  '.xml',
  '.zip',
]
file_format_selectbox.current(0)
file_format_selectbox.configure(cursor="hand2")

def format_change(e):
  """Function executed when changing the file format

  Args:
      e (tkinter.Event): Event automatically managed
  """
  selected_format = file_format_selectbox.get()
  if selected_format and not selected_format.startswith('.') and not selected_format == "All" :
    file_format_selectbox.set('')

def open_options(e):
  print(e)
  print(type(e))
  file_format_selectbox.event_generate('<Down>')

file_format_selectbox.bind("<<ComboboxSelected>>", format_change)
file_format_selectbox.bind("<Key>", format_change)
file_format_selectbox.bind("<Button-1>", open_options)

open_destination_folder_var = tk.BooleanVar(value=True)
open_destination_folder_checkbox = ttk.Checkbutton(text="Open destination folder", variable=open_destination_folder_var)
open_destination_folder_checkbox.configure(cursor="hand2")
open_destination_folder_checkbox.grid(row=5, column=1, sticky="w", padx=8, pady=8)

delete_files_var = tk.BooleanVar()
delete_files_checkbox = ttk.Checkbutton(text="Delete original files", variable=delete_files_var)
delete_files_checkbox.configure(cursor="hand2")
delete_files_checkbox.grid(row=6, column=1, sticky="w", padx=8, pady=8)

close_button = ttk.Button(text="Close", command=close_program)
close_button.configure(cursor="hand2")
close_button.grid(row=7, column=1, sticky="e", padx=8, pady=8)

launch_button = ttk.Button(text="Run", command=launch_program)
launch_button.configure(cursor="hand2")
launch_button.grid(row=7, column=2, sticky="w", padx=8, pady=8)

window.mainloop()