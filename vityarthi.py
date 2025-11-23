print("an account management system is here to help")
acc=[]
def create_account():
     name=input("enter the holders name:")
     bal=int(input("enter balance"))
     acno=input("create and enter the account number")
     acc.append(acno)
     acc.append(name)
     acc.append(bal)
     print("account successfully created")
def view_account():
    if len(acc)!=0:
        print(acc)
    else:
        print("account does not exist")
def deposit():
        b=input("enter the account no.")
        bal=int(input("enter the amount deposited"))
        if acc[0]==b:
               g=acc[2]+bal
               print("amount successfully deposited")
               acc[2]=g
               return acc[2]
        else:
           print("account doesn't exist")
def withdraw():
        b=input("enter the account no.")
        bal=int(input("enter the amount withdrawn"))
        if acc[0]==b:
                if acc[2]>=bal:
                   e=acc[2]-bal 
                   print("amount successfully withdrawn")
                   acc[2]=e
                   return acc[2]
                else:
                   print("insufficient balance")
        else:
           print("account doesn't exist")
def check_balance():
    print("balance in account is",acc[2])
while True:
  print("its here to help certain account management tasks such as:")
  print("1.create an account")
  print("2.view an account")
  print("3.deposit in account")
  print("4.withdraw from account")
  print("5.to check balance")
  print("6.Exit")
  ch=int(input("enter your choice"))
  if ch==1:
     create_account()
  elif ch==2:
     view_account()
  elif ch==3:
     deposit()
  elif ch==4:
     withdraw()
  elif ch==5:
      check_balance()
  elif ch==6:
      print("thank you")
      break
  else:
      print("invalid choice")
