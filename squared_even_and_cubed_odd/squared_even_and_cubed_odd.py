# open and read integer.txt
with open("integers.txt", "r") as integer_file:
    for line in integer_file: 

# convert line into integer
        line = int(line.strip())
        
# if number is even, square it and append in double.txt
    # open and append line to double.txt
# if number is odd, cube it and append in triple.txt
    # open and append line to triple.txt 
# END OF PROGRAM