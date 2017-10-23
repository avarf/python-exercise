import os

"Get the current directory"
curretn_dir = os.getcwd()

print (curretn_dir)

"Change directory"
os.chdir('/home/ali/workspace')
curretn_dir = os.getcwd()
print (curretn_dir)

"Get the list of all the files and folders in the working directory"
object_list = os.listdir()
print(object_list)
print('=============')

"We can work with this object list like a normal python list"
print (object_list[0:2])
print (type(object_list))


"Get a list of all objects in a specific directory"
# print (os.listdir('/home/ali/workspace/Tag_FileManager/Code'))

print('=============')
"Creating new directory"
os.mkdir('/home/ali/workspace/Tag_FileManager/Code/python_file_test')
"I commented out the directory creating code because we cannot create a new directory with the same name each time"

os.chdir('/home/ali/workspace/Tag_FileManager/Code')
print(os.listdir())

print('=============')
"Rename files or directories"
"os.rename('old_name', 'new_name')"

os.rename('python_file_test', 'Renamed_Directory')
print (os.listdir())
os.rename('Renamed_Directory','python_file_test')
print (os.listdir())

print('=============')
"Removing files"
# os.remove()
"Removing empty directory"
# os.rmdir()
"Removing directory with empty subdirectories"
# os.removedirs()

"Removing non-empty directories"
"Recursively delete a directory"
import shutil
shutil.rmtree('python_file_test')
print (os.listdir())

print('=============')
"Copy directory and files"
"Find difference between different copy methods for files"
# shutil.copytree()
# shutil.copy() # Coppy data ???
# shutil.copyfile()

print('=============')
"Cut directory and files"
"Maybe move directory"
"Recursively move a file or directory and works similar to mv command in linux"
# shutil.move()
