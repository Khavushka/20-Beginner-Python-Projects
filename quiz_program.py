# a dictionary that stores questions and answers for
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# show the final result when quiz is completed

score = 0

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Danmark?",
        "answer": "Kopenhagen"
    },
    "question3": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    }
}

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score + 1
        print("Your score is " + str(score))
    else:
        print('You lose')
        print("Your score " + str(score))

print("You got " + str(score) + " out of 3 questions correctly")
print("Your percentage is " + str(score/7 * 100) + "%")