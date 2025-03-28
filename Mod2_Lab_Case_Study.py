"""
Mark Klein
App Name: The List

This app will take input for a students name and GPA and will give an output 
of whether or not the student has made the deans list (3.5 GPA or higher) or
the Honor Roll (3.25 - 3.4). 

Enter "zzz" when entering the students last to quit the app.

"""

while True: #Initiate while loop to accept and intialize first and last name or to quit with ZZZ
    last_name = input("Enter Students Last Name (Enter ZZZ to quit): ")
    if last_name == "ZZZ":
        quit()
    first_name = input("Enter Students First Name: ")

    while True: #While loop to retrieve gpa in specific range and retry if not in correct range.
        gpa = float(input("Enter Student GPA: "))
        if 0.0 <= gpa <= 4.0: #Struggled to figure out this range, had it backwards for a long while.
            break
        print("Please enter a correct GPA range of 0.00 through 4.00")

    #Logic for the tier of grades for student    
    if gpa >= 3.5:
        print(f"Congradulations {first_name} {last_name} you have made the Deans List!")
    elif gpa >= 3.25 and gpa <= 3.4:
        print(f"Congradulations {first_name} {last_name} you are on the Honor roll!")
    elif gpa >= 0 and gpa <= 3.24:
        print(f"Sorry {first_name} {last_name} you are not on the Honor Roll or the Deans List V_V")

    else:
        print("")