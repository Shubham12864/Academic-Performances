import pandas as pd
from random import randint, choice, seed
import numpy as np

def generate_students_data(num_students=50):
    seed(42)  # For reproducibility
    
    # BCA subjects
    subjects = ['Mathematics', 'Computer Science', 'Statistics', 'Data Structures', 'Algorithms']
    
    # Realistic student names
    student_names = [
        'Ankit', 'Priya', 'Rahul', 'Sneha', 'Amit', 'Pooja', 'Vikash', 'Ritu',
        'Rohit', 'Kavya', 'Arjun', 'Nisha', 'Karan', 'Meera', 'Sanjay', 'Divya',
        'Abhishek', 'Shreya', 'Deepak', 'Anjali', 'Manish', 'Preeti', 'Suresh', 'Neha',
        'Aditya', 'Swati', 'Vishal', 'Kritika', 'Rajesh', 'Simran', 'Gaurav', 'Riya',
        'Harsh', 'Aarti', 'Nikhil', 'Tanya', 'Ashish', 'Varsha', 'Mohit', 'Jyoti',
        'Sachin', 'Pallavi', 'Vinay', 'Shweta', 'Akash', 'Sonia', 'Raghav', 'Megha',
        'Dhruv', 'Aditi', 'Ravi', 'Ananya', 'Tarun', 'Kirti', 'Manoj', 'Rashmi'
    ]
    
    students_data = []
    
    # Ensure we have enough names
    if num_students > len(student_names):
        for i in range(len(student_names), num_students):
            student_names.append(f'Student_{i+1}')
    
    for i in range(num_students):
        # Create more realistic score distributions
        # Some students are consistently good, some average, some struggling
        performance_type = choice(['excellent', 'good', 'average', 'below_average'])
        
        if performance_type == 'excellent':
            base_score = randint(85, 95)
            variance = randint(5, 10)  # Fixed: Always positive
        elif performance_type == 'good':
            base_score = randint(70, 85)
            variance = randint(5, 15)  # Fixed: Always positive
        elif performance_type == 'average':
            base_score = randint(60, 75)
            variance = randint(5, 15)  # Fixed: Always positive
        else:  # below_average
            base_score = randint(45, 65)
            variance = randint(5, 15)  # Fixed: Always positive
        
        scores = []
        for subject in subjects:
            # Fixed the randint range issue
            score = base_score + randint(-variance, variance)
            # Ensure score is within valid range
            score = max(0, min(100, score))
            scores.append(score)
        
        # Calculate additional metrics
        total_marks = sum(scores)
        percentage = round(total_marks / len(subjects), 2)
        
        # Determine grade based on percentage
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B+'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        else:
            grade = 'F'
        
        # Determine pass/fail status
        status = 'Pass' if all(score >= 35 for score in scores) and percentage >= 40 else 'Fail'
        
        student = {
            'student_id': f'BCA{2024:04d}{i+1:03d}',
            'name': student_names[i],
            'Mathematics': scores[0],
            'Computer Science': scores[1],
            'Statistics': scores[2],
            'Data Structures': scores[3],
            'Algorithms': scores[4],
            'total_marks': total_marks,
            'percentage': percentage,
            'grade': grade,
            'status': status,
            'semester': choice([1, 2, 3, 4, 5, 6]),
            'attendance': randint(65, 98)
        }
        
        students_data.append(student)
    
    return students_data

def get_dataframe(num_students=50):
    """Return student data as pandas DataFrame"""
    data = generate_students_data(num_students)
    return pd.DataFrame(data)

def get_subjects():
    """Return list of BCA subjects"""
    return ['Mathematics', 'Computer Science', 'Statistics', 'Data Structures', 'Algorithms']

def get_summary_stats(df):
    """Return summary statistics for the dataset"""
    subjects = get_subjects()
    
    stats = {
        'total_students': len(df),
        'pass_rate': round((df['status'] == 'Pass').sum() / len(df) * 100, 2),
        'average_percentage': round(df['percentage'].mean(), 2),
        'highest_scorer': df.loc[df['percentage'].idxmax(), 'name'],
        'lowest_scorer': df.loc[df['percentage'].idxmin(), 'name'],
        'subject_averages': {subject: round(df[subject].mean(), 2) for subject in subjects},
        'grade_distribution': df['grade'].value_counts().to_dict()
    }
    
    return stats

if __name__ == "__main__":
    # Generate and display sample data
    df = get_dataframe(30)
    print("Sample Student Data:")
    print(df.head(10))
    print("\nDataset Info:")
    print(df.info())
    print("\nSummary Statistics:")
    stats = get_summary_stats(df)
    for key, value in stats.items():
        print(f"{key}: {value}")