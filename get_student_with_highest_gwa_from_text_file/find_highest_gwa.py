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

# Bold to emphasize
bold_start = "\033[1m" + "\033[95m"
bold_end = "\033[0;0m"

# print the name and gwa of the student with the highest gwa
print("\n" + bold_start + "Student/s with the highest GWA:" + bold_end, list_of_student_with_highest_gwa)
print(bold_start +"GWA:" + bold_end, highest_gwa, "\n")