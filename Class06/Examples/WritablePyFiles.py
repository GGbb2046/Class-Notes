import os

path = "C:\\"
all_writable_py_files = []
count = 0
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename.endswith(".py"):
            file_path = os.path.join(dirpath,filename)
            if os.access(file_path, os.W_OK):
                count += 1
                all_writable_py_files.append(file_path)
                print(str(count) + "  " + file_path + " is writable")


ans = input("Do you want me to try to add a payload to the start of these files? [Y/N]: ")
if ans == "Y" or ans=="y":
    print("Sorry, I'm not a virus. "
          "If I were a virus, I might try to write a piece of malicious code into the header of the .py files I found.")