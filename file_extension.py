def file_extension(filename):
    if '.' in filename:
        return filename.split('.')[-1]
    else:
        raise Exception("File extension is missing!!")

filename = input("Enter the file name : ")

try:
    file_extension = file_extension(filename)
    print("The file extension is : ",file_extension)
except Exception as e:
    print(e)
