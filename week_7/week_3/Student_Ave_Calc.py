choice = "y"
while choice =="y":
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # canculating the average:
    average =(quiz_1  + quiz_2 + quiz_3) / 3
    print(f"The average mark is:{average}")

    if average >=50:
        print("status: Pass")
    else:
        print("status: Fail")
    
    choice = input("Do you want to enter student's marks? (y/n: )").lower()

print("prrogram Ended")


