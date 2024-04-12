thisdict = {
}

def save():
  x = input("Enter a website: ")
  y = input("Enter your password: ")
  thisdict[x] = y

def retrieve():
  x = input("Enter a website: ")
  print(thisdict[x])

def view():
  print(thisdict)

print("Type save to save a new password")
print("Type retrieve to retrieve a password")
print("Type view to view all passwords")
print("Type exit to exit the program")
count = True
while(count):
  inp = input("Enter your command: ")
  if inp == "save":
    save()
  elif inp == "retrieve":
    retrieve()
  elif inp == "view":
    view()
  elif inp == "exit":
    count = False
  else:
    print("Invalid input")







