# Configuration settings for the student performance analysis application

# Constants for subjects
SUBJECTS = ["Mathematics", "Computer Science", "Statistics", "Data Structures", "Database Management"]

# Number of students to generate
NUM_STUDENTS = 100

# Random seed for reproducibility
RANDOM_SEED = 42

# Grading scale
GRADE_SCALE = {
    "A": (90, 100),
    "B": (80, 89),
    "C": (70, 79),
    "D": (60, 69),
    "F": (0, 59)
}

# Pass mark
PASS_MARK = 40

# File paths for data storage
DATA_FILE_PATH = "src/data/students_data.py"