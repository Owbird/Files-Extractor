from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from glob import glob
import os
import shutil
import sys

# Creating the app
root = Tk()

# Setting the title of the app
root.title("Files Extractor")

# Setting the icon of the file
if os.name == "nt":

	root.iconbitmap("scan.ico")

# Setting the size of the app
root.geometry("450x400")

# Making the size fixed
root.resizable(0, 0)

# Setting the background color of the app
root.configure(bg="light grey")

class Events(object):

    # Directory of the folder to beautify
    dir = ''
    
    # Choice of user for archiving
    archive = False

    def select_dir(event):

        # Displaying the folder dialog
        dir = filedialog.askdirectory(title="Select folder to save files")
        
        # Saving the path to the folder
        Events.dir = dir
        
    def check(event):

        # if archive not selected
        if ans.get() == 1:
                
                # Disabling entry 
                archive_name_label.configure(state="disabled")
                archive_name.configure(state="disabled")
                
                Events.archive = False
                
        else:
            
                # Enabling entry
                archive_name_label.configure(state="normal")
                archive_name.configure(state="normal")
                
                # Moving cursor to entry
                archive_name.focus_set()
                
                Events.archive = True

    def done(event):
    
        # Retrieving path
        try:
        
       		os.mkdir(os.path.join(Events.dir, "Files Extractor"))
       	
       	except FileExistsError:
       	
       		pass
       		
        paste_path = os.path.join(Events.dir, "Files Extractor")
        # Getting extension
        ext = ext_entry.get()

        print(f"[*] Extracting  all {ext} files...")
        
        # validating the extension
        if ext == "":
        
            # Alerting the user
            messagebox.showwarning("Empty Field", "Extension Can't Be Left Blank")
            
            # Exiting app
            sys.exit()
        
        # Validating the path to save the files to
        if paste_path == "":
            
            # If blank, saving them to their current directory
            paste_path = os.getcwd()
                
        # checking for type of os
        root_directory = "c:/" if os.name == "nt" else "/"
        
        # Going through the computer
        for root, sub, files in os.walk(root_directory):

            # Targeting files
            for file in files:

                # Setting copy path
                copy_path = f"{root}/{file}"

                # Verifying extension
                if file.endswith(f'.{ext}') or (file.startswith('.') and file.endswith(f'.{ext}')):

                    try:
                
                        # Copy file
                        shutil.copy(copy_path, paste_path)
                    
                    # Checking for errors               
                    except (shutil.SameFileError, FileNotFoundError, PermissionError, OSError):
                        
                        continue    
                        
                    # Showing current process
                    print(f'[*] Extracted {file}')
        
        # Changing directory
        os.chdir(paste_path)
        
        # Counting copied files 
        copied = len(glob(f"*{ext}"))
        
        # Alerting the user
        if copied > 0:

            done_label['text'] = f"Succesfully extracted {copied} {ext} files"
            done_label['bg'] = "green"
            
        else:
        
            done_label['text'] = f"Sorry found no {ext} files"
            done_label['bg'] = "red"
            
        # If archive was selected
        if Events.archive:
            
            # Setting the name
            name = archive_name.get()
            
            # Validating name
            if name == "":
                
                # If name is blank, setting name to "{ext} files"
                name = f"{ext} files"
            
            # Change directory
            os.chdir('../')
            
            # Archiving folder
            try:
                
                shutil.make_archive(name, 'zip', "Files Extractor")
            
            except PermissionError:
            
                messagebox.showwarning("Error", "Couldn't Create Archive, Check Folder")

            # Remove folder
            shutil.rmtree("Files Extractor")
           
        # Alertin user on completing 
        messagebox.showinfo("Done", "Complete!")
            
# Extension label
ext_label = Label(root, text="Extension(eg. txt, mp3, jpg, mp4):")
ext_label.grid(row=0, column=0, sticky=W)

# Area to enter extension
ext_entry = Entry(root)
ext_entry.focus_set()
ext_entry.grid(row=0, column=1)

# Space
space = Label(root, bg="light grey").grid(row=1, column=0)

# Button to select folder
select_dir_btn = Button(root, text="Select folder to save files")
select_dir_btn.grid(row=2, column=0, sticky=W)
select_dir_btn.bind("<Button-1>", Events.select_dir)

space = Label(root, bg="light grey").grid(row=3, column=0)

# Variable for checkbox
ans = IntVar()

# Checkbox
check_button = Checkbutton(root, text="Create Archive", variable=ans)
check_button.grid(row=4, column=0, sticky=W)
check_button.bind("<Button-1>", Events.check)

# archive name label
archive_name_label = Label(root, text="Archive name: ")
archive_name_label.configure(state="disabled")
archive_name_label.grid(row=5, column=0, sticky=W)

# Area to enter name 
archive_name = Entry(root)
archive_name.configure(state="disabled")
archive_name.grid(row=5, column=1)

space = Label(root, bg="light grey").grid(row=6, column=0)

# Done button to start the process
done_btn = Button(root, text="Done", bg="light blue")
done_btn.grid(row=7, column=0, sticky=W)
done_btn.bind("<Button-1>", Events.done)

# About info
about_txt = f"""
Files Extractor
version 2.0
Author: Owbird
https://github.com/owbird
"""

# Displaying the about info
about_label = Label(root, text=about_txt, bg='light grey')
about_label.grid(row=8, column=0)

# Displaying status
done_label = Label(root, text="")
done_label.grid(row=9, column=0, sticky=W)

# App stays till user ends it
root.mainloop()
