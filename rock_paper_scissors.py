import random
import time
l=("ROCK","PAPER","SCISSOR")
#Title
print('=-='*18)
print('WELCOME TO COMPUTER VS YOU')
print('=-='*18)
#Programming
print("")
print("TO PLAY  PRINT[A]")
print("")
s=input("ENTER YOUR CHOICE:>> ")
print("")
if s == "A":
  print("WELCOME TO PLAY WITH COMPUTER")
  print("")
  q=input("ENTER YOUR NAME")
  print("")
  print("WELCOME:::",q,"TO GAME")
  print("your opponent name is :: AI")
  print("")
  # Main game..loop
  user=0
  AI=0
  game=0
  gameloop=5
  while game<5:
    time.sleep(3)
    print("===================")
    print(" _____")
    print("|               |")
    print("| [R] FOR ROCK  |")
    print("| [P] FOR PAPER |")
    print("| [S] SCISSOR   |")
    print("|_____|")
    print("===================")
    x=input("ENTER COD IN BOX []")
    ai=random.choice(l)
    #win.lose points
    user+=0
    AI+=0
    # main code
    if x=="R" and ai=="ROCK":
      print("______")
      print("===== TIE =====")
      print("")
      print("AI CHOICE:>>",ai)
      print("__________")
       
    if x=="R" and ai=="PAPER":
      print("________")
      print("===== AI WIN ======")
      print("")
      print("AI CHOICE:>>",ai)
      print("__________")
      AI+=1
    
    if x=="R" and ai=="SCISSOR":
      print("_______")
      print("==== YOU WIN ==== ")
      print("")
      print("AI CHOICE:>>",ai)
      print("__________")
      user+=1
    
    if x=="P" and ai=="PAPER":
      print("______")
      print("==== TIE ====")
      print("")
      print("AI CHOICE:>>",ai)
      print("__________")
         
    if x=="P" and ai=="RAOCK":
      print("________")
      print("===== YOU WIN =====")
      print("")
      print("AI CHOICE:>>",ai)
      print("__________")    
      user+=1   
    if x=="P" and ai=="SCISSOR":
      print("______")
      print("===== AI WIN =====")
      print("")
      print("AI CHOICE:>>",ai)
      print("__________")
      AI+=1 
      
    if x=="S" and ai=="PAPER":
      print("_______")
      print("===== YoU WIN =====")
      print("")
      print("AI CHOICE:>>",ai)
      print("__________")
      user+=1
      
    if x=="S" and ai=="SCISSOR":
      print("_______")
      print("===== TIE ===== ")
      print("")
      print("AI CHOICE:>>",ai)
      print("__________")
      
    if x=="S" and ai=="ROCK":
      print("______")
      print("===== AI WIN =====")
      print("")
      print("AI CHOICE:>>",ai)  
      print("__________")
      AI+=1
      
    # WIN OR LOSE
      
    if user==5:
      print("==================")
      print("==================")
      print(" YOU WIN THE ROUND")
      print("==================")
      print("==================")
      break
      
    if AI==5:
       print("==================")
       print("==================")
       print(" YOU LOST ROUND")
       print("==================")
       print("==================")
       break