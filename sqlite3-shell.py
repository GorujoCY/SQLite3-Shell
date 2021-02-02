import sqlite3
import time
import os
import traceback
from sys import platform

clear_comm = "cls"
if platform in ["linux", "linux2"]:
    clear_comm = "clear"
elif platform == "darwin":
    clear_comm = "printf '\\33c\\e[3J'"

print("Booting Sqlite3 shell...")
print("------------------------")
print("The required version of Python is Python 3+")
time.sleep(2)
os.system(clear_comm)
print("Welcome, please input your first database you wanna load or start creating it")
print("-----------------------------------------------------------------------------")
filename = input("filename of db> ")
while filename == "":
    print("Please enter a database name.")
    filename = input("filename of db> ")

print("Please Wait...")
print("--------------")
try:
    db = sqlite3.connect(f"{filename}.db")
    c = db.cursor()
except:
    print("something went wrong, or failed to load database!")
    print("Restart shell!")
    input()
    exit()
finally:
    print("Database loaded!")
    print("----------------")
    time.sleep(2)
    os.system(clear_comm)
    print("SQLite3 Shell v1.1 by GeorgeCY (Made in Python)")
    print("------------------------------")

while True:
    try:
        commands = input("sqlite> ")
        while commands == "":
            print("Please enter an sqlite3 command.")
            commands = input("sqlite> ")

        if commands == "close":
            c.close()
            db.close()
            print("Closing...")
            break
        
        if commands == "exit":
            print("Exitting...")
            break
        
        if commands == "whats-new":
            print("What's New in V1.1:")
            print("1. Minor improvements and better handling")
            print("2. Now you can use the 'SELECT' statement in any cases (like lowercase, capital etc.)[Recommended to use it in uppercase]")
            continue
        
        if commands == "help":
            print("Help:")
            print("Shell Commands:")
            print("exit: Exits the program (not way recommended because it doesnt close the database!)")
            print("close: Closes the database, then exits the shell!")
            print("whats-new: Prints whats new in every update")
            print("-------------------------------------------------")
            print("Database Commands:")
            print("commit: commit/saves the database (occurs error when none of the changes was made)")
            print("[Note: when the number 0 Prints, it means sucess!]")
            continue




        output =  c.execute(f"{commands}")
        if not output:
            print("No output.")
        else:
            for line in output:
                print(line)

        print(0)
        
        if commands.upper().startswith("SELECT"):
            for rows in c.fetchall():
                print(rows)
        
        if commands == "commit":
            db.commit()
            print("database commited!")
        
    except:
        print("Error Occured:")
        traceback.print_exc()
