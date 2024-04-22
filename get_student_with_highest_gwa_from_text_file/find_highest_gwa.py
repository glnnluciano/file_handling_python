# open the text file and read per line
with open("class_record.txt", "r") as class_record:
    for line in class_record:
        
# separate the name and gwa
        student_name, gwa = line.strip().split(",")
        gwa = float(gwa)
# find the highest gwa
# print the name and gwa of the student with the highest gwa