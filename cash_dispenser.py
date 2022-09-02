name=input()
surname=input()
accountNo=input()
accountState=int(input())
accountAdd=int(input())

AccountS = {
    'Name':name,
    'Surname':surname,
    'Account No': accountNo,
    'Account State': accountState,
    'Account Add'  : accountAdd
  
}

AccountA = {
    'Name':"Elif",
    'Surname':"Bekir",
    'Account No': "85845",
    'Account State': 2000,
    'Account Add'  : 3000
}
AccountB = {
    'Name':"Deniz",
    'Surname':"Sedir",
    'Account No': "83845",
    'Account State': 4000,
    'Account Add'  : 1000
}
AccountC = {
    'Name':"Kadir",
    'Surname':"Kiraz",
    'Account No': "83844",
    'Account State': 1000,
    'Account Add'  : 1000
}

def withdrawMoney(account,quantity):
    print(f"Welcome to the account  {account['Name']} ")
    
    
    if  account['Account State']>=quantity:
     account['Account State'] =  account['Account State']-quantity 
     print("You can get the money")
     
  
    else :
        if account['Account State']+ account['Account State']>quantity:
          print("Would you like to use your additional account?")
          a=input("y or n")
          if a =='y':
            summ=account['Account State']+ account['Account Add']
            summ=summ-quantity
            print("You can get the money")
          else:
            print("Your account is insufficient")




def depositMoney(account,quantity):
    print(f"Welcome to the account  {account['Name']} ")
    print("Please choose")
    a=int(input("1- Adding account or 2- Adding aditional account"))
    if a==1:
      summ=account['Account State']+quantity
      print(f" Account money quantitiy:{summ}")
    else:
       summ=account['Account Add']+quantity
       print(f"Additional account money quantitiy:{summ}")




def showAccount(account):
  print(f"Welcome to the account  {account['Name']} ")
  a=int(input("1- Account or 2- Aditional account"))
  if a==1:
      print(f" Account money quantitiy:{account['Account State']}")
  else:
     print(f"Additional account money quantitiy:{account['Account Add']}")

     
withdrawMoney(AccountS,3000)
withdrawMoney(AccountA,3000)
depositMoney(AccountS,3000)
depositMoney(AccountA,3000)
showAccount(AccountS)
showAccount(AccountA)
