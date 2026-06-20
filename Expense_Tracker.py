#Expense Tracker Project 
expenseslist=[] #list of all expenses in form of dictionary
print("Welcome to Expense Tracker ")
while True:
    print("==MENU==")
    print("1.Add Expense")
    print("2.View all Expenses")
    print("3.View Total Expenses")
    print("4.Exit")

    choice = int(input("Please Enter Your Choice :"))
    
#add expense    
    if(choice == 1):
        date = input("enter date in format DD/MM/YYYY : ")
        category=input("Enter the Category (Food,Tavel,Makeup,etc) : ")
        description =input("Product Detail : ")
        amount = float(input("Enter the amount : "))

        expense={
            "Date":date,"Category":category,"Description":description,"Amount":amount}
        expenseslist.append(expense)
        print("\n Done , Expense is added successfully ")

#2 view all expenses
    elif(choice==2):
        if(len(expenseslist)==0):
            print("No Expenses")
        else:
            print("===== Your Expenses=====")
            count=1
            for eachexpense in expenseslist:
                print(f"Expense Number {count} -> {eachexpense["Date"]},{eachexpense["Category"]},{eachexpense["Description"]},{eachexpense["Amount"]}")
                count=count+1

#3. View Total Spending        
    elif(choice == 3):
        total = 0
        for eachexpense in expenseslist:
            total=total + eachexpense["Amount"]

        print("\n TOTAL EXPENSE = " ,total)

#4 Exit
    elif(choice==4):
        print("Thank You")
        break

    else:
        print("Invalid")
