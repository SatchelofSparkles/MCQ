from data import question_data
import random
from quiz_brain import QuizBrain
from ui import QuizInterface
import json

THEME_COLOR = "#375362"

question_bank = {

}


def produce_question_set(quantity):
    available_questions = [n for n in range(0, len(question_data))]
    random.shuffle(available_questions)

    while len(available_questions) > quantity:
        available_questions.pop(quantity)
    print(available_questions)
    with open("question_set.json", "w", encoding="utf-8") as question_set:
        question_set.write("")
    for q in range(0, quantity):
        question_number = available_questions[q]
        question = question_data[question_number]["question"]
        colours = ["green", "blue", "yellow", "red"]
        random.shuffle(colours)
        correct = colours[0]
        answers = [question_data[q]["correct_answer"], question_data[q]["incorrect_answers"][0], question_data[q]["incorrect_answers"][1], question_data[q]["incorrect_answers"][2]]
        with open("question_set.json", "a", encoding="utf-8") as question_set:
            num = str(q+1)
            next_question = {
                "question": question,
                "correct": correct,
                colours[0]: answers[0],
                colours[1]: answers[1],
                colours[2]: answers[2],
                colours[3]: answers[3],
            }
            json.dump(next_question, question_set, ensure_ascii=False, indent=4)


produce_question_set(10)

quiz = QuizBrain(question_bank)
q = QuizInterface(quiz)
