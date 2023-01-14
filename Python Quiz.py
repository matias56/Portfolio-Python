print(f"Welcome to my Computer Quiz!")

play = input(f"Want to play?")

if play.lower()!= "yes":
    print(f"See ya!")

score = 0

q1 = input(f"What does CPU stands for?")

if q1.lower() == "central processing unit":
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")
    
q2 = input(f"What does GPU stands for?")

if q2.lower() == "graphics processing unit":
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")

q3 = input(f"What does RAM stands for?")

if q3.lower() == "random access memory":
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")

q4 = input(f"What does PSU stands for?")

if q4.lower() == "power supply":
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")


q5 = input(f"Which year was Python created?")

if q5 == '1980':
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")

q6 = input(f"Who created Python?")

if q6.lower() == "guido van rossum":
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")


q7 = input(f"Which Python version is the latest?")

if q7 == '3.12':
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")


q8 = input(f"Which sequence of bytes is mutable?")

if q8.lower() == 'bytearray':
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")

q9 = input(f"What are +, - and *?")

if q9.lower() == 'expressions':
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")

q10 = input(f"Django is a web framework originated from Python. True or False?")

if q10.lower() == 'true':
    print(f"Correct!")
    score += 1
else:
    print(f"Incorrect.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
