'''This program will quiz the user on the New Zealand TV show, Shortland Street'''

#This stores the questions and answers that the user will be asked
questions = {"True or false. Did Shortland street debut in 1995?" : False,
            "True or false. Is Shortland Street the longest running NZ TV show?" : True,
            "What year did Ed Sheeran have a cameo on the show?" : 2014,
            "What drink replaced sparkling wine with when filming?\nA) L&P,\nB) Sprite,\nC) Ginger Beer,\nD) None\n" : "A",
            "How many episodes are produced in 5, 10-hour working days?" : 5,
            "Who was the first gay character in the show?(Answer with the character's stage name)" : "Jamie Forest",
            "Who is the longest running original character?" : "Dr. Chris Warner",
            "How many original characters are there?\nA) 13,\nB) 14,\nC) 15,\nD) 16\n" : "D"
            }

#Keeps track of the user's score
score = 0

#asks the user for the answer to the questions
user_answer = input(question)

#Using a for loop will provide the user with questions
for question, answer in questions.items():
    if type(answer) == str:
        try:
            user_answer = input(question)
            if user_answer.lower() == answer.lower():
                print("Correct!")
                score += 1
            else:
                print("False.")
        except Exception as error:
            print(f"{error}!")
    
    if type(answer) == int:
        user_answer = False
        print(question)
        while user_answer == False:
            try:
                user_answer = int(input())
                if user_answer == answer:
                    print("Correct")
                    score += 1
                    user_answer == True
                else:
                    print("False")
                    user_answer == True
            except ValueError:
                print("Please re-enter a valid number.")
                user_answer = int(input())
                user_answer = False
    if type(answer) == bool:





percent = round((score/len(question))*1000,2)
print(f"{percent}%")