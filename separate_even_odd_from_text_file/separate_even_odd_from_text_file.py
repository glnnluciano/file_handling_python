# open the number.txt file and read the numbers separately from the file
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        line = line.strip()

# separate odd and even numbers
        if int(line) % 2 == 0:

# write even numbers to even.txt
            with open("even.txt", "a") as even_file:
                even_file.write(line + "\n")

# write odd numbers to odd.txt
        else:
            with open("odd.txt", "a") as odd_file:
                odd_file.write(line + "\n")
                
# END OF PROGRAM