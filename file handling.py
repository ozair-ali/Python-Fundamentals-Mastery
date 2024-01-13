# opening the original file in read mode and the formatted file in write mode
file = open("C:\\Users\\Toshiba\\Desktop\\product descriptions.txt","r")
newfile = open("C:\\Users\\Toshiba\\Desktop\\formatted descriptions.txt","w")

# checking if the files are opened or not
if file and newfile:
    print("Files are opened successfully")
    # reading the text line by line from the source file
    lines = file.readlines()
    
    # using for loop to iterate through each line
    for line in lines:
        # using title() to capitalize each line
        capital_words = [line.title()]
        # writing the formatted lines into a new file
        newfile.writelines(capital_words)

    # closing both the files
    file.close()
    newfile.close()

else:
    print("Files are not found")