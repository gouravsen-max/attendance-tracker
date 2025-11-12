import datetime
                                        #......................(Task 1)......................
print("\nWelcome to Attendance Tracker!")
print("This tool helps record and manage student attendance.\n")

                                        #......................(Task 2 + 3)......................
att = {}

n = int(input("How many students you want to record?  "))

for i in range(n):
    print("\nEntry", i+1)

    while True:
        name = input("Enter student name: ")
        name = name.strip()
        
        if name == "":
            print("Error: Name cannot be empty. Please try again.")
        
        elif name in att:
            print("Error: This student's attendance is already marked. Try again.")
        
        else:
            break

    while True:
        time = input("Enter check-in time (like 09:15 AM): ")
        time = time.strip()

        if time == "":
            print("Error: Timestamp is missing. Please re-enter the time.")
        else:
            break

    att[name] = time
    print("Record added successfully for", name)

print("\n--- Data collection complete. ---")
                                        #......................(Task 4)......................

print("\n==============================")
print("   Attendance Summary")
print("==============================")

print("Student Name\t|\tCheck-in Time")
print("--------------------------------------")

for name in att:
    print(name, "\t\t|\t", att[name])

print("--------------------------------------")

present_count = len(att)

print("\nTotal Students Present: " + str(present_count))
                                        #......................(Task 5)......................
print("\n--- Absentee Calculation ---")

total_students = 0
absent_count = 0

total_input = input("Enter the total number of students in the class (Press Enter to skip): ")

if total_input == "":
    print("Skipping absentee calculation.")

else:
    try:
        total_students = int(total_input)
        
        if total_students < present_count:
            print("Warning: Total students count is less than present students.")
            print("Total Absent: 0")
        else:
            absent_count = total_students - present_count
            print("Total Students in class: " + str(total_students))
            print("Total Absent: " + str(absent_count))
    
    except ValueError:
        print("Error: Invalid input. Sirf number input karo (jaise 10, 20).")
        print("Skipping absentee calculation.")
                                        #......................(Task 6)......................
print("\n--- Save Report to File ---")

save_choice = input("Do you want to save this report to a file? (yes/no): ")

if save_choice.lower() == 'yes' or save_choice.lower() == 'y':
    
    try:
        filename = "attendance_log.txt"
        
        file = open(filename, "w")
        
        now = datetime.datetime.now()
        report_time = now.strftime("%Y-%m-%d %H:%M:%S")
        
        file.write("--- Attendance Report ---\n")
        file.write("Generated on: " + report_time + "\n\n")
        
        file.write("--- Students Present ---\n")
        for name in att:
            file.write(name + " : " + att[name] + "\n")
        
        file.write("\n--- Summary ---\n")
        file.write("Total Students Present: " + str(present_count) + "\n")
        
        if total_input != "":
            file.write("Total Absent: " + str(absent_count) + "\n")
        
        file.close()
        
        print("Successfully saved report to " + filename)

    except:
        print("Error: Could not save the file.")
        
else:
    print("Report not saved.")

print("\n--- Thank you for using the tracker! ---")