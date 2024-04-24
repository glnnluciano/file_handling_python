# if want to enter data in mylife.txt file(y = yes, n = no), 
user_input = input("Do you want to enter data in mylife.txt file? (y/n): ")

# if yes, open/create mylife.txt file, use append mode
if user_input.lower() == "y":
    with open("mylife.txt", "a") as my_life:
        my_life.write(input("Enter line: ") + "\n")

# if no,
elif user_input.lower() == "n":

    # input if want to read, overwrite, close mylife.txt file (r = read, s = startover, c = close)
    read_start_over_close = input("Do you want to read (r), startover (s), or close (c) mylife.txt file?:")

    # if r, open mylife.txt file, read
    if read_start_over_close.lower() == "r":
        with open("mylife.txt", "r") as my_life:
            for line in my_life:
                print(line.strip())
        
        # if s, open mylife.txt file, overwrite
        # if c, break