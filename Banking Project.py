pin = "4567"
Amount = 10000
while True:
    wrong = 0
    while True:
        Enter_PIN = input("Enter your PIN to withdraw/deposit cash or q to Quit: ")
        if Enter_PIN == "q":
            break
        if Enter_PIN == pin:
            print("")
            print("*"*20)
            print("Correct Pin Entered!")
            print("*"*20)
            print("")
            print("You have ",Amount," bath in your account.")
            print("")
            while True:
                Service = input("Press 1 to deposit or 2 to withdraw: ")
                print("")
                if Service == "1":
                    Deposite = int(input("Enter an amount to deposit: "))
                    Amount = Amount + Deposite
                    print("-"*20)
                    print("")
                    print("|"," ","DEPOSIT FUND"," ","|"," ","BALANCE"," ","|")
                    print("|"," "*5,Deposite," "*5,"|"," "*2,Amount," "*2,"|")
                    print("")
                    print("-"*20)
                    break
                if Service == "2":
                        Withdraw = int(input("Enter an amount to withdraw: "))
                        if Withdraw<=Amount:
                            Amount = Amount - Withdraw
                            print("-"*20)
                            print("")
                            print("|"," ","Withdraw FUND"," ","|"," ","BALANCE"," ","|")
                            print("|"," "*5,Withdraw," "*5,"|"," "*2,Amount," "*2,"|")
                            print("")
                            print("-"*20)
                            break
                        else:
                            print("*"*20)
                            print("Not Enough Money In The Account.")
                            print("Please Try Again.")
                            print("*"*20)
                            break
            break
        if Enter_PIN != pin:
            wrong +=1
            print("Attempt# ",wrong,".Incorrect PIN!! Try Again.")
        if wrong ==3:
            break
    if Enter_PIN == "q":
         break
    print("")
    Decide = input("Press enter to continue")
    print("")
    if Decide == "":
        if wrong >= 3:
            print("Your account is locked. Please contact bank.")
            break
        else:
            continue
    else:
        continue



            

