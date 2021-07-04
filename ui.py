THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz= quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = 0
        self.score_label = Label(bg=THEME_COLOR, highlightthickness=0, text="Score: 0",fg="white", font=("Arial", 15,"italic"))
        self.score_label.grid(column=1, row=0)

        self.question = Canvas(width=300, height=250)
        self.question_text = self.question.create_text(
            150,
            125,
            width=280,
            text="Test",
            font=("Arial",20,"italic"),
            fill=THEME_COLOR)
        self.question.grid(column=0,row=1, columnspan=2,pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(column=0,row=2)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=q_text)
            self.question.config(bg="white")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.question.itemconfig(self.question_text, text="You have answered for all questions there was :)")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        if is_right:
            self.score += 1




    def check_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        if is_right:
            self.score += 1



    def give_feedback(self,is_right):
        if is_right:
            self.question.config(bg="green")
        else:
            self.question.config(bg="red")
        self.window.after(1000, self.get_next_question)
