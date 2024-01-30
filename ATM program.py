import datetime
language_selection= """ 
1.TELUGU
2.ENGLISH
3.HINDI   """
menu=""""
1.CHECK BALENCE
2.DEPOSIT MONEY
3.WITHDRAW MONEY
4.MINI STATEMENT
5.EXIT
     """
pin=8855
time=datetime.datetime.now()
Amount=0
print(language_selection)                        
l_option=int(input("SELECT OPTIONS"))
if l_option==2:  
    while True:
            user_pin=int(input("ENTER PIN:"))
            if user_pin==pin:
                print(menu)
                option2=int(input("Select any one option "))
                if option2==1:                    
                    print(f"AVAILABLE BALANCE RS {Amount}")
                    print("********")
                elif option2==2:
                    deposit_money=float(input("ENTER AMOUNT: "))
                    Amount+=deposit_money
                    print("DEPOSIT TRANSACTION IS SUCCESSFUL")
                    print("********")
                elif option2==3:
                    print("AVAIL BAL IS", Amount)
                    with_draw=float(input("ENTER AMOUNT: "))
                    if with_draw<=Amount:
                        Amount-=with_draw
                        print(f"AVAILABLE BALANCE RS {Amount}")
                        print("********")
                    else:
                        print("INSUFFICIENT BALANCE")
                        print("********")
                elif option2==4:
                    print("STATE BANK OF INDIA")
                    print("STATEMENT FOR XXXXXXXXXXXXX2343")
                    print(f"AVAIL BAL  {Amount}.50+")
                    print(time)
                    print("********")
                elif option2==5:
                    print("THANK YOU.VISIT AGAIN :)")
                    print("visit us at www.sbi.com")
                    print("********")
                    break     
            else:
                print("INVALID PIN.PLEASE ENTER VALID PIN")
else:
   print("please select ENGLISH :)")
