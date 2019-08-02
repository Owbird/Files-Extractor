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
#root.iconbitmap("scan.ico")

# Setting the size of the app
root.geometry("300x300")

# Making the size fixed
root.resizable(0, 0)

# Setting the background color of the app
root.configure(bg="light grey")

class Events(object):

	# Directory of the folder to beautify
	dir = ''
	archive = False

	def select_dir(event):

		# Displaying the folder dialog
		dir = filedialog.askdirectory(title="Select folder to save files")
		
		# Saving the path to the folder
		Events.dir = dir
		
	def check(event):

		if ans.get() == 1:
		
				archive_name_label.configure(state="disabled")
				archive_name.configure(state="disabled")
				
				Events.archive = False
				
		else:
		
				archive_name_label.configure(state="normal")
				archive_name.configure(state="normal")
				
				Events.archive = True

	def done(event):
	
		# Retrieving path
		paste_path = Events.dir
		
		# Getting extension
		ext = ext_entry.get()
		
		# validating the extension
		if ext == "" or dir == "":
		
			# Alerting the user
			messagebox.showwarning("Blank Entry", "Entry can't be left blank!")
			
			# Exiting app
			sys.exit()
		
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

		# Setting copied files to 0
		
		folder = paste_path.split('/')[-1]
		os.chdir(paste_path)
		copied = len(glob(f"*{ext}"))
		
		# Alerting the user
		if copied > 0:

			done_label['text'] = f"Succesfully extracted {copied} {ext} files"
			done_label['bg'] = "green"
			
		else:
		
			done_label['text'] = f"Sorry found no {ext} files"
			done_label['bg'] = "red"
			
		if Events.archive:
			
			os.chdir('../')
			shutil.make_archive(archive_name.get(), 'zip', folder)
			shutil.rmtree(folder)
			
		messagebox.showinfo("Done", "Complete!")
			
# Describing text area to user
ext_label = Label(root, text="Extension of files (eg. txt, mp3, jpg, mp4):")
ext_label.grid(row=0, column=0, sticky=W)

# Text to enter extension
ext_entry = Entry(root)
ext_entry.focus_set()
ext_entry.grid(row=1, column=0, sticky=W)

# Button to select folder
select_dir_btn = Button(root, text="Select folder to save files")
select_dir_btn.grid(row=2, column=0, sticky=W)
select_dir_btn.bind("<Button-1>", Events.select_dir)

ans = IntVar()

check_button = Checkbutton(root, text="Create Archive", variable=ans)
check_button.grid(row=3, column=0, sticky=W)
check_button.bind("<Button-1>", Events.check)

archive_name_label = Label(root, text="Archive name: ")
archive_name_label.configure(state="disabled")
archive_name_label.grid(row=4, column=0, sticky=W)

archive_name = Entry(root)
archive_name.configure(state="disabled")
archive_name.grid(row=5, column=0, sticky=W)

# Done button to start the process
done_btn = Button(root, text="Done", bg="light blue")
done_btn.grid(row=6, column=0, sticky=W)
done_btn.bind("<Button-1>", Events.done)

# About info
about_txt = f"""
Files Extractor
version 2.0
Author: Owbird
https://github.com/owbird
"""

# Displaying the about info
about_label = Label(root, text=about_txt, padx=100, bg='light grey')
about_label.grid(row=7, column=0)

# Displaying status
done_label = Label(root, text="")
done_label.grid(row=8, column=0, sticky=W)

# App stays till user ends it
root.mainloop()
