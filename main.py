import os, time
todoList = []

def printList():
  print()
  for items in todoList:
    print(items)
  print()

while True:
  menu = input("TODO Lsit Manager\n Do you want to add, view, edit, or remove an item from the to do list?")
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What do you want to add?\n").title()
    todoList.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?\n").title()
    check = input("Are you  sure you want to remove this?\n")
    if check[0] =="y":
      if item in todoList:
        todoList.remove(item)
  elif menu == "edit":
    item = input("What do you want to change it to?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(todoList)):
      if todoList[i] == item:
        todoList[i] = new
  elif menu == "delete":
    todoList = []
  time.sleep(1)
  os.system('clear')
    
