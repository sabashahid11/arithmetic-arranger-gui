# GUI bananey ke liye tkinter library import kia, tk naam se use  kia
import tkinter as tk
# Message boxes dikhane ke liye messagebox module import kia
from tkinter import messagebox

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid format."

        first, operator, second = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2

        first_line.append(first.rjust(width))
        second_line.append(operator + ' ' + second.rjust(width - 2))
        dashes.append('-' * width)

        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))

    arranged_problems = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes)
    )

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems


# GUI App 

def arrange_and_display():
    raw_input = input_entry.get("1.0", tk.END).strip()
    problems = [p.strip() for p in raw_input.split(',')]
    show_ans = show_var.get()

    result = arithmetic_arranger(problems, show_ans)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


# Window setup
window = tk.Tk()
window.title("Arithmetic Arranger")
window.geometry("500x400")

# Widgets
input_label = tk.Label(window, text="Enter problems (comma-separated):")
input_label.pack(pady=5)

input_entry = tk.Text(window, height=3, width=60)
input_entry.pack(pady=5)

show_var = tk.BooleanVar()
show_checkbox = tk.Checkbutton(window, text="Show answers", variable=show_var)
show_checkbox.pack()

arrange_button = tk.Button(window, text="Arrange Problems", command=arrange_and_display)
arrange_button.pack(pady=10)

output_label = tk.Label(window, text="Output:")
output_label.pack(pady=5)

output_text = tk.Text(window, height=10, width=60)
output_text.pack()

# Run app
window.mainloop()