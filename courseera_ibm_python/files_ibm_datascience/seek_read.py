# with open("sample_data.txt",'r') as file:
#     FileContent = file.read()
#     print("FileContent at first using read():",FileContent)
#     print("raw contents:",repr(FileContent))
#     print("first 6 characters:",file.read(6))
#     print("present file cursor index is", file.tell())
#     file.seek(0)
#     print("present file cursor index is", file.tell())
#     print("thats because read function made to go index at last character, so we reset it to 0 again, now first 6 characters:", file.read(6))
#     print("present file cursor index is", file.tell())
#     print("next 3 characters:", file.read(3))
#     print("present file cursor index is", file.tell())
#     file.seek(24)
#     print("present file cursor index is", file.tell())
#     print("From position 24 next 6 characters:",file.read(6))
#     print("file name:",file.name)
#     print("file mode:", file.mode)
#     print("present file cursor index is",file.tell())
#     FileContent = file.read()
#     print(FileContent)
#     print("present file cursor index is", file.tell())
#
# print("you can even access filecontent stored in variable outside with block also:",FileContent)
# print("does file closed by using with operator:",file.closed)

# # Create a new file Example2.txt for writing
# with open('Example2.txt', 'w') as file1:
#     file1.write("This is line A\n")
#     file1.write("This is line B\n")
#     # file1 is automatically closed when the 'with' block exits
#
# # List of lines to write to the file
# Lines = ["This is line 1", "This is line 2", "This is line 3"]
# # Create a new file Example3.txt for writing
# with open('Example3.txt', 'w') as file2:
#     for line in Lines:
#         file2.write(line + "\n")
#     # file2 is automatically closed when the 'with' block exits

# # Data to append to the existing file
# new_data = "This is line C"
# # Open an existing file Example2.txt for appending
# with open('Example2.txt', 'a') as file1:
#     file1.write(new_data + "\n")
#     # file1 is automatically closed when the 'with' block exits

# Open the source file for reading
with open('Example3.txt', 'r') as source_file:
    # Open the destination file for writing
    with open('destination.txt', 'w') as destination_file:
        # Read lines from the source file and copy them to the destination file
        for line in source_file:
            destination_file.write(line)
    # Destination file is automatically closed when the 'with' block exits
# Source file is automatically closed when the 'with' block exits