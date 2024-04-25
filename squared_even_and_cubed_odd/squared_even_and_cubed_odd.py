# open and read integer.txt
with open("integers.txt", "r") as integer_file:
    for line in integer_file: 

# convert line into integer
        line = int(line.strip())

# if number is even, square it and append in double.txt
        if int(line) % 2 == 0:

            # square the even integer
            line = line**2

    # open and append line to double.txt
            with open("double.txt", "a") as even_file:
                even_file.write(str(line) + "\n")

# if number is odd, cube it and append in triple.txt
    # open and append line to triple.txt 
# END OF PROGRAM