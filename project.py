import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Quiz Application")
        self.master.geometry("400x300")
        self.master.config(bg="#f0f0f0")

        self.questions = [
            {
                "question": "Which of the following is not a valid Python data type?",
                "options": ["int", "bool", "str", "character"],
                "answer": "character"
            },
            {
                "question": "What will my_list = [1, 2, 3, 4, 5]; my_list.append(6) return?",
                "options": ["[1, 2, 3, 4, 5, 6]", "[1, 2, 3, 4, 5, [6]]", "[6]", "Error"],
                "answer": "[1, 2, 3, 4, 5, 6]"
            },
            {
                "question": "What will be printed by for i in range(3, 7): print(i)?",
                "options": ["3 4 5 6", "3 4 5", "3 4", "error"],
                "answer": "3 4 5 6"
            },
            {
                "question": "Which of the following is true about tuples in Python?",
                "options": ["Tuples are mutable", "Tuples can contain multiple data types",
                            "Tuples are defined using square brackets",
                            "Tuples cannot contain more than one element"],
                "answer": "Tuples can contain multiple data types"
            },
            {
                "question": "Which mode is used to open a file for reading?",
                "options": ["w", "r", "a", "rb"],
                "answer": "r"
            },
            {
                "question": "What is the output of print(type([]))?",
                "options": ["list", "dict", "tuple", "set"],
                "answer": "list"
            },
            {
                "question": "Which of the following is used to define a function in Python?",
                "options": ["def", "function", "fun", "define"],
                "answer": "def"
            },
            {
                "question": "What will be the output of print(2 ** 3)?",
                "options": ["6", "8", "9", "3"],
                "answer": "8"
            }
        ]
        
        self.score = 0
        self.question_index = 0
        
        self.question_label = tk.Label(master, text="", wraplength=300, bg="#f0f0f0", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []
        
        for i in range(4):
            option = tk.Radiobutton(master, text="", variable=self.var, value="", bg="#f0f0f0", font=("Arial", 12), selectcolor="#ffcc00")
            option.pack(anchor='w', padx=20)
            self.options.append(option)
        
        self.next_button = tk.Button(master, text="Next", command=self.next_question, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.next_button.pack(pady=10)

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_application, bg="#f44336", fg="white", font=("Arial", 12))
        self.exit_button.pack(pady=10)

        self.display_question()
    
    def display_question(self):
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]
            self.question_label.config(text=question["question"])
            self.var.set(None)  # Reset the selected option
            
            for i, option in enumerate(self.options):
                option.config(text=question["options"][i], value=question["options"][i])
        else:
            self.show_score()
    
    def check_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.question_index]["answer"]
        if selected_answer == correct_answer:
            self.score += 1
    
    def next_question(self):
        self.check_answer()  # Check the answer before moving to the next question
        self.question_index += 1
        self.display_question()
    
    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your total score is: {self.score}/{len(self.questions)}")
        self.master.quit()

    def exit_application(self):
        # Close the application immediately
        self.master.destroy()  # Use destroy to close the application

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()
