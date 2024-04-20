# open the number.txt file and read the numbers separately from the file
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        line = line.strip()
        print(line)
# separate odd and even numbers
# write even numbers to even.txt
# write odd numbers to odd.txt
# END OF PROGRAM