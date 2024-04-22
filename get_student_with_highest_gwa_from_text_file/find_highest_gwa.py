# open the text file and read per line
with open("class_record.txt", "r") as class_record:

# initialize the variable 
    highest_gwa = 0

    for line in class_record:

# separate the name and gwa
        student_name, gwa = line.strip().split(",")
        gwa = float(gwa)

# find the highest gwa
    if gwa > highest_gwa:
        highest_gwa = gwa
        highest_gwa_student = student_name
        
# print the name and gwa of the student with the highest gwa