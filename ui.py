from tkinter import *
from quiz_brain import QuizBrain
import random
import json

THEME_COLOR = "#375362"


# json serialiser and deserialiser, json libs

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.frame = Frame()

        self.value = 1

        self.current_score = 0

        self.score = Label(text=f"Score: {self.current_score}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.correct_answer = "something"

        with open("question_set.json", "r") as questions:
            self.questions_for_use = json.load(questions)

        self.number_of_questions = list(self.questions_for_use.keys())
        self.final_key = str(self.number_of_questions[-1]).split("Q")
        self.final_question = int(self.final_key[1])


        self.canvas = Canvas(width=500, height=300, bg="white")

        self.question_num = f"Q{self.value}"

        self.question_text = self.canvas.create_text(
            250,
            150,
            width=480,
            text="_",
            font=("Arial", 18, "italic"))
        self.canvas.itemconfig(self.question_text, text=self.questions_for_use[self.question_num]["question"])
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        # self.question_text = self.canvas.create_text(
        #     250,
        #     150,
        #     width=480,
        #     text=self.questions_for_use[self.question_num]["question"],
        #     font=("Arial", 18, "italic"))

        def choose_green():
            give_feedback("green")

        def choose_blue():
            give_feedback("blue")

        def choose_yellow():
            give_feedback("yellow")

        def choose_red():
            give_feedback("red")

        def give_feedback(color):
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"")
            with open("question_set.json", "r") as questions:
                answers = json.load(questions)
                n = f"Q{self.value}"
                if color == answers[n]["correct"]:
                    self.current_score += 1
                    self.canvas.itemconfig(self.question_text, text=f"You chose {color}. That's right, that is!")
                    self.Scorecard = f"Score: {self.current_score} / {self.value}"
                    self.score.config(text=self.Scorecard)
                else:
                    self.canvas.itemconfig(self.question_text,
                                           text=f'You chose {color}. That was wrong. The correct answer was in the {self.questions_for_use[n]["correct"]} box')
                    self.Scorecard = f"Score: {self.current_score} / {self.value}"
                    self.score.config(text=self.Scorecard)
                self.window.after(5000, self.get_next_question)

        self.button_a = Button(width=20, height=8, text=self.questions_for_use[self.question_num]["green"], bg="pale green", command=choose_green)
        self.button_a.config(font=("Arial", 14, "italic"), wraplength=200)
        self.button_a.grid(column=0, row=2, padx=5, pady=10)

        self.button_b = Button(width=20, height=8, text=self.questions_for_use[self.question_num]["blue"], bg="light blue", command=choose_blue)
        self.button_b.config(font=("Arial", 14, "italic"), wraplength=200)
        self.button_b.grid(column=1, row=2, padx=5, pady=10)

        self.button_c = Button(width=20, height=8, text=self.questions_for_use[self.question_num]["yellow"], bg="light goldenrod", command=choose_yellow)
        self.button_c.config(font=("Arial", 14, "italic"), wraplength=200)
        self.button_c.grid(column=0, row=3, padx=5, pady=10)

        self.button_d = Button(width=20, height=8, text=self.questions_for_use[self.question_num]["red"], bg="light coral", command=choose_red)
        self.button_d.config(font=("Arial", 14, "italic"), wraplength=200)
        self.button_d.grid(column=1, row=3, padx=5, pady=10)


        # self.question_text = self.canvas.create_text(
        #     250,
        #     150,
        #     width=480,
        #     text=self.questions_for_use[self.question_num]["question"],
        #     font=("Arial", 18, "italic"))

        self.window.mainloop()

    def get_next_question(self):
        self.value = self.value + 1
        if self.value <= self.final_question:
            n = f"Q{self.value}"
            self.score.config(bg=THEME_COLOR)
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=self.questions_for_use[n]["question"])
            self.button_a.config(bg="pale green")
            self.button_a.config(text=self.questions_for_use[n]["green"])
            self.button_b.config(bg="light blue")
            self.button_b.config(text=self.questions_for_use[n]["blue"])
            self.button_c.config(bg="light goldenrod")
            self.button_c.config(text=self.questions_for_use[n]["yellow"])
            self.button_d.config(bg="light coral")
            self.button_d.config(text=self.questions_for_use[n]["red"])
        else:
            self.canvas.itemconfig(self.question_text, text=[f"Quiztime over, good game!"])

#        self.canvas.itemconfig(self.question_text, text=question_data[self.value]["question"])
#        self.button_a.config(text = question_data[self.value]["green"])
#        self.button_b.config(text = question_data[self.value]["blue"])
#        self.button_c.config(text = question_data[self.value]["yellow"])
#        self.button_d.config(text = question_data[self.value]["red"])


# else:
#     self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
#     self.button_a.config(state="disabled")
#     self.button_b.config(state="disabled")
#     self.button_c.config(state="disabled")
#     self.button_d.config(state="disabled")
