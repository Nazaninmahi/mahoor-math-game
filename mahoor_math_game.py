import tkinter as tk
import random

# Variable values for Mahoor's name
variables = {
    'm': 5,
    'a': 2,
    'h': 6,
    'o': 9,
    'r': 3
}

# Messages
correct_messages = [
    "Great job!",
    "Bravo! You did it!",
    "You're amazing!",
    "Yay! Correct!",
    "Keep it up!"
]

wrong_messages = [
    "Oops! Try again!",
    "Not quite! You can do it!",
    "Don't give up!",
    "Almost there!",
    "Keep trying!"
]

# Game state
score = 0
stars = 0

def generate_question():
    global current_answer

    x = random.choice(list(variables.keys()) + list(range(0, 21)))
    y = random.choice(list(variables.keys()) + list(range(0, 21)))
    op = random.choice(["+", "-", "*"])

    def resolve(val):
        return variables[val] if isinstance(val, str) else val

    val_x = resolve(x)
    val_y = resolve(y)

    if op == "+":
        current_answer = val_x + val_y
    elif op == "-":
        current_answer = val_x - val_y
    else:
        current_answer = val_x * val_y

    question = f"{x} {op} {y}"
    question_label.config(text=question)
    entry.delete(0, tk.END)

def check_answer():
    global score, stars

    try:
        user_answer = int(entry.get())
        if user_answer == current_answer:
            score += 1
            message = random.choice(correct_messages)
            feedback_label.config(text=message, fg="green")
        else:
            message = random.choice(wrong_messages)
            feedback_label.config(text=message, fg="red")
            return

        if score % 5 == 0:
            stars += 1
            star_label.config(text=f"⭐ x {stars}")
            if stars == 15:
                question_label.config(text="🎉 You win! 🎉")
                feedback_label.config(text="So many stars! You're a math star! 🌟", fg="purple")
                return

        generate_question()

    except ValueError:
        feedback_label.config(text="Please enter a number!", fg="orange")

# GUI setup
window = tk.Tk()
window.title("Mahoor's Math Game")
window.geometry("400x300")
window.config(bg="lightyellow")

title = tk.Label(window, text="💖 Mahoor's Math Game 💖", font=("Helvetica", 16, "bold"), bg="lightyellow")
title.pack(pady=10)

question_label = tk.Label(window, text="", font=("Helvetica", 20), bg="lightyellow")
question_label.pack(pady=20)

entry = tk.Entry(window, font=("Helvetica", 16), justify="center")
entry.pack()

submit_button = tk.Button(window, text="Submit", font=("Helvetica", 14), command=check_answer)
submit_button.pack(pady=10)

feedback_label = tk.Label(window, text="", font=("Helvetica", 12), bg="lightyellow")
feedback_label.pack(pady=10)

star_label = tk.Label(window, text="⭐ x 0", font=("Helvetica", 14), bg="lightyellow")
star_label.pack()

generate_question()
window.mainloop()
