# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Patrick Woodard,8/1/2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task:Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data in ToDoList.txt
# into a python list of dictionary rows (like Lab 5-2)
ToDoList=open(objFile, 'r')
for row in ToDoList:
    lstRow = row.split(",")
    dicRow = {lstRow[0]:lstRow[1].strip()}
    lstTable.append(dicRow)
ToDoList.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save data to file
    5) Exit program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
# Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("TASK\t| PRIORITY")
        for row in lstTable:
            for key,value in row.items():
                print(key,"\t| ",value)
            continue
        continue
# Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask=input("Task Name: ")
        newPriority=input("Task Priority: ")
        dicRow={newTask:newPriority}
        lstTable.append(dicRow)
        continue
# Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        delTask = input("Enter task to delete: ")
        count = 0 # count used to identify list item to delete
        for item in lstTable:
            if delTask in item:
                print("*** Removed '",delTask,"' from list ***")
                del lstTable[count]
                break
            else: count += 1
        else: print("\n*** item not in list ***")
        continue
# Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        ToDoList = open(objFile, 'w')
        for row in lstTable:
            for myKey,myValue in row.items():
                item = (myKey+","+myValue+"\n")
                ToDoList.write(item)
        ToDoList.close()
        print('*** list saved to file: '+objFile+' ***')
        continue
# Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        dummy=input("*** press enter to exit program ***")
        break  # and Exit the program
