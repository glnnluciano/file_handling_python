# open the number.txt file and read the numbers separately from the file
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        line = line.strip()

# separate odd and even numbers
        if int(line) % 2 == 0:

# write even numbers to even.txt
# write odd numbers to odd.txt
# END OF PROGRAM