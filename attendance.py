Attendance = int(input("enter attendance:"))

if Attendance >= 70:
    grade = int(input("enter grade"))
    if grade > 90:
        print("A")

    elif grade >= 80:
        print("B")

    elif grade >= 70:
        print("C")

    elif grade >= 60:
        print("D")

    else:
        print("F")

else:
    print("sorry you have failed")