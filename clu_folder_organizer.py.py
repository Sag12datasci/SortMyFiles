import os
import shutil
import time 
import tkinter as tk 
from tkinter import filedialog
import traceback

# """      This program will organize the cluttered folder by moving the files to their respective folders based on their extensions.
#             just run the program and enter the path of the folder you want to organize and the program will do the rest for you"""


print("Go to the folder right click , Copy as Path and paste it here or select the folder press Ctrl+Shift and c and paste it here")


# #This function will return the category paths for the files based on their extensions.
def get_category_paths():
    return {
        'Documents': [
            '.doc', '.docx', '.txt', '.pdf', '.rtf', '.odt', '.tex', '.md', '.log', '.wps',
            '.wpd', '.asc', '.ans', '.json', '.yaml', '.yml', '.ini', '.cfg',
            '.conf', '.nfo'
        ],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.ogg'], 
        'Archived': ['.zip', '.rar', '.gz', '.bz2'],
        'C': ['.c', '.h'],
        'Python': ['.py', '.pyc'],
        'Java': ['.java', '.class'],
        'JavaScript': ['.js'],
        'HTML': ['.html', '.htm'],
        'CSS': ['.css'],
        'Avogadro': ['.cjson', '.xyz', '.pdb', '.mol'],
        'Chimera': ['.mae', '.mol2', '.sdf'],
        'AutoDockTools': ['.dlg', '.pdbqt'],
        'Discovery Studio': ['.cif', '.sdf'],
        'Executables': ['.exe', '.bin'],
        'Excel': ['.xls', '.xlsx', '.xlsm', '.xlsb', '.xlt', '.xltx', 
                '.xltm', '.ods', '.csv', '.tsv'],
        'Other': []
    }
    

"Ensure that a folder exists for each category under the root folder"
def ensure_directories_exist(root_folder, getcategory_paths):
    for category in getcategory_paths.keys():
        category_path = os.path.join(root_folder, category)
        
        "Create the directory if it doesn't already exist"
        os.makedirs(category_path, exist_ok=True)


"Move a single file into its category folder based on its extension"
def move_file_to_category(file_path, root_folder, getcategory_paths):
    file_name = os.path.basename(file_path) # Extract just the file name
    base , ext = os.path.splitext(file_name) #Split into name and extension
    ext=ext.lower()
    print(f"DEBUG: {file_name!r} → ext={ext!r}") #Debug print to show extension




    # Check each category to see if the file's extension matches
    for category, extensions in getcategory_paths.items():

        if ext in extensions:
            dest_folder= os.path.join(root_folder,category)

            dest_path=os.path.join(dest_folder,file_name)

            # If a file with the same name already exists, append a counter
            counter = 1 
            while os.path.exists(dest_path):
                new_name= f"{base}_{counter}{ext}"
                dest_path=os.path.join(dest_folder,new_name)
                counter +=1

            # Move the file into the category folder
            shutil.move(file_path, dest_path)
            print(f"Moved '{file_name}' -> '{category}/{os.path.basename(dest_folder)}'")
           
            return True
    return False    # Return False if no matching category was found

print("____________________________________________________________________________")

"# Remove empty folders left after moving files"
def remove_empty_folders(root_folder): 


    # Walk the directory tree bottom-up (deepest directories first)
    for dirpath, _ , _ in os.walk(root_folder, topdown=False):
       
        
       try:
            if (os.path.isdir(dirpath) and not os.listdir(dirpath) #first is it a dict? , is it empty? , don't delete the root folder itself  
                and dirpath != root_folder):

                os.rmdir(dirpath)
                print(f"Removed empty folder: {os.path.relpath(dirpath, root_folder)}")

       except Exception as e:
            print(f"Failed to remove {dirpath}: {e}")


"""
# Main organizing routine that ties everything together

"""
def organize_folder(root_folder):
    category_map = get_category_paths()


# Pre-compute absolute paths of category folders (except 'Other')
    category_path ={ 
        os.path.abspath(os.path.join(root_folder, cat))
        for  cat in category_map 
        if cat != 'Other'
        }
    

    # Step 1: Create category directories
    ensure_directories_exist(root_folder, category_map)

    # Step 2: Walk through all files and subdirectories
    for dirpath, _, file_names in os.walk(root_folder,topdown=False):
        absolute_path=os.path.abspath(dirpath)


        # file_path = os.path.join(root_folder, file_names)

        # if any (absolute_path == os.path.abspath(os.path.join(root_folder, cat))
        #         for cat in category_map):



        # Skip moving files inside the category folders themselves
        if absolute_path in category_path:
            continue


        # Process each file in the current directory
        for fname in file_names:
            file_path=os.path.join(dirpath,fname)


            # Skip hidden or system files starting with a dot
            if fname.startswith('.'):
                continue

            # Try moving to a known category; if it fails, move to 'Other'
            if not move_file_to_category(file_path,root_folder,category_map):
                other_folder= os.path.join(root_folder,'Other')
                base ,ext = os.path.splitext(fname)
                dest=os.path.join(other_folder,fname)


                 # Handle name collisions in 'Other' folder
                counter=1
                while os.path.exists(dest):
                    dest= os.path.join(other_folder,f"{base}_{counter}{ext}")
                    counter +=1

                shutil.move(file_path,dest)
                print(f"Moved '{fname}' to 'Other/{os.path.basename(dest)}'")


            # After moving files, if the source folder is now empty (and not a category folder), delete it
            if (dirpath != root_folder and not os.listdir(dirpath) 
                and absolute_path not in category_path):

                # Check if the directory is empty
                os.rmdir(dirpath)
                relative_path=os.path.relpath(dirpath,root_folder)
                print(f"Removed empty folder: {relative_path}")



        # if os.path.isdir(file_path):#If the file is a directory, skip it
        #     continue


     # Step 3: Clean up any empty category folders
    for category in category_map:
        cat_path = os.path.join(root_folder,category)
        # if os.path.exists(cat_path) and not os.path.isdir(cat_path):
        if os.path.isdir(cat_path) and not os.listdir(cat_path):
            try:
                os.rmdir(cat_path)
                print(f"Deleted empty category folder: {category}")
            except OSError as e:
                traceback.print_exc()
    

    # Final cleanup of any remaining empty subfolders
    return remove_empty_folders(root_folder)




#for terminal

# def main():
    # while True:
    #     try:
    #         folder_path = input("Enter the path of the folder to organize (or type 'exit' to quit):").strip()
    #         folder_path=folder_path.replace('"', '').replace("'",'')
    #         if folder_path.lower() == 'exit':
    #             break

    #         if not os.path.isdir(folder_path):
    #            print("Invalid folder path. Please try again.")
    #            continue

    #         organize_folder(folder_path)

    #         for Wrong_input in range(4):
    #             another_input = input(f"{Wrong_input + 1} Do you want to organize another folder? (yes/no):").strip()
    #             if another_input.lower() not in ('yes', 'no'):
    #                 print("Invalid input. Please enter 'yes' or 'no'.")
    #             elif another_input.lower() == 'no':
    #                 print("Thank you for using the program. Exiting in 3 seconds")
    #                 time.sleep(3)
    #                 exit()
    #             else:
    #                 break
    #         exit("Too many invalid attempts\nThank you for using the program.Exiting the program")
    #     except KeyboardInterrupt:
    #         print("\nProcess interrupted by user. Exiting in 5 seconds")
    #         for i in range(5, 0, -1):#Countdown
    #             print(i)
    #             time.sleep(1)
    #         break
    #     except Exception as e:
    #         print(f"An error occurred: {e}. Please try again.")


def main():
    root = tk.Tk()
    root.withdraw()

    # 2. Show folder-selection dialog
    folder_path = filedialog.askdirectory(
        title="Select Folder to Organize",
        mustexist=True,
        initialdir=os.path.expanduser("~")
    )
    if not folder_path:
        print("No folder selected. Exiting.")
        return

    # 3. Run the organizer
    organize_folder(folder_path)

    print("Organization complete. Exiting in 3 seconds...")
    time.sleep(3)

if __name__ == '__main__':
    main()


