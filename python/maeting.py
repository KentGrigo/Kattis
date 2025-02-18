input() # not used
mondayStudents = input().split()
tuesdayStudents = input().split()

output = ""
for mondayStudent in mondayStudents:
    for tuesdayStudent in tuesdayStudents:
        if mondayStudent == tuesdayStudent:
            if output != "":
                output += " "
            
            output += mondayStudent
            break

print(output)
