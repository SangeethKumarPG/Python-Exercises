from question_model import Question
from data import question_data,fetched_question
from quiz_brain import QuizBrain
question_bank = []

for item in fetched_question:
    question = item["text"]
    answer = item["answer"]
    q1 = Question(text= question, answer= answer)
    question_bank.append(q1)

brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.next_question()

print("You have completed the quiz")
print(f"Your score is {brain.score}/{brain.question_number + 1}")



