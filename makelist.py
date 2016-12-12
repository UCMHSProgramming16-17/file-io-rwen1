# Dec 12, 2016
# Take user input and write it to a file as a numbered list of 10 items

file_write = open("list.txt", 'w') # Initiate file writing
for number in range(10):
    file_write.write(str(number + 1) + ". " + input(str(number + 1) + ":  ") + "\n") # Ask for user input and write it to the file
file_write.close() # Close the file