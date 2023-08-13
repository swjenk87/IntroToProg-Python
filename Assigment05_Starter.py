# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SJenkins,2023-08-08,Added additional functionality to Assignment 05
# SJenkins,2023-08-12,Finalized script for turn-in
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = ""  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strFileHeader = "Task & Priority" # Setr a file header for the text file

# Additional variables added to enhance functionality.
lstRow = [] # A row of data from the file
strWarning = "Warning: Your To Do List Doesn't Exist!" # Create a warning message and check if it is being used
strTask = "" # Empty variable to store user input for a task
strPriority = "" # Empty variable to store user input for a task's priority




# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

# Attempt to find and load data from a text file that may or may not exist.
try:
    objFile = open("ToDoList.txt", "r")
    for row in objFile:
        lstRow = row.split(",") # Returns any current data in the file to a list row
        dicRow = {"Task":lstRow[0].strip(), "Priority":lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()

# After failing to locate a text file, create a file if one does not exist, and present warning to the user
except:
    print(strWarning)
    print("Creating One for You Now!\n")
    objFile = open("ToDoList.txt", "w")
    objFile.close()
    print("Your To Do List is Created and Ready to Modify!")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here

        # Checks to see if the table is empty or contains data to display.
        if lstTable == []:
            print("Your To Do List is Empty, Try Adding Some Tasks!")
            print("-" * 50)
        else:
            print("Currently Your Tasks Are: \n")
            for row in lstTable:
                print("Task:", row["Task"], "||", "Priority:", row["Priority"])
            print("-" * 50)

        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        # Confirming the user's choice to add a new task to the To Do List.
        print("You've Chosen to Add a New Task!")

        # Loops as long as the user opts to keep adding items, via a y/n choice below.
        while(True):
            # Modify the strTask variable with a user input, check if "exit" was entered.
            strTask = input("Type a New Task (or Exit for the Menu): ")
            if(strTask.lower() == "exit"): # Exit criteria
                break

            # Modify the strPriority variable with a user input, check if "exit" was entered.
            strPriority = input("Type the Task's Estimated Priority[High/Medium/Low] (or Exit for the Menu): ")
            if(strPriority.lower() == "exit"):
                break

            # If exit was not selected, display what was entered and append it to the table.
            else:
                print("You Entered:", strTask, "with a Priority of", strPriority)
                print("-" * 50)
                lstTable.append({"Task":strTask, "Priority":strPriority})
                print("You're Task has been Added! Remember to Save Before Exiting!\n")

                # Ask the user if they want to add more data before taking them back to the menu.
                strConData = str(input("Do you want to add more tasks? (y/n): "))
                if(strConData.lower() == "y"):
                    print("\n")
                    continue
                elif(strConData.lower() == "n"):
                    print("\n")
                    break
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        # Letting the user know they have chosen to remove items and to follow the prompts.
        print("Follow the instructions below to remove a To Do List item!")

        # Loops as long as the user wishes to remove items from the To Do List
        while(True):
            strRemoveTask = input("Which Task Would you Like to Remove?: ")
            intRowCount = 0
            blnRemove = False
            while(intRowCount < len(lstTable)):
                if(strRemoveTask == str(list(dict(lstTable[intRowCount]).values())[0])):
                    del lstTable[intRowCount]
                    blnRemove = True
                intRowCount += 1

            # Check the removed task boolean.
            if(blnRemove == True):
                # Check if the user wants to remove any additional items, before returning to the menu.
                print("Your task was removed!")
                strConRemoveData = str(input("Do you want to remove more tasks? (y/n): "))
                if(strConRemoveData.lower() == "y"):
                    print("\n")
                    continue
                elif(strConRemoveData.lower() == "n"):
                    print("\n")
                    break
            # If the task does not exist, print the following statement.
            else:
                print("That task does not exist!")

        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        # Check if user wants to see the data one more time before saving to file.
        strDispData = input("Do you wish to see your list before saving?: ")
        if(strDispData.lower() == "y"):
            print("Currently Your Tasks Are: \n")
            for row in lstTable:
                print("Task:", row["Task"], "||", "Priority:", row["Priority"])
            print("-" * 50)

        # Save Table to text file.
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write("Task: " + row["Task"] + "||" + "Priority: " + row["Priority"] + "\n")
        objFile.close()
        input("Your tasks have been saved to your To Do List! Hit [Enter] to go back to the main menu.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
