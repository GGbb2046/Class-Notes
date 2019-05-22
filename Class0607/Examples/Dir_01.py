import os
print(">>>> Files in this directory:")
for filename in os.listdir("./"):
    print(filename)

print(">>>> Files in the directory above:")
for filename in os.listdir("../"):
    print(filename)

print(">>>> Files in the users directory:")
for filename in os.listdir("C:/Users"):
    if filename not in ["All Users", "Default", "Default User", "desktop.ini", "Public"]:
        print("It looks like we have a user named " + filename)
        user_name = filename


# print all content found under a given path
# path = "C:/Users/" + user_name
# for (dirpath, dirnames, filenames) in os.walk(path):
#     print(dirnames)

# print all python files found under a given path
# path = "C:/Users/" + user_name
# path = "C:/Users/Tim/Dropbox/__UT/ITM695/PyCharm695M18"
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
    # note: this approach would likely set off a ton of OS warnings about trying to write to files. You'd need to be
    # smarter to ensure you were trying to write to files you have write access to.