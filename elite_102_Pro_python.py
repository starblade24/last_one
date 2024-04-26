import mysql.connector

def menu():
  print("--------------------------------------------")
  print("1. View Account Balances ")
  print("2. Deposit ")
  print("3. Withdraw ")
  print("4. Delete account")
  print("5. Make accoount")
  print("6. Change account details")
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

  elif userInput == 3:
    amount = int(input("How much would you like to withdraw?: "))
    if amount <= 0:
      print("Can not put negative amount out")
    else:
      testQuery = ("UPDATE bank  SET money = -" + str(amount) + " + money  WHERE acc_name = " + "'" + name + "'") 
      cursor.execute(testQuery)
      testQuery = ("SELECT * FROM sample.bank WHERE acc_name = " +  "'" + name + "'" )
      cursor.execute(testQuery)
      for row in cursor:
          print(row)
      connection.commit()



  elif userInput == 4:
    testQuery = ("delete from bank where acc_name = " + "'" + name + "'") 
    cursor.execute(testQuery)
    testQuery = ("SELECT * FROM sample.bank WHERE acc_name = " +  "'" + name + "'" )
    cursor.execute(testQuery)
    for row in cursor:
        print(row)
    connection.commit()
    print("Account deleted succfully :)")

  elif userInput == 5:
    stats = int(input("How much money would you like to start with?"))
    acc_de = input("What one word should be your detail? (no spaces)")
    if " " in acc_de:
      print('No spaces')
    else:
      testQuery = ("INSERT INTO bank(money, acc_name, details) VALUES (" + str(stats) +  ", '" + name + "' , '" + acc_de +"');") 
      cursor.execute(testQuery)
      testQuery = ("SELECT * FROM sample.bank WHERE acc_name = " +  "'" + name + "'" )
      cursor.execute(testQuery)
      for row in cursor:
          print(row)
      connection.commit()

  elif userInput == 6:
    new_de = input("what new one word should your details be now?")
    testQuery = ("UPDATE bank SET details = '" + new_de +   "' WHERE acc_name = '" + name +  "';") 
    cursor.execute(testQuery)
    testQuery = ("SELECT * FROM sample.bank WHERE acc_name = " +  "'" + name + "'" )
    cursor.execute(testQuery)
    for row in cursor:
        print(row)
    connection.commit()
  






menu()
options()

    
