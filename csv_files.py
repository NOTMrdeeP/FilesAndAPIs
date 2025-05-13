import os
import csv

class StudentRecord:
    """A single student record"""
    def __init__(self, student_number, name, grade1, grade2, grade3):
        self.student_number = student_number
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def to_dict(self):
        return {
            "student_number": self.student_number,
            "name": self.name,
            "grade1": self.grade1,
            "grade2": self.grade2,
            "grade3": self.grade3
        }

class CSVFileHandler:
    """read/write student records into CSV"""
    def __init__(self, filename, fieldnames):
        self.filename = filename
        self.fieldnames = fieldnames

    def read_all(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', newline='') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except IOError as error:
            print(f"Error reading file: {error}")
            return[]

    def write_all(self, records):
        try:
            with open(self.filename, "w", newline='') as f:
                writer = csv.DictWriter(f, fieldnames = self.fieldnames)
                writer.writeheader()
                writer.writerows([r.to_dict() for r in records])
            print(f"Data written to {self.filename}")
        except IOError as error:
            print(f"Error writing to file: {error}")

    def append(self, record):
        file_exists = os.path.exists(self.filename)
        try:
            with open(self.filename, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames = self.fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(record.to_dict())
            print(f"Record added to {self.filename}")
        except IOError as error:
            print(f"Could not append to file: {error}")

class StudentManager:
    """Student record input, validation, display"""
    def __init__(self, handler):
        self.handler = handler

    def input_grade(self, label):
        while True:
            try:
                grade = int(input(f"Enter {label} (0-100):"))
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("Grade must be between 0 and 100")
            except ValueError:
                print("Please enter a valid number")

    def add_record(self):
        existing_records = self.handler.read_all()
        existing_ids = {r['student_number'] for r in existing_records}

        while True:
            student_number = input("Enter student number (9 digits):")
            if not student_number.isdigit() or len(student_number) != 9:
                print("Student number consists of 9 digits")
                continue

            if student_number in existing_ids:
                print("Student number already exists")
                continue
            break

        name = input("Enter Name: ")
        grade1 = self.input_grade("Grade 1")
        grade2 = self.input_grade("Grade 2")
        grade3 = self.input_grade("Grade 3")
        student = StudentRecord(student_number, name, grade1, grade2, grade3)
        self.handler.append(student)

    def calculate_letter_grade(self, average):
        if average >= 75:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "F"

    def calculate_pass_fail(self, average):
        if average >= 75:
            return "Pass with Distinction"
        elif average >= 50:
            return "Pass"
        else:
            return "Fail"

    def display_records(self):
        records = self.handler.read_all()
        if not records:
            print("No records found")
            return

        # Validate structure
        if not all(key in records[0] for key in self.handler.fieldnames):
            print("CSV file structure is incorrect or missing expected headers")
            return

        #Add average, letter, result to display
        display_fields = self.handler.fieldnames + ["average", "letter", "result"]
        col_widths = {key: len(key) for key in display_fields}

        for record in records:
            try:
                avg = round((int(record['grade1']) + int(record['grade2']) + int(record['grade3']))/3)
                record['average'] = f"{avg}"
                record['letter'] = self.calculate_letter_grade(avg)
                record['result'] = self.calculate_pass_fail(avg)
            except (ValueError, KeyError):
                record['average'] = "N/A"
                record['letter'] = "N/A"
                record['result'] = "N/A"

            for key in display_fields:
                col_widths[key] = max(col_widths[key], len(str(record.get(key, ""))))

        header = " | ".join(key.upper().ljust(col_widths[key]) for key in display_fields)

        seperator = "=+=".join("="*col_widths[key] for key in display_fields)

        print("\n========STUDENT RECORDS==========")
        print(header)
        print(seperator)
        for record in records:
            row = " | ".join(str(record.get(key, "")).ljust(col_widths[key]) for key in display_fields)
            print(row)

        print("=" * (sum(col_widths.values()) + 3 * (len(display_fields) - 1)))



