'''This program will quiz the user on the New Zealand TV show, Shortland Street'''

#This stores the questions and answers that the user will be asked
questions = {"True or false. Did Shortland street debut in 1995?" : "False",
            "True or false. Is Shortland Street the longest running NZ TV show?" : "True",
            "What year did Ed Sheeran have a cameo on the show?" : "2014",
            "What drink replaced sparkling wine with when filming?" : "L&P",
            "How many episodes are produced in 5, 10-hour working days?" : "5",
            "Who was the first gay character in the show?(Answer with the character's stage name)" : "Jamie Forest",
            "Who is the longest running original character?" : "Dr. Chris Warner",
            "How many original characters are there? A) 13, B) 14, C) 15, D) 16" : "D"
            }

#Keeps track of the user's score
score = 0

#Using a for loop will provide the user with questions
for question, answer in questions.items():
    try:
        user_answer = input(question)
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
    except Exception as error:
        print(f"{error}! Please answer with a valid response.")

percent = score/10

        