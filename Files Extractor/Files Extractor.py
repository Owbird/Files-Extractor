from glob import glob
import os
import shutil
import sys
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("ext", help="Base extension to extract")
parser.add_argument("path", help="Path to save files to")
parser.add_argument("-z", "--zip", help="Archive extracted files with a name")

args = parser.parse_args()

# About
print('            #####################################')
print('            #                                   #')
print('            #        Files Extractor            #')
print('            #        version 1.0                #')
print('            #        Author: Owbird             #')
print('            #        https://github.com/owbird  #')
print('            #                                   #')
print('            #####################################')

print('\n\n')

# Validating path
if not os.path.isdir(args.path):

	# Alerting user
	print(f"[!] {args.path} does not exist!")
	
	# Exiting program
	sys.exit()
	
# Checking for format
if not args.ext[0] == '.':

	args.ext = f'.{args.ext}'

print()

# Showing current process
print(f'[*] Copying all {args.ext} to {args.path}')

print()

# checking for type of os
root_directory = "c:/" if os.name == "nt" else "/"

try:

	os.mkdir(os.path.join(args.path, "Files Extractor"))

except FileExistsError:
   	
	pass 
# Going through the computer
for root, sub, files in os.walk(root_directory):

	# Targeting files
	for file in files:

		# Setting copy path
		copy_path = f"{root}/{file}"

		# Verifying extension
		if file.endswith(args.ext) or (file.startswith('.') and file.endswith(args.ext)):

			try:
				
				# Copy file
				shutil.copy(copy_path, os.path.join(args.path, "Files Extractor"))
			
			# Checking for errors					
			except (shutil.SameFileError, FileNotFoundError, PermissionError, OSError):
				
				continue

			# Showing current process
			print(f'[*] Extracted {file}')

# Setting copied files to 0

os.chdir(os.path.join(args.path, "Files Extractor"))
copied = len(glob(f"*{args.ext}"))

# If nothing was copied
if copied == 0:

	# Prompt user
	print(f'[*] No {args.ext} files found')
	
	# Exit
	sys.exit()

else:

	# Showing current process
	print(f'[*] Done! copied {copied} files')

print()

# If zip option was added
if args.zip:

	# Showing current process
	print('[*] Archiving...')
	
	# Getting folder of saved files
	folder = args.path.split('/')[-1]
	
	# Changing directory
	os.chdir('../')
	
	# Creating zip
	shutil.make_archive(args.zip, 'zip', "Files Extractor")

	# Deleting folder
	shutil.rmtree("Files Extractor")
	
	# Showing current process
	print('[*] Archiving done!')

