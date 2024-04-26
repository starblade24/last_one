import mysql.connector

def menu():
  print("--------------------------------------------")
  print("1. View Account Balances ")
  print("2. Deposit ")
  print("3. Withdraw ")
  print("4. Delete account")
  print("5. Update account details")
  print("--------------------------------------------")

connection = mysql.connector.connect(
        user = 'root', 
        database = 'sample', 
        password = 'Starsans47$'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM sample.bank")
cursor.execute(testQuery)

for row in cursor:
  print(row)



def options():
  name = input("What is your name?: ")
  userInput = int(input("What would like to do?: "))
  
  if userInput == 1:
    try:
      testQuery = ("SELECT * FROM sample.bank WHERE acc_name = " +  "'" + name + "'" )
      cursor.execute(testQuery)
      for row in cursor:
        print(row)
      connection.commit()
    except ValueError:
      print("not a name in out database, would you like to make a acc?")
    menu()
    options()

  elif userInput == 2:
    amount = int(input("How much would you like to deposit?: "))
    if amount <= 0:
      print("Can not put negative amount in?")
    else:
      testQuery = ("UPDATE bank  SET money = " + str(amount) + " + money  WHERE acc_name = " + "'" + name + "'") 
      cursor.execute(testQuery)
      testQuery = ("SELECT * FROM sample.bank WHERE acc_name = " +  "'" + name + "'" )
      cursor.execute(testQuery)
      for row in cursor:
        print(row)
      connection.commit()
"""
  elif userInput == 3:
    menu()
  elif userInput == 4:
    loop = False
    print("bye bye ;)")

loop = True
  



while loop == True:
    menu()

"""
menu()
options()

    
