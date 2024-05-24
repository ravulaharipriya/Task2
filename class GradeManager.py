class GradeManager:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_count = sum([len(grades) for grades in self.grades.values()])
        if total_count == 0:
            return 0
        return total_grades / total_count

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

    def calculate_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_grades(self):
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

    def display_summary(self):
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.calculate_gpa(average)
        print("\n--- Grade Summary ---")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

def main():
    manager = GradeManager()
    while True:
        print("\n--- Grade Manager ---")
        print("1. Add Grade")
        print("2. Display Grades")
        print("3. Display Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            subject = input("Enter subject name: ")
            try:
                grade = float(input("Enter grade: "))
                if 0 <= grade <= 100:
                    manager.add_grade(subject, grade)
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
        elif choice == '2':
            manager.display_grades()
        elif choice == '3':
            manager.display_summary()
        elif choice == '4':
            print("Exiting Grade Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
