import tkinter as tk
from tkinter import messagebox
import random

# Define a list of quiz questions and answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Bangalore", "Chennai"],
        "correct_answer": "New Delhi"
    },
    {
        "question": "Which river is known as the Ganges in India?",
        "options": ["Yamuna", "Brahmaputra", "Indus", "Ganges"],
        "correct_answer": "Ganges"
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Indira Gandhi"],
        "correct_answer": "Jawaharlal Nehru"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("India General Knowledge Quiz")

        self.score = 0
        self.current_question = None

        self.label = tk.Label(root, text="", padx=10, pady=10)
        self.label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            button.pack()
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if not questions:
            self.show_score()
            return

        self.current_question = random.choice(questions)
        self.display_question(self.current_question)
        questions.remove(self.current_question)

    def display_question(self, question_data):
        self.label.config(text=question_data["question"])
        options = question_data["options"]
        random.shuffle(options)
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def check_answer(self, index):
        if self.current_question["options"][index] == self.current_question["correct_answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Wrong", f"The correct answer is: {self.current_question['correct_answer']}")

        self.next_question()

    def show_score(self):
        self.label.config(text=f"Your score: {self.score}/{len(questions)}")
        for button in self.option_buttons:
            button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()