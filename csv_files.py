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
