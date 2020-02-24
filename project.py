import glob
import os
import re
import sys
import tkinter as tk

root =tk.Tk()
mystring =tk.StringVar(root)
e1 = tk.Entry(root,textvariable = mystring,width=100,fg="blue",bd=3,selectbackground='violet').pack()
button1 = tk.Button(root, 
                text='Submit', 
                fg='White', 
                bg= 'dark green',height = 1, width = 10, command = root.destroy).pack()

root.mainloop()

path = "./"
directory = os.listdir(path)
list_of_files = []
files = []
result = []

#gets every file in a specified directory
for filename in glob.glob('*.txt'): 
    file = open(filename, "r")
    files.append(filename)

    #list of words in every file
    list_of_words = []
    
    #gets every line from a file
    for line in file:
        #removes punctuation
        line = re.sub(r'[^\w\s]', '', line)

        #gets every word in a line
        for word in line.split():
            #makes all words lowercase (type insensitive)
            word = word.lower()
            #adds word to the total words list of the file
            list_of_words.append(word)
    
    #add list_of_words to the total list of files
    list_of_files.append(list_of_words)

#############33query = sys.stdin.readline() #string input
query = mystring.get()
keywords = re.sub(r'[^\w\s]', '', query)
keywords = keywords.split()


query = query.replace('!', 'not ')
query = query.replace('&&', 'and')
query = query.replace('||', 'or')

for document in list_of_files:
    test = query

    for keyword in keywords:
        if (keyword in document):
            test = re.sub(r"\b%s\b" %keyword , '1', test)

    for keyword in keywords:
        if (keyword != 1):
            test = re.sub(r"\b%s\b" %keyword , '0', test)
    
    try:
        if (eval(test)):
            result.append(list_of_files.index(document))
    except:
        print("An error has occured")

for i in result:
    print(files[i])


