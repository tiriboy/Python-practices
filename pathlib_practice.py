import pyinputplus
import os


def accept_dir():
   
   try:
     path = pyinputplus.inputFilepath(prompt='Enter a the path of the file to be moved: ', limit=3)
     new_dir = pyinputplus.inputFilepath(prompt='Enter the directory path to move this folder to: ', limit=3)
     if os.path.exists(path) and os.path.isdir(new_dir):
        new_path = os.path.join(new_dir,path.strip().split('\\')[-1])
        os.rename(path,new_path)
     list_files = os.listdir(new_path)
     for file in list_files:
        print(file)   
   except Exception as e:
      print(e)
      return

accept_dir()     