import time
dict={}

while True:
  
  def func():
    print("***** Instruction👇 ****** ")
    print("Type a or A to create new data")
    print("Type b or B to show data")
    print("Type c or C to edit the data")
    print("Type d or D to delete the data")
    print("Type e or E to exit")
    
  func()
  print("")
  time.sleep(1)
  user=input("Enter your choice:  ")
  
  if user =="a" or user =="A":
    name=input("Enter your name: ")
    address=input("Enter your address:  ")
    nation=input("Enter your Nationality:  ")
    dict[name]=address
    dict[address]=nation
    
  elif user=="b" or user=="B":
    name=input("Enter the name: ")
    if name in dict.keys():
      print("")
      time.sleep(1)
      print("Name is "+name+".🚻")
      time.sleep(3)
      print("Live in country "+ dict[address]+".🌎")
      time.sleep(2)
      print("Location is "+ dict[name]+".🏰")
    else:
      print("* No Data found * ")
      print("!!* Store the data *!!")
      
  elif user=="c" or user== "C":
     name=input("Enter the name: ")
     if name in dict.keys():
       address=input("Enter your address: ")
       nation=input("Enter your Nationality: ")
       dict[name]=address
       dict[address]=nation
     else:
       print("Your name doesn't exists!!")
   
  elif user=="d" or user== "D":
     name=input("Enter the name: ")
     if name in dict.keys():
       del dict[name],dict[address]
     else:
       print("Name not found***!")
  elif user=="e" or user=="E":
     break
  else:
    print("*Read the instruction carefully!*")
     
  print("")
  time.sleep(3)