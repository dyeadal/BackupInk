import sys

# Main function
if __name__ == "__main__":
    
# NO ARGUMENTS PROVIDED / RAN SCRIPT WITH NO ARGUMENTS
    if len(sys.argv) == 1: 
        print ("\nDyeadal's Incremental Backup\n-------------------------------\n")
        print("No arguments supplied\nUse --help to print options available\n\n")

    
# IF ARGUMENTS EXIST: 
    else:
    #creates a deep copy array of the arguments  
        argList = sys.argv.copy()
        argList.pop(0) #removes the first (0) argument or item in the list which is the command to run the script itself or location of the script

    #if "--help" is used
        if "--help" in argList:
            print ("\nDyeadal's Incremental Backup\n-------------------------------\n")
            print("\nCommon Usages:\nBack up files missing from a source directory to an existing directory: -i [input_directory] -b [backup_directory]")

            print("\n Arguments to use:")
            print("-b\tBackup directory location of where your archive is stored.")
            print("-i\tDirectory to back up to. This is used with the [-b] command.")
            print()

    # Back up Directory 
        if "-b" in argList: 
            backupDir = argList[argList.index("-b")+1]
            print("Directory to store backup: ", backupDir)

        if "-i" in argList: 
            inputDir = argList[argList.index("-i")+1]
            print("Directory to backup: ", inputDir)

        if "-b" and "-i" in argList:

#TO DO Confirm both inputs are directories (input validation)
        
#TO DO Create an array for each directory of hashes of each file, recursively (store values)
        
#TO DO List disrepencies OR State if no difference in arrays (list array differences)

            print("\nIncremental Copy From:", inputDir, "\t\tTo:", backupDir,"?")
        #Confirm prompt to ensure the user is aware of the changes
            confirmPrompt = input("(Y/N): ")
            if confirmPrompt == str("y" or "Y"):
                print("Copying")
# TO DO Copy file function

            elif confirmPrompt == str("n" or "N"):
                print("Canceling backup")
            else:
                print("Invalid input, use --help for assitance")


    
