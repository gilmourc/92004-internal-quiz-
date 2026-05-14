'''This program will quiz the user on the New Zealand TV show, Shortland Street'''

#Introduces the user to the quiz to get them familiar with the questions that will be asked
print("Welcome to the Shortland Street quiz!")
print("This quiz will test your knowledge of shortland street through a series of:\nMultichoice, true or false, and number questions!")
print("Have fun!")

#This stores the questions and answers that the user will be asked
questions = {"True or false. Did Shortland street debut in 1995?" : "False",
            "True or false. Is Shortland Street the longest running NZ TV show?" : "True",
            "What year did Ed Sheeran have a cameo on the show?" : 2014,
            "What drink replaced sparkling wine with when filming?\n1) L&P,\n2) Sprite,\n3) Ginger Beer,\n4) None" : 1,
            "How many episodes are produced in 5, 10-hour working days?" : 5,
            "True or false. Is Jamie Forest the first homosexual character in the show?" : "True",
            "True or false. Was Dr. Chris Warner recently introduced to the show" : "False",
            "How many original characters are there?\n1) 13,\n2) 14,\n3) 15,\n4) 16" : 4
            }

#Keeps track of the user's score
score = 0

#write somethign here
multichoice = [1, 2, 3, 4]

#Using a for loop will provide the user with questions
for question, answer in questions.items():
    while True:
        user_answer = input(f"{question}\n")
        if type(answer) == str:
            try:
                if user_answer.lower() == answer.lower():
                    print("Correct. Next question")
                    score += 1
                    break
                else:
                    print("Wrong.")
                    break
            except TypeError: 
                print("Please enter either true or false.")
            
        elif type(answer) == int:
            try:
                if answer in multichoice:
                    if int(user_answer) == int(answer):
                        print("Correct! Next question.")
                        score += 1
                        break
                    elif int(user_answer) <= 0:
                        print("Please choose a number from 1-4")
                    elif int(user_answer) >= 5:
                        print("Please choose a number from 1-4")
                    else:
                        print("Wrong. Next question.")
                        break
            except ValueError:
                print("Please answer from the number of mulitchoice questions")

            try:
                if answer not in multichoice:
                    if int(user_answer) == int(answer):
                        print("Correct! Next question")
                        score += 1
                        break
                    elif int(user_answer) <= 0:
                        print("Please enter a number larger than 0.")
                    elif int(user_answer) > 2026:
                        print("Please enter a number less than 2026.")
                    else:
                        print("False. Moving on.")
                        break
            except ValueError:
                print("Please answer a valid number")

   
percent = round((score/len(questions))*100,2)
print(f"{percent}%")

if percent == 100:
    print("yay perfect score")
elif percent >= 80:
    print("good job")
elif percent >= 60:
    print(" you did ok")
elif percent >= 40:
    print("at least you tried")
else:
    print("better luck next time")