'''This program will quiz the user on the New Zealand TV show, Shortland Street'''

#Introduces the user to the quiz to get them familiar with the questions that will be asked
print("Welcome to the Shortland Street quiz!")
print("This quiz will test your knowledge of shortland street through a series of:\nMultichoice, true or false, and number questions!")
print("Have fun!")

#This stores the questions and answers that the user will be asked
questions = {"True or false. Did Shortland street debut in 1995?" : "false",
            "True or false. Is Shortland Street the longest running NZ TV show?" : "true",
            "What year did Ed Sheeran have a cameo on the show?" : 2014,
            "What drink replaced sparkling wine with when filming?\n1) L&P,\n2) Sprite,\n3) Ginger Beer,\n4) None" : 1,
            "How many episodes are aprroximately produced in 5 days?" : 5,
            "True or false. Is Jamie Forest the first homosexual character in the show?" : "true",
            "True or false. Was Dr. Chris Warner recently introduced to the show" : "false",
            "How many original characters are there?\n1) 13,\n2) 14,\n3) 15,\n4) 16" : 4
            }

#This variable keeps track of the user's score 
score = 0

#These lists contain the possible right answers to the multivhoice and true or false questions
multichoice = [1, 2, 3, 4]
truefalse = ["true", "false"]

#Using a for loop will provide the user with questions
for question, answer in questions.items():
    #When the user answers with the valid answer, this loop will break
    while True:
        user_answer = input(f"{question}\n")
        #Catagorises the answers so the code doesn't test for e.g. a multichoice question
        if answer in truefalse:
            #Until the user answers either true or false, the while-loop will keep asking for another input
            while user_answer.lower() not in truefalse:
                print("Please enter either true or false.")
                user_answer = input(f"{question}\n")
            if str(answer) == str(user_answer.lower()):
                print("Next question:")
                #Adds 1 to the user's final score
                score += 1
                #Breaks the loop so it can ask the user the next question
                break
            else:
                print("Next question:")
                break 
        
        #Catagorises the questions in which their answer is an interger
        elif type(answer) == int:
            try:
                #This seperates questions that have multichoice answers or not
                if answer in multichoice:
                    if int(user_answer) == int(answer):
                        print("Next question:")
                        score += 1
                        break
                    #Sets an boundary on what the user can input so it won't accept an answer for which user_answer<=0
                    elif int(user_answer) <= 0:
                        print("Please choose a number from 1-4")
                    #Same instance here but for when user_answer>=5
                    elif int(user_answer) >= 5:
                        print("Please choose a number from 1-4")
                    else:
                        print("Next question:")
                        break        
            except ValueError:
                #try...except Valuerror ensures the user answers an integer
                print("Please answer from the number of mulitchoice questions")

            try:
                #tests for questions which have interger answers but are not multichoice
                if answer not in multichoice:
                    if int(user_answer) == int(answer):
                        print("Next question:")
                        score += 1
                        break
                    #Same instance here but for when user_answer<=0
                    elif int(user_answer) <= 0:
                        print("Please enter a number larger than 0.")
                    #Similar here but for when the the answer is only greater than 2026 as we are in the year 2026
                    elif int(user_answer) > 2026:
                        print("Please enter a number less than 2026.")
                    else:
                        print("Next question:")
                        break
            except ValueError:
                print("Please answer a valid number")

#This calculates the percentage of how many correct answers were given out of all the answers asked
#score/len(questions) was used to make the code more handy incase more questions were to be added in the future   
percent = round((score/len(questions))*100,2)
print(f"{percent}%")

#This gives the user a different comment on their attempt depending on the value of their score
if percent == 100:
    print("Good job, you got a perfect score!")
elif percent >= 80:
    print("Well done!")
elif percent >= 60:
    print("You did good.")
elif percent >= 50:
    print("Nice try.")
else:
    print("Better luck next time")