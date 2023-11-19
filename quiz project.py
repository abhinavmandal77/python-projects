print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ATM stand for? ")
if answer.lower() == "automated telling machine":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does LED stand for? ")
if answer.lower() == "light emitting diode":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions corrrect!")
print("You got " + str((score/4)*100)+" %")
