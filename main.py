import os       # to list details of directories, and its files.
import platform     # to detects OS platform to run correct copy and hash commands.
import openpyxl     # to create and edit spreadsheets

# Main function
if __name__ == "__main__":

    # Computer Information | Default and Environmental Variables
    opsysPlatform = platform.system()
    archiveDir = ""
    sourceDir = ""

    # Main Menu Function
    def main_menu():
        splash()
        print("Computer Information: " + opsysPlatform)
        print("Source Directory: " + sourceDir + "\nArchive Directory: " + archiveDir)
        print("\n\tC\t-\tChose Directories to compare or create backup")
        print("\tD\t-\tDisplay Differences")
        print("\tI\t-\tPerform an Incremental Backup")
        print("\n\tQ\t-\tQuit")
        option = input("\n\nType Letter and press [Enter]: ")

        if option.upper() == "C":
            chose_directories()
        elif option.upper() == "D":
            directory_differences()
        elif option.upper() == "I" :
            print("Performing Incremental Backup")
        elif option.upper() == "Q":
            print("Quitting")
        else:
            return_to_menu()

"""
Chose Directories Functions
"""

    # Function to begin choosing directories to compare and create backups
    def chose_directories():
        splash()
        print("\n\nDirectories for Comparing or Incrementally Backing Up\n")
        global archiveDir, sourceDir
        if sourceDir!= "":
            print("Chose a different directory than ", sourceDir,"?")
            option = input("(y/n): ")
            if option.upper() == "Y":
                chose_source()
        else: chose_source()

        if archiveDir != "":
            print("Chose a different directory than Path:", archiveDir, " ?")
            option = input("(y/n): ")
            if option.upper() == "Y":
                chose_archive()
        else:
            chose_archive()

        return_to_menu()
    # Function to chose archive directory
    def chose_archive():
        source = input("Full path of where to store backup: ")
        if is_valid_directory(source):
            print("Valid: " + source)
            global archiveDir
            if source.endswith("/") or source.endswith("\\"):
                archiveDir = source
            elif opsysPlatform == "Windows":
                archiveDir = source+"\\"
            else: archiveDir = source+"/"

        else:
            print("Invalid Directory/File, check if storage is properly connected/mounted")
            option = input("Try Again? (y/n): ")
            if option.upper() == "Y":
                chose_archive()
            elif option.upper() == "N":
                return_to_menu()
            else:
                print("Invalid, Quitting")
                terminate(None)
    # Function to chose source directory
    def chose_source():
        archive = input("Full path of data needing back up: ")
        if is_valid_directory(archive):
            print("Valid: " + archive)
            global sourceDir
            sourceDir = archive
        else:
            print("Invalid Directory/File, check if storage is properly connected/mounted")
            option = input("Try Again? (y/n): ")
            if option.upper() == "Y":
                chose_source()
            elif option.upper() == "N":
                return_to_menu()
            else:
                terminate("Invalid option, exiting program")

    def are_directories_chosen():
        if sourceDir == "" or archiveDir == "":
            print("You must first choose your directories")
            input("Press any key to return to menu")
            return_to_menu()

    # Function to validate directory path actually exists
    def is_valid_directory(directorypath):
        return os.path.isdir(directorypath)
        # Why does this line have an error?

"""
Integrity Check Functions
"""
    # Function to show the differences between the two chosen directories
    def directory_differences():
        splash()
        are_directories_chosen()
        map_directory(sourceDir)

    def map_directory(directory):
        maindir = os.listdir(directory)
        x = 0
        while len(maindir) > x:
            path = directory+maindir[x]

            # If item in directory is another directory
            if is_valid_directory(path):
                if is_windows():
                    path += "\\"
                    print(path)     # Debug: this shows what is added to the array/spreadsheet
                    map_directory(path)
                if is_unix():
                    path += "/"
                    print(path)     # Debug: this shows what is added to the array/spreadsheet
                    map_directory(path)


            # If item is a file and not an embedded directory
            else:
                print(path)     # Debug: this shows what is added to the array/spreadsheet
            x += 1

    def hash_calculator():
        print("")

    def directory_array(directory):
        listdir = os.listdir(directory)
        print(directory+listdir[0])

###################### Excel Functions ##################################
    # Test openpyxl module to see how to create and manipulate spreadsheets
    def create_spread_sheet_file(filename):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet ['A1'] = "Hi"
        workbook.save(filename+"xml")

###################### Termination Options ###############################
    # Function to return to menu or quit
    def return_to_menu():
        option = input("\n\n\nReturn to Menu [Enter] or [Q]uit")
        if option.upper() == "Q": terminate(None)
        else: return_to_menu()

###################### General Functions ########################
    # Logo ASCII art
    def splash():
        clear_screen()
        print(".................")
        print("| |           | |")
        print("| | BackupInk | |")
        print("| |           | |")
        print("| |___________| |")
        print("|   _________   |")
        print("|   |     | |   |")
        print("|___|_____|_|___|")
        print("Made by dyeadal\n\n")

    # Clear console screen
    def clear_screen():
        if is_windows():
            os.system('cls')
            print("")
        elif is_unix() == "Linux":
            os.system('clear')
        print("")

    # Functions to determine OS platform and dictates what commands are ran for their respective platform
    def is_windows():
        global opsysPlatform
        if opsysPlatform == "Windows":
            return True
        else:
            return False

    def is_unix():
        global opsysPlatform
        if opsysPlatform == "Linux":
            return True
        else: return False

    # Function to quit program
    def terminate(msg):
        quit()

    # Starts program
    main_menu()
