# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Dan Ficek,3-9-2022,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

# Import Classes

if __name__ == "__main__":
    #import DataClasses1
    # as D  # data classes
    import ProcessingClasses as P  # processing classes
    from DataClasses import Employee as Emp  # Employee class only!
    #from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

#define variables
lstTableEmp=[]  #list of employee objects
strChoice = ""  #user menu choice

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTableEmp.clear()
for line in lstFileData:
    lstTableEmp.append(Emp(line[0], line[1], line[2].strip()))

# Show user a menu of options
while (True):
    Eio.print_menu_items()
    str_Choice = Eio.input_menu_options() # Get user's menu option choice

    if str_Choice == "1": # Show user current data in the list of employee objects
        Eio.print_current_list_items(lstTableEmp)

    elif str_Choice == "2":# Let user add data to the list of employee objects
        lstTableEmp.append(Eio.input_employee_data())

    elif str_Choice == "3":# let user save current data to file
        P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTableEmp)
        print("Data Saved to file!")

    elif str_Choice == "4": # Let user exit program
        break
# Main Body of Script  ---------------------------------------------------- #
