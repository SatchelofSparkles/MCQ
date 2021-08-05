import random


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # def next_question(self):
    #     current_question = self.question_list[self.question_number]
    #     self.question_number += 1
    #     self.check_answer(current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"That's correct! Your current score is {self.score}")
        else:
            print(f"That's wrong. Your current score is {self.score}")
