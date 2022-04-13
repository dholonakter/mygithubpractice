print("welcome to computer quizz")
playing=input("Do you want to play? ")
if playing !="yes":
    quit()
print("Okay!Let's play :)")
answer=input("What does CPU stand for?")
print("Remember, CPU is an abbreviation!")
print("Remember, it is in your PC!!")
if answer=="Central processing unit":
    print('Correct!')
else:
    print("Incorrect")
answer=input("What does GPU stand for?")

print("this answer should not be visible")
print(type(answer), "this is the type of the answer")

if answer=="Graphical processing unit":
    print('Correct!')
else:
    print("Incorrect")
