'''This program will quiz the user on the New Zealand TV show, Shortland Street'''

#Introduces the user to the quiz to get them familiar with the questions that will be asked
print("Welcome to the Shortland Street quiz!")
print("This quiz will test your knowledge of shortland street through a series of:\nMultichoice, true or false, and number questions!")
print("Have fun!")

#This stores the questions and answers that the user will be asked
questions = {"True or false. Did Shortland street debut in 1995?" : "False",
            "True or false. Is Shortland Street the longest running NZ TV show?" : "True",
            "What year did Ed Sheeran have a cameo on the show?" : 2014,
            "What drink replaced sparkling wine with when filming?\nA) L&P,\nB) Sprite,\nC) Ginger Beer,\nD) None\n" : "A",
            "How many episodes are produced in 5, 10-hour working days?" : 5,
            "True or false. Is Jamie Forest the first homosexual character in the show?" : "True",
            "True or false. Was Dr. Chris Warner recently introduced to the show" : "False",
            "How many original characters are there?\nA) 13,\nB) 14,\nC) 15,\nD) 16\n" : "D"
            }

#Keeps track of the user's score
score = 0

#Using a for loop will provide the user with questions
for question, answer in questions.items():
    while True:
        #asks the user for the answer to the question
        user_answer = input(question)
        if type(answer) == str:
            try:
                if answer.lower() == user_answer.lower():
                    print("Correct! Next question!")
                    score += 1
                else:
                    print("Wrong. Moving on.")
                break
            except Exception as error:
                print(error)
        elif type(answer) == int:
            try:
                user_answer == int(user_answer)
                if user_answer == answer:
                    print("Correct! Next question")
                    score += 1
                elif user_answer <= 0:
                    print("Please enter a number larger than 0.")
                elif user_answer > 2026:
                    print("Please enter a number less than 2026.")
                else:
                    print("False. Moving on.")
                break
            except ValueError:
                print("Please enter a valid number!")

percent = round((score/len(questions))*100,2)
print(f"{percent}%")