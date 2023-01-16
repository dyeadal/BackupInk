import sys
import os

# Main function
if __name__ == "__main__":
    
# If no arguments were provided, running the script as is
    if len(sys.argv) == 1: 
        print ("\nDyeadal's Incremental Backup\n-------------------------------\n")
        print("No arguments supplied\nUse --help to print options available\n\n")

    
# If arguments were provided
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



        # Store -b value as a variable to easily call on backupDir
        if "-b" in argList: 
            backupDir = argList[argList.index("-b")+1]
            print("Directory to store backup: ", backupDir)
        
        # Store -i value as a variable to easily call on input Dir
        if "-i" in argList: 
            inputDir = argList[argList.index("-i")+1]
            print("Directory to backup: ", inputDir)

        # If one argument is used and not the other to notify and quit
        if "-i" and not "-b" in argList:
            print("\nError: No value for -b supplied.\nUsing -i requires the usage of -b as well. For further help use '--help'")

        elif "-i" and not "-b" in argList:
            print("\nError: No value for -i supplied.\nUsing -b requires the usage of -i as well. For further help use '--help'")
        else:
            if "-b" and "-i" in argList:
        #Confirm both inputs for directories are actual paths
                if os.path.exists(backupDir and inputDir):
                    print("Paths are valid")

                    backupArr = []
                    inputArr = []
                    removedArr = []
                    backupHash = []
                    inputHash = []

                #TO DO Loop function to store paths of files and their MD5 hashsums
                    #inputDir list files
                    inputArr.append(os.listdir(inputDir))

                #TO DO while loop to recursively list and store directory values
                    #check if any are directories in array
                    #if directories exist list those new directories
                    #loop till no directories left undocumented
                                        
                    #print output of array to see append worked
                    print(inputArr)

                #TO DO Research either os or subprocess is better for running MD5 hashsum command in Pythong
                #EITHER:
                    #os.popen(Get-FileHash <filepath> -Algorithm MD5).read()
                #OR:
                    #output = subprocess.check_output("Get-FileHash <filepath> -Algorithm MD5", shell=True)


                #TO DO List disrepencies OR State if no difference in arrays (list array differences)
                    #Loop to check missing files from back up (indicating new file), or changed MD5 sum (indicating changed file)

                    #Loop to check files that were removed from input that are backed up (removed files from production yet existed before in backups)

                #TO DO: Save changes to an XML file prior to initating backup, as a forensic log


                    print("\nIncremental Copy From:", inputDir, "\t\tTo:", backupDir,"?")
        #Confirm prompt to ensure the user is aware of the changes
                    confirmPrompt = input("(Y/N): ")
                    if confirmPrompt == str("y" or "Y"):
                        print("Copying")    
                    

                # TO DO Copy file functions of missing or modified files
                    #

                # TO DO Remove files that were removed in input directory from back up archive if they were removed
                    #

                    elif confirmPrompt == str("n" or "N"):
                        print("\nCanceling backup")
                    else:
                        print("\nError: Invalid input, use --help for assitance")

            # if path validation fails print error
                else: print ("\nError: Paths used can not be found")
