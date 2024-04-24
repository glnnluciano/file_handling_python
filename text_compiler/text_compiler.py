# if want to enter data in mylife.txt file(y = yes, n = no), 
user_input = input("Do you want to enter data in mylife.txt file? (y/n): ")

# if yes, open/create mylife.txt file, use append mode
if user_input.lower() == "y":
        with open("mylife.txt", "a") as my_life:
            my_life.write(input("Enter line: ") + "\n")
# if no,
    # input if want to read, overwrite, close mylife.txt file (r = read, s = startover, c = close)
        # if r, open mylife.txt file, read
        # if s, open mylife.txt file, overwrite
        # if c, break