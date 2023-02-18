
class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
    
    def next_question(self):
        question = self.question_list[self.question_number]
        text = question.text
        user_answer = input(f"Q{self.question_number + 1} : {text}, True/False : ").lower()
        self.check_answer(user_answer,question.answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
         
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("Sorry that's not correct")
        print(f'Your current score is {self.score}/{self.question_number + 1}')
        print(f"The correct answer is {correct_answer}")
        print("\n")
        
