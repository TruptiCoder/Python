import os
import shutil

path = "Advance\\Module\\copy.txt"

try:
    os.remove(path)
    # os.rmdir(path) # to remove empty folder
    # shutil.rmtree(path) # to remove folder with files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You can not delete that using that method")
else:
    print(path + " was deleted")