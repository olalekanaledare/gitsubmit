
print("Welcome to ABC Bank\n\ninsert your card")

password=1234
balance=10000
choice=0

pin=int(input("Enter ur four digit pin"))
   
if pin==password:

   while choice !=4:

     print("\n\n****menu***")
     print("1 == balance")
     print("2 == deposit")
     print("3 == withdraw")
     print("4 == cancel\n")

     choice=int(input("\nEnter ur option:\n"))

     if choice==1:
        print("Balance = R" , balance)
        
     elif choice==2:
        dep=int(input("Enter ur deposit: R"))
        balance += dep
        print("\ndeposited amount: R" ,dep)
        print("Balance = R" , balance)

     elif choice==3:
        wit=int(input("Enter the amt to withdrw: R"))
        balance -= wit
        print("\nwithdrawn amount: R" ,wit)
        print("Balance = R" , balance)

     elif choice==4:
        print("\n Session ended!! Goodbye")

     else:
        print("\nInvalid entry!!")

else:
   print("Pin incorrect!! Try again")
   
