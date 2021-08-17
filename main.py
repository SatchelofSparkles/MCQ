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
    question_number_1 = available_questions[0]
    q_1 = question_data[question_number_1]["question"]
    colours = ["green", "blue", "yellow", "red"]
    random.shuffle(colours)
    correct = colours[0]
    answers = [question_data[question_number_1]["correct_answer"], question_data[question_number_1]["incorrect_answers"][0],
               question_data[question_number_1]["incorrect_answers"][1], question_data[question_number_1]["incorrect_answers"][2]]
    green_response = answers[colours.index("green")]
    blue_response = answers[colours.index("blue")]
    yellow_response = answers[colours.index("yellow")]
    red_response = answers[colours.index("red")]
    new_data = {"Q1":
        {
            "question": q_1,
            "correct": correct,
            "green": green_response,
            "blue": blue_response,
            "yellow": yellow_response,
            "red": red_response
        }}
    with open("question_set.json", "w") as question_set:
        json.dump(new_data, question_set, indent=4)

    for q in range(1, quantity):
        question_number = available_questions[q]
        numbering = q + 1
        tag = f"Q{numbering}"
        question = question_data[question_number]["question"]
        colours = ["green", "blue", "yellow", "red"]
        random.shuffle(colours)
        correct = colours[0]
        answers = [question_data[question_number]["correct_answer"], question_data[question_number]["incorrect_answers"][0],
                   question_data[question_number]["incorrect_answers"][1], question_data[question_number]["incorrect_answers"][2]]
        with open("question_set.json", "r") as data_file:
            next_question = {tag:
                {
                    "question": question,
                    "correct": correct,
                    colours[0]: answers[0],
                    colours[1]: answers[1],
                    colours[2]: answers[2],
                    colours[3]: answers[3],
                }}
            data_current = json.load(data_file)
            data_current.update(next_question)
        with open("question_set.json", "w") as data_file:
            json.dump(data_current, data_file, indent=4)


    #         json.dump(next_question, question_set, ensure_ascii=False, indent=4)
    #         question_set.write(",")
    # question_number = available_questions[quantity - 1]
    # question = question_data[question_number]["question"]
    # colours = ["green", "blue", "yellow", "red"]
    # random.shuffle(colours)
    # correct = colours[0]
    # answers = [question_data[quantity - 1]["correct_answer"], question_data[quantity - 1]["incorrect_answers"][0],
    #            question_data[quantity - 1]["incorrect_answers"][1], question_data[quantity - 1]["incorrect_answers"][2]]
    # with open("question_set.json", "a", encoding="utf-8") as question_set:
    #     next_question = {
    #         "question": question,
    #         "correct": correct,
    #         colours[0]: answers[0],
    #         colours[1]: answers[1],
    #         colours[2]: answers[2],
    #         colours[3]: answers[3],
    #     }
    #     json.dump(next_question, question_set, ensure_ascii=False, indent=4)
    #     question_set.write("]")


produce_question_set(10)

quiz = QuizBrain(question_bank)
q = QuizInterface(quiz)
