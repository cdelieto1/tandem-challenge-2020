'''
    TANDEM TRIVIA by Cassandra Delieto (C) 2020
'''

import json
import random
import time


def run_trivia():

    #Set global variables as default counters
    HIGH_SCORE = 0
    NUMBER_ANSWERED_QUEST = 0
    NUMBER_MAX_QUEST = 9 #Runs for 10 questions
    USER_INPUT_TRIES = 0
    MAX_INPUT_TRIES = 2

    #Open JSON file and remove any extra lines.
    with open('trivia_questions.json', 'r') as file:
        data = file.read().replace('\n', '')

    trivia_data = json.loads(data)
    random.shuffle(trivia_data) # randomize trivia questions

    #Header of Game
    print("\nWELCOME TO THE TRIVIA GAME!\n")
    print("Read the question and answer by entering a number between 1-4.")
    print("Your final score will be displayed at the end.\n")
    print("READY, SET, GO!\n")

    #Index and then parse each JSON into an array of K,V === Question, Boolean. 
    for index, data in enumerate(trivia_data):
        
        question = data["question"]
        answer_dict = []

        print(f'Question #{index+1} : {question}\n')

        # Prepare answers
        for wrong_answer in data['incorrect']:
            answer_dict.append([wrong_answer, False])
        answer_dict.append([data['correct'], True])
        random.shuffle(answer_dict) # randomize answers

        #Display numbers question as the first index of each array
        for index, answer in enumerate(answer_dict, 1):
            print(f"{index}: {answer[0]}")

        #Evaluate input of user using stdin and kicked them out after 3 fails.
        valid_input = False

        while not valid_input:
            try:
                user_input = int(input("\nYour answer is: "))
                if user_input > 0 and user_input < 5:
                    print(f'Your final answer was: {answer_dict[user_input-1][0]}') # string answer (key)
                    valid_input = True
                else:
                    print(f'Answer must be between 1-4! Try again plz. Tries left: {MAX_INPUT_TRIES-USER_INPUT_TRIES}')
            except:
                print(f'Answer must be between 1-4! Try again plz. Tries left: {MAX_INPUT_TRIES-USER_INPUT_TRIES}')

            if USER_INPUT_TRIES == MAX_INPUT_TRIES:
                print("\nSorry, you clearly can't follow instructions. Giving up!\n")
                exit()
            USER_INPUT_TRIES += 1

        USER_INPUT_TRIES = 0

        #If you pull a correct value, add 100 points. 
        if answer_dict[user_input-1][1]:
            HIGH_SCORE += 100
            print("\nCORRECT!\n")
        else:
            for solution in answer_dict:
                if solution[1]:
                    print("\nWRONG! The correct answer is: solution[0]\n")
                    break

        # Limit questions to 10
        if NUMBER_ANSWERED_QUEST < NUMBER_MAX_QUEST:
            NUMBER_ANSWERED_QUEST += 1
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
    if HIGH_SCORE > 0:
        print(f"\nYour final score is: {HIGH_SCORE} 🎉\n")
    else:
        print("\nYou really are not good at this game! 🤮\n")


if __name__ == '__main__':
    run_trivia()

