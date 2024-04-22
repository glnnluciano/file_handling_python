# open the text file
with open("class_record.txt", "r") as class_record:

# initialize the variable 
    highest_gwa = 0
    list_of_student_with_highest_gwa = ""

# read per line
    for line in class_record:

# separate the name and gwa
        student_name, gwa = line.strip().split(",")
        gwa = float(gwa)

# find the highest gwa
        if gwa > highest_gwa:
            highest_gwa = gwa
            list_of_student_with_highest_gwa = [student_name]
        elif gwa == highest_gwa:
            list_of_student_with_highest_gwa.append(student_name)

# print the name and gwa of the student with the highest gwa
print("Student/s with the highest GWA:", list_of_student_with_highest_gwa)
print("GWA:", highest_gwa)