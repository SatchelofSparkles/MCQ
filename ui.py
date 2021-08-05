from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
import random

THEME_COLOR = "#375362"

question_current = {
            "question": "question",
            "correct": "initial",
            "green": "green_val",
            "blue": "blue_val",
            "yellow": "yellow_val",
            "red": "red_val",
        }

# json serialiser and deserialiser, json libs

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.frame = Frame()

        self.score = Label(text=f"", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.correct_answer = "something"

        self.canvas = Canvas(width=500, height=300, bg="white")
        self.question_text = self.canvas.create_text(
            250,
            150,
            width=480,
            text="Question",
            font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)



        def choose_green():
            give_feedback("green")
            print("green")

        def choose_blue():
            give_feedback("blue")
            print("blue")

        def choose_yellow():
            give_feedback("yellow")
            print("yellow")

        def choose_red():
            give_feedback("red")
            print("red")

        def give_feedback(color):
            if color == self.correct_answer:
                self.canvas.itemconfig(self.question_text, text=f"You chose {color}. That's right, that is!")
                self.window.after(5000, self.get_next_question)
            else:
                self.canvas.itemconfig(self.question_text, text=f'You chose {color}. That was wrong. The correct answer was in the {question_current["correct"]} box')
                self.window.after(5000, self.get_next_question)

        self.button_a = Button(width=20, height=8, text="words", bg="pale green", command=choose_green)
        self.button_a.config(font=("Arial", 14, "italic"), wraplength = 200)
        self.button_a.grid(column=0, row=2, padx=5, pady=10)

        self.button_b = Button(width=20, height=8, text = "words", bg="light blue", command=choose_blue)
        self.button_b.config(font=("Arial", 14, "italic"), wraplength = 200)
        self.button_b.grid(column=1, row=2, padx=5, pady=10)

        self.button_c = Button(width=20, height=8, text = "words", bg="light goldenrod", command=choose_yellow)
        self.button_c.config(font=("Arial", 14, "italic"), wraplength = 200)
        self.button_c.grid(column=0, row=3, padx=5, pady=10)

        self.button_d = Button(width=20, height=8, text = "words", bg="light coral", command=choose_red)
        self.button_d.config(font=("Arial", 14, "italic"), wraplength = 200)
        self.button_d.grid(column=1, row=3, padx=5, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        value = random.randint(1, 25)
        question = question_data[value]["question"]
        colours = ["green", "blue", "yellow", "red"]
        random.shuffle(colours)
        correct = colours[0]
        answers = [question_data[value]["correct_answer"], question_data[value]["incorrect_answers"][0],
                   question_data[value]["incorrect_answers"][1], question_data[value]["incorrect_answers"][2]]
        question_current["question"] = question
        question_current["correct"] = correct

        for j in range(4):
            question_current[colours[j]] = answers[j]
        self.canvas.itemconfig(self.question_text, text = question_current["question"])
        self.button_a.config(text = question_current["green"])
        self.button_b.config(text = question_current["blue"])
        self.button_c.config(text = question_current["yellow"])
        self.button_d.config(text = question_current["red"])



        # else:
        #     self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
        #     self.button_a.config(state="disabled")
        #     self.button_b.config(state="disabled")
        #     self.button_c.config(state="disabled")
        #     self.button_d.config(state="disabled")
