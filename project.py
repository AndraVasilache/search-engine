import glob
import os
import re
import sys
import tkinter as tk


##start of the first GUI window
root =tk.Tk()
root.title("Open Source Search Engine")
root.geometry("700x500")
root.config(bg = "light blue")

description = tk.Label(root, bg = "light blue", text = " ")
description.pack()
description = tk.Label(root, bg = "light blue", text = "Welcome to Open Source Search Engine, an app made entirely in")
description.pack()
description = tk.Label(root, bg = "light blue", text = "Python. Find the documents from any directory that match your search!")
description.pack()
description = tk.Label(root, bg = "light blue", text = "Your search needs to look something like:")
description.pack()
description = tk.Label(root, bg = "light blue", text = "word1 && (word2 || (word3 && !(word4)))")
description.pack()
description = tk.Label(root, bg = "light blue", text = "Happy searching!")
description.pack()
description = tk.Label(root, bg = "light blue", text = " ")
description.pack()

#input variable
mystring = tk.StringVar(root)

#interactables
entry = tk.Entry(root, textvariable = mystring, width = 50, fg = "blue", bd = 3, selectbackground = 'violet').pack()
button = tk.Button(root, text = 'Submit', fg = 'White', bg = '#49A', height = 1, width = 10, command = root.destroy).pack()

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

try:
    query = mystring.get()
except:
    print("An error has occured. Something must not be right with the input")
    sys.exit()

if (not query):
    print("Your input is empty!")
    sys.exit()
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
        sys.exit()

root =tk.Tk()
root.title("Open Source Search Engine")
root.config(bg = "light blue")

description = tk.Label(root, bg = "light blue", text = "Your search matched these documents:")
description.pack()

text = tk.Text(root)
text.config(bg = "light blue")
for i in result:
    text.insert(tk.END, files[i] + '\n')
text.pack()

button = tk.Button(root, text = 'Exit', fg = 'White', bg = '#49A', height = 1, width = 10, command = root.destroy).pack()
    
root.mainloop()


