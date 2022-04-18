#Script to remove "y2mate" from the begining of all filenames in Music folder
import os

os.chdir(r'C:\Users\lucas\Desktop\Music')

for file in os.listdir():
    nombreSeparado = (file.split('-'))
    os.rename(file, nombreSeparado[-1])