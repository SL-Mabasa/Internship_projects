def counter(name):
    filename = str(name+'.txt')
    print(filename)
    normalcount=0
    wordcount=0
    try:
        file = open(filename)
        lines = file.readlines()
        #print(lines)
        linecount = len(lines)
        while normalcount<linecount:
            spliter=lines[normalcount].split()
            wordcount+=len(spliter)
            normalcount+=1
        file.close()
        return print(f"\nWord count is {wordcount}.")
    except FileNotFoundError as error:
        print("File Not Found")
    

print("Program counts words in a file\n")
document = str(input("Enter file name\n-> "))
counter(document)