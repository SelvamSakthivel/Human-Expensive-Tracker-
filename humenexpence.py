#Personal Expense Tracker
print("Welcome To Your Personal Expense Tracker ☺")
def login():
    user_name = input("Enter your UserName:")
    mail_id = input("Enter Your MailID:")
    enter_mail_id = input("ReEnter Your EmailID:")
    #Condition from mailid
    if mail_id == enter_mail_id:
        if "@" in mail_id and "." in mail_id:
            print("Mail ID Login Successfully")
        else:
            print("Invalied Email Format (Missing @ or .)")
    else:
        print("MailID Mismatch")
    user_password = input("Enter your 4-Digit Password:")
    enter_password = input("ReEnter Your 4-Digit Password:")
    #condition from password
    if user_password == enter_password:
       if  user_password.isnumeric() and enter_password.isnumeric():
           print("Password Correct.....")
       else:
           print("Invalied Password Reson You Only use numbers Don'n allowe for Letters")
    else:
        print("Wrong Password")
login()

#User INTERFACE
def personal():
    print("PERSONAL EXPENCE TRACKER")
    month_salary = int(input("Enter Your Monthly Salary:"))
    family_expensive = int(input("Enter your family Expensive:"))
    shopping_expensive = int(input("Enter Your Shopping Expensive"))
    food_expensive = int(input("Enter Your Food Expensive:"))
    bike_expensive = int(input("Enter your bike Expensive:"))
    current_bill = int(input("Enter Your Current Biss Payment:"))
    hospital_expensive = int(input("Enter Your Hospital Expensive:"))
    other_expensive = int(input("Other Expensive:"))
    
    print("So Your Expensive Amount And Your Savings")
    total_expenses = (family_expensive + shopping_expensive + food_expensive +
                  bike_expensive + current_bill + hospital_expensive + other_expensive)
    #calculate Savings
    savings = month_salary - total_expenses
    expensive = total_expenses
    #Check  Balance if Statement
    if savings>0:
        print("This Month Savings:",savings)
    elif savings == 0:
        print("No savings, you spent everything.")
    else:
        print("You are in loss! Expenses are more than salary")
personal()           
            
    
    
