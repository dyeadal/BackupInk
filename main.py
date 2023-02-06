import sys
import os # lists directories, and its files. Also can see modification dates
import platform #Detects OS platform to run correct copy and hash commands.

# Main function
if __name__ == "__main__":

# Computer Information | Default and Environmental Variables
    opsysPlatform = platform.system()
    archiveDir = ""
    sourceDir = ""



# Main Menu Function
    def mainMenu():
        splash()
        print("Computer Information: " + opsysPlatform)
        print("Source Directory: " + sourceDir +"\nArchive Directory: " + archiveDir)
        print("\n\tC\t-\tChose Directories to compare or create backup")
        print("\tD\t-\tDisplay Differences")
        print("\tI\t-\tPerform an Incremental Backup")
        print("\n\tQ\t-\tQuit")
        option = input("\n\nType Letter and press [Enter]: ")

        if option.upper() == "C" : choseDirs()
        elif option.upper() == "D" : displayDifferences()
        elif option.upper() == "I" : print("Performing Incremental Backup")
        elif option.upper() == "Q" : print("Quitting")
        else: mainMenu()

####################### Chose Directories ############################
# Functions to begin the directory allotment
# Splitting into multiple functions allows us to repeat a selection process for each individal directory path if it is not a valid input
    def choseDirs():
        splash()
        print("\n\nDirectories for Comparing or Incrementally Backing Up\n")
        global archiveDir, sourceDir
        if sourceDir!= "":
            print("Chose a different directory than ", sourceDir,"?")
            option = input("(y/n): ")
            if option.upper() == "Y":
                choseSource()
        else: choseSource()

        if archiveDir != "":
            print("Chose a different directory than Path:", archiveDir, " ?")
            option = input("(y/n): ")
            if option.upper() == "Y":
                choseArchive()
        else: choseArchive()
        mainMenu()
    # Function to chose archive directory
    def choseArchive():
        source = input("Full path of where to store backup: ")
        if validDir(source):
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
                choseArchive()
            elif option.upper() == "N":
                mainMenu()
            else:
                print("Invalid, Quitting")
                terminate()
    # Function to chose source directory
    def choseSource():
        archive = input("Full path of data needing back up: ")
        if validDir(archive):
            print("Valid: " + archive)
            global sourceDir
            sourceDir = archive
        else:
            print("Invalid Directory/File, check if storage is properly connected/mounted")
            option = input("Try Again? (y/n): ")
            if option.upper() == "Y":
                choseSource()
            elif option.upper() == "N":
                mainMenu()
            else:
                terminate("Invalid option, exiting program")

    def areDirEmpty():
        if sourceDir == "" or archiveDir == "":
            print("You must first choose your directories")
            input("Press any key to return to menu")
            mainMenu()

    # Function to validate file path exists
    def validDir(directorypath):
        if os.path.exists(directorypath):
            return True;
        else: return False;

####################### Integrity Check ############################
# Function to show the differences between the two chosen directories
    def displayDifferences():
        splash()
        areDirEmpty()


    def hashCalculator():
        print("")

    def dirArray(directory):
        listdir = os.listdir(directory)
        print(directory+listdir[0])


###################### Termination Options ###############################
    # Function to return to menu or quit
    def returnToMenu():
        option = input("\n\n\nReturn to Menu [Enter] or [Q]uit")
        if option.upper() == "Q": terminate()
        else: mainMenu()

###################### General Functions ########################
    # Logo ASCII art
    def splash():
        clearScreen()
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
    def clearScreen():
        if opsysPlatform == "Windows":
            os.system('cls')
            print("")
        elif opsysPlatform == "Linux":
            os.system('clear')
        print("")

    #Function to quit program
    def terminate():
        quit()
    def terminate(msg):
        print(msg)
        quit()




#TO DO Loop function to store paths of files and their MD5 hashsums
    #inputDir list files


                #TO DO while loop to recursively list and store directory values
                    #check if any are directories in array
                    #if directories exist list those new directories
                    #loop till no directories left undocumented
                                        
                    #print output of array to see append worked

                #TO DO Research either os or subprocess is better for running MD5 hashsum command in Python
                #EITHER:
                    #os.popen(Get-FileHash <filepath> -Algorithm MD5).read()
                #OR:
                    #output = subprocess.check_output("Get-FileHash <filepath> -Algorithm MD5", shell=True)


                #TO DO List disrepencies OR State if no difference in arrays (list array differences)
                    #Loop to check missing files from back up (indicating new file), or changed MD5 sum (indicating changed file)

                    #Loop to check files that were removed from input that are backed up (removed files from production yet existed before in backups)

                #TO DO: Save changes to an XML file prior to initating backup, as a forensic log


                # TO DO Copy file functions of missing or modified files
                    #

                # TO DO Remove files that were removed in input directory from back up archive if they were removed

    #Starts program
    mainMenu()
