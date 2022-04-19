#Script to remove "y2mate" from the begining of all filenames in Music folder
import os

#Change current working directory
os.chdir(r'C:\Users\lucas\Desktop\Music')

#Iterate over directory
for file in os.listdir():
    #Split filename by '-', creating a list with all parts
    nombreSeparado = (file.split('-'))
    #Rename file as the last item on the list
    os.rename(file, nombreSeparado[-1])