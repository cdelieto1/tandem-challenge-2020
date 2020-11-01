'''
    TANDEM TRIVIA by Cassandra Delieto (C) 2020
'''

import json
import random
import time


def run_trivia():

    #SET GLOBAL VARIABLES AS DEFAULT COUNTERS
    high_score = 0
    number_answered_quest = 0
    number_max_quest = 9 #Runs for 10 questions
    user_input_tries = 0
    max_input_tries = 2

    with open('trivia_questions.json', 'r') as file:
        data = file.read().replace('\n', '')

    trivia_data = json.loads(data)
    random.shuffle(trivia_data) # randomize trivia questions

    #HEADER OF GAME
    print("\nWELCOME TO THE TRIVIA GAME!\n")
    print("Read the question and answer by entering a number between 1-4.")
    print("Your final score will be displayed at the end.\n")
    print("READY, SET, GO!\n")

    #INDEX AND PARSE EACH QUESTION INTO AN ARRAY W/ ANSWERS AS BOOLEANS
    for index, data in enumerate(trivia_data):
        
        question = data["question"]
        answer_dict = []

        print(f'Question #{index+1} : {question}\n')

        # Prepare answers
        for wrong_answer in data['incorrect']:
            answer_dict.append([wrong_answer, False])
        answer_dict.append([data['correct'], True])
        random.shuffle(answer_dict) # randomize answers

        for index, answer in enumerate(answer_dict, 1):
            print("%s: %s" % (index, answer[0]))

        #Evaluate input of user using stdin.
        valid_input = False
        while not valid_input:
            try:
                user_input = int(input("\nYour answer is: "))
                if user_input > 0 and user_input < 5:
                    print(f'Your final answer was: {answer_dict[user_input-1][0]}') # string answer (key)
                    valid_input = True
                else:
                    print("Answer must be between 1-4! Try again plz. Tries left: %s" % (max_input_tries-user_input_tries))
            except:
                print("Answer must be between 1-4! Try again plz. Tries left: %s" % (max_input_tries-user_input_tries))

            if user_input_tries == max_input_tries:
                print("\nSorry, you clearly can't follow instructions. Giving up!\n")
                exit()
            user_input_tries += 1

        user_input_tries = 0

        if answer_dict[user_input-1][1]:
            high_score += 100
            print("\nCORRECT!\n")
        else:
            for solution in answer_dict:
                if solution[1]:
                    print("\nWRONG! The correct answer is: %s\n" % solution[0])
                    break

        # Limit questions
        if number_answered_quest < number_max_quest:
            number_answered_quest += 1
        else:
            break


    # Finalization
    print("\nNOW, FOR THE FINAL SCORE!")
    time.sleep(2)
    print("\nDrum Roll please...")
    time.sleep(2)
    print("\n...")
    time.sleep(2)
    print("\nThe suspense is killing me too ;)")
    time.sleep(2)
    if high_score > 0:
        print("\nYour final score is: %s 🎉\n" % high_score)
    else:
        print("\nYou really are not good at this game! 🤮\n")


if __name__ == '__main__':
    # TODO: implement unit tests
    run_trivia()

