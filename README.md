# Open Source Search Engine

This project matches and returns the files that match a query given by the user. 

## Prerequisites
This project was developed using Python3 and TkInter for Python3 on Ubuntu 19.01. 
You will need to have both installed in order to run the app. See deployment for a 
script that should install everything needed.

### Installing
You will need to have your system up to date in order to install Python3 and TkInter.
Open a terminal and type in:
```
sudo apt-get update -y
sudo apt-get upgrade -y
```
Now that your system is updated, we can install Python by using:
```
sudo apt-get install python3.6 -y
```
Finally, install TkInter for the GUI this program provides:
```
sudo apt-get install python3-tk -y
```

## Running the tests
To start the program, make sure you are in the same directory as the project.py file is. To start, type
```
python3 project.py
```
in the command line and you should see a pop-up that lets you write a query.
Queries should have the following format:
```
word1 && (word2 || word3) && !(word4)
```
Which translates to : find documents containing word1 and either word2 or word 3, but exclude documents containing word 4. If the operation is successful, you will be provided yet another pop up containing the names of the documents. In case of failure, the program will throw an exception and an error message you visible in the command line.

## Deployment
To run the script, make sure you give it ALL PRIVILEDGES. You can use the command below:
```
chmod 777 installation.sh
```
Then run the script:
```
sudo ./installation.sh
```

## Authors

* **Andra Vasilache**

