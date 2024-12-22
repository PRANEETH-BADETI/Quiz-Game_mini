from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

for question in question_data:
    options = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(options)
    question_bank.append(Question(question['question'],question['correct_answer'], options))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

score = quiz.score/quiz.question_number
print(f"Your Total Score: {quiz.score}/{quiz.question_number} \nPercentage: {score*100} ")
if score > 0.5:
    print("Congrats! You have passed the test")
else:
    print("You have failed the test\nScore above 50% to pass")