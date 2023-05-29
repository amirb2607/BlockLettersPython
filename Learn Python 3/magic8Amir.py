import random

name = "Amir"
#name = ""
question = "Are you a student?"
#question = ''
answer = ''
random_number = random.randint(1,12)
#print(random_number)

#Random response
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Probably not"
elif random_number == 11:
  answer = "Most likley"
elif random_number == 12:
  answer = "LMAO NOPE"
else:
  answer = "Error"

#Checks if name is blank or not.
if not question == '':
  if not name == '':
    print(name + " asks: " + question)  
  else:
    print("Question: " + question)
else:
  print("Question is blank...")

print("Magic 8-Ball's answer: " + answer)p
