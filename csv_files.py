import os
import csv
from calendar import error

from urllib3.filepost import writer


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

class CSVFileHander:
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


