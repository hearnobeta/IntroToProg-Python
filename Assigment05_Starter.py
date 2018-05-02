#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   JHall
# Date:  APRIL 29, 2018
# JHall, 11/02/2016, Created starting template
#   <JESSICA HALL>, ???, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

To_Do_File = "Todo.txt"
tasks = []

# When the program starts, load each "row" of data

# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"

# Step 1 - Load data from a file
open_file = open(To_Do_File, 'r')
task_data = open_file.readlines()  # type:
open_file.close()

for task in task_data:
    task_info = task.split(",")
    task_dict = ({"task": task_info[0], "priority": task_info[1].strip('\n')})
    tasks.append(task_dict)




# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print() #adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        for task in tasks:
            print(task['task'] + ': ' + task['priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = input("What is the task name?:")
        strPriority = input("What is the priority Level?")
        tasks.append({"task": strTask, "priority": strPriority})
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        remove_option = input("Which task name would you like to remove?")
        for task in tasks:
            if task["task"].lower() == remove_option.lower():
                tasks.remove(task)
                print("Okay I removed it!\n")
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        open_file = open(To_Do_File, 'w')
        for task in tasks:
            open_file.write(task["task"] + "," + task["priority"] + '\n')
        open_file.close()
        print("Your selection has been saved")

        continue
    elif (strChoice == '5'):
        print("Goodbye")
        break #and Exit the program
    else:
        print("Please select a different option")

