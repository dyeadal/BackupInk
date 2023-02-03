import sys
import os # lists directories, and its files. Also can see modification dates
import platform #Detects OS platform to run correct copy and hash commands.

# Main function
if __name__ == "__main__":

# Computer Information | Default and Environmental Variables
    opsysPlatform = platform.system()
    toFile = "Not yet chosen"
    fromFile = "Not yet chosen"



# Main Menu Function
    def mainMenu():
        print("\nDyeadal's Incremental Backup\n-------------------------------")
        print("Computer Information: " + opsysPlatform + "\n")
        print("Source Directory: " + fromFile + "\t\t\tArchive Directory: " + toFile)
        print("\n\tC\t-\tChose Directories to compare or create backup")
        print("\tD\t-\tDisplay Differences")
        print("\tI\t-\tPerform an Incremental Backup")
        print("\n\tQ\t-\tQuit")
        option = input("\n\nType Letter and press [Enter]: ")

        if option.isalpha():
            if option == "C" or "c": choseDirs()
            if option == "D" or "d": print("Displaying Differences")
            if option == "I" or "i": print("Performing Incremental Backup")
            if option == "Q" or "q": print("Quitting")
            else:
                print("Not a registered option, returning to screen")
                mainMenu()
        else:
            print("Not a valid input, returning to screen")
            mainMenu()

####################### Chose Directories ############################
# Functions to begin the directory allotment
# Splitting into multiple functions allows us to repeat a selection process for each individal directory path if it is not a valid input
    def choseDirs():
        print("\n\nDirectories for Comparing or Incrementally Backing Up\n")
        choseSource()
        choseArchive()
        print("\n Current/Production Storage Directory: " + fromFile + "\n Directory to Archive to or Compare: " + toFile)
        mainMenu()
    # Function to chose archive directory
    def choseArchive():
        source = input("Directory to copy from, or compare (usually storage device that needs files backed up): ")
        if validDir(source):
            print("Valid: " + source)
            global fromFile
            fromFile = source
        else:
            print("Invalid Directory/File\n")
            choseArchive()
    # Function to chose source directory
    def choseSource():
        archive = input("Directory to back up to, or compare to (an archive of existing files): ")
        if validDir(archive):
            print("Valid: " + archive)
            global toFile
            toFile = archive
        else:
            print("Invalid Directory/File\n")
            choseSource()
    # Function to validate file path exists
    def validDir(directorypath):
        if os.path.exists(directorypath):
            return True;
        else: return False;

####################### Integrity Check ############################
# Function to show the differences between the two chosen directories
    def displayDifferences():
        mainMenu()


###################### Termination Options ###############################
    # Function to return to menu or quit
    def returnToMenu():
        option = input("\n\n\nReturn to Menu [Enter] or [Q]uit")
        if option == "Q" or "q": terminate()
        else: mainMenu()

    #Function to quit program
    def terminate():
        print("\nGood bye :)")




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
