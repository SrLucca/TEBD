import tkinter as tk
from tkinter import simpledialog
import random

def ask_user_input(questions):
    number_range = list(range(0, len(questions), 3))
    random_number = random.choice(number_range)
    question_id, math_question, correct_answer = questions[random_number]


    user_input = simpledialog.askstring(f"Pergunta {question_id}", math_question)
    if user_input is not None:
        if user_input == correct_answer:
            return True
        return False
    else:
        return False
