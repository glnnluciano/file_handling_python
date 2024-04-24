# open/create mylife.txt file
with open("mylife.txt", "w") as my_life:
        print(my_life.write("Hello World!"))
# if want to enter data in mylife.txt file(y = yes, n = no), 
# if yes, use append mode
# if no,
# if want to read data from mylife.txt file (r = read), use read mode, 
# if want to overwrite data in mylife.txt file, use write mode (s = startover)