import sqlite3
import time
import os
import traceback

print("Booting Sqlite3 shell...")
print("------------------------")
print("The Version of Python must be available is Python 3+ and Windows Machine")
print("News about the shell:")
print("---------------------")
print("Linux availability is coming!")
time.sleep(4)
os.system("cls")
print("Welcome, please input your first database you wanna load or start creating it")
print("-----------------------------------------------------------------------------")
filename = input("filename of db> ")
print("Please Wait...")
print("--------------")
try:
    db = sqlite3.connect(f"{filename}.db")
    c = db.cursor()
except:
    print("something went wrong, or failed to load database!")
    print("Restart shell!")
    input("")
    exit()
finally:
    print("Database loaded!")
    print("----------------")
    time.sleep(2)
    os.system("cls")
    print("SQLite3 Shell v1.0 by GeorgeCY (Made in Python) [BETA]")
    print("------------------------------")

while True:
    try:
        commands = input(">")
        if commands == "close":
            c.close()
            db.close()
            print("Closing...")
            break
        
        if commands == "exit":
            print("Exitting...")
            break
        
        if commands == "help":
            print("Help:")
            print("Shell Commands:")
            print("exit: Exits the program (not way recommended because it doesnt close the database!)")
            print("close: Closes the database, then exits the shell!")
            print("-------------------------------------------------")
            print("Database Commands:")
            print("commit: commit/saves the database (occurs error when none of the changes was made)")
            print("[Note: when the number 0 Prints, it means sucess!]")
            print("[Another Note is that the program is currently in BETA!]")
            print("(ignore error on bottom:)")
            print("-----------------------")
            pass

        c.execute(f"{commands}")
        print(0)
        
        if commands.startswith("SELECT"):
            for rows in c.fetchall():
                print(rows)
        
        if commands == "commit":
            db.commit()
            print("database commited!")
        
       
    except:
        print("Error Occured:")
        traceback.print_exc()