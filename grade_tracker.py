import tkinter as tk
from tkinter import messagebox

#manages the students grades
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}
        
    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]
    
    def calculate_average(self):
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count != 0 else 0
    
    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    def display_grades(self):
        grades_info = f"Grades for {self.name}:\n"
        for subject, grades in self.grades.items():
            grades_info += f"  {subject}: {grades}\n"
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        grades_info += f"\nAverage Grade: {average:.2f}\n"
        grades_info += f"Letter Grade: {letter_grade}\n"
        return grades_info
    
#creates the GUI using the tkinter
class GradeTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Tracker")
        
        self.student = None
        
        self.name_label = tk.Label(root, text="Student's Name:")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack()
        
        self.subject_label = tk.Label(root, text="Subject:")
        self.subject_label.pack()
        
        self.subject_entry = tk.Entry(root)
        self.subject_entry.pack()
        
        self.grade_label = tk.Label(root, text="Grade:")
        self.grade_label.pack()
        
        self.grade_entry = tk.Entry(root)
        self.grade_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Grade", command=self.add_grade)
        self.add_button.pack()
        
        self.display_button = tk.Button(root, text="Display Grades", command=self.display_grades)
        self.display_button.pack()
        
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack()
        
    def start(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showwarning("Input Error", "Please enter the student's name.")
            return
        self.student = Student(name)
        messagebox.showinfo("Student Created", f"Student {name} created successfully.")
        
#adds grade for a subject       
    def add_grade(self):
        if self.student is None:
            messagebox.showwarning("Error", "Please start by entering the student's name.")
            return
        
        subject = self.subject_entry.get()
        grade = self.grade_entry.get()
        
        if not subject or not grade:
            messagebox.showwarning("Input Error", "Please enter both subject and grade.")
            return
        
        try:
            grade = float(grade)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid grade.")
            return
        
        self.student.add_grade(subject, grade)
        messagebox.showinfo("Grade Added", f"Grade {grade} for {subject} added successfully.")
        
#displays the students grades in the text field      
    def display_grades(self):
        if self.student is None:
            messagebox.showwarning("Error", "Please start by entering the student's name.")
            return
        
        grades_info = self.student.display_grades()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, grades_info)
        
#initializes and runs the tkinter main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = GradeTrackerApp(root)
    root.mainloop()
