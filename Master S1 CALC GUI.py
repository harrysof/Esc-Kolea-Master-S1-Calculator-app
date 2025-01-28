import tkinter as tk

def calculate_semester_average():
    # Get grades from entry fields
    Inferential_Statistics_exam = float(entries_exam[0].get())
    Inferential_Statistics_TD = float(entries_TD[0].get())
    Financial_Accounting_exam = float(entries_exam[1].get())
    Financial_Accounting_TD = float(entries_TD[1].get())
    Management_exam = float(entries_exam[2].get())
    Management_TD = float(entries_TD[2].get())
    Marketing_exam = float(entries_exam[3].get())
    Marketing_TD = float(entries_TD[3].get())
    Macroeconomy_exam = float(entries_exam[4].get())
    Macroeconomy_TD = float(entries_TD[4].get())
    Computer_Science_exam = float(entries_exam[5].get())
    Computer_Science_TD = float(entries_TD[5].get())
    Law_exam = float(entries_exam[6].get())
    Law_TD = float(entries_TD[6].get())
    English_exam = float(entries_exam[7].get())
    English_TD = float(entries_TD[7].get())
    
    # Calculate averages
    Inferential_Statistics_average = (Inferential_Statistics_exam * 0.67) + (Inferential_Statistics_TD * 0.33)
    Financial_Accounting_average = (Financial_Accounting_exam * 0.67) + (Financial_Accounting_TD * 0.33)
    Management_average = (Management_exam * 0.67) + (Management_TD * 0.33)
    Marketing_average = (Marketing_exam * 0.67) + (Marketing_TD * 0.33)
    Macroeconomy_average = (Macroeconomy_exam * 0.67) + (Macroeconomy_TD * 0.33)
    Computer_Science_average = (Computer_Science_exam * 0.67) + (Computer_Science_TD * 0.33)
    Law_average = (Law_exam * 0.67) + (Law_TD * 0.33)
    English_average = (English_exam * 0.67) + (English_TD * 0.33)
    
    # Calculate total
    Total = (Inferential_Statistics_average * 4) + (Financial_Accounting_average * 4) + (Management_average * 4) + (Marketing_average * 4) + (Macroeconomy_average * 3.5) + (Computer_Science_average * 3.5) + (Law_average * 3.5) + (English_average * 3.5)
    Semester_average = Total / 30
    formatted_float = "{:.2f}".format(Semester_average)
    BetterTotal = "{:.2f}".format(Total)
    
    # Display result
    result_label.config(text=f"Total: {BetterTotal}\n1st Semester Average: {formatted_float}")

# Create GUI window
root = tk.Tk()
root.title("Semester Grade Calculator")

# Add headers for Exam and TD sections
exam_header = tk.Label(root, text="Exam")
exam_header.grid(row=0, column=1, padx=5, pady=5)
td_header = tk.Label(root, text="TD")
td_header.grid(row=0, column=2, padx=5, pady=5)

# Add labels and entry fields for each subject
subjects = [
    "Inferential Statistics", "Financial Accounting", "Management",
    "Marketing", "Macroeconomy", "Computer Science", "Law", "English"
]

labels = []
entries_exam = []
entries_TD = []

for i, subject in enumerate(subjects):
    label = tk.Label(root, text=subject)
    label.grid(row=i+1, column=0, padx=5, pady=5)
    
    entry_exam = tk.Entry(root)
    entry_exam.grid(row=i+1, column=1, padx=5, pady=5)
    entries_exam.append(entry_exam)
    
    entry_TD = tk.Entry(root)
    entry_TD.grid(row=i+1, column=2, padx=5, pady=5)
    entries_TD.append(entry_TD)

# Add button to trigger calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate_semester_average)
calculate_button.grid(row=len(subjects)+1, columnspan=3, padx=5, pady=10)

# Add label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=len(subjects)+2, columnspan=3, padx=5, pady=10)

root.mainloop()
