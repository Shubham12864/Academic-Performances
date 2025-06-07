def calculate_average_performance(students):
    averages = {}
    for student in students:
        averages[student['name']] = sum(student['scores']) / len(student['scores'])
    return averages

def calculate_pass_rate(students, passing_score=40):
    pass_rate = {}
    for student in students:
        pass_count = sum(score >= passing_score for score in student['scores'])
        pass_rate[student['name']] = pass_count / len(student['scores']) * 100
    return pass_rate

def get_subject_wise_average(students):
    subject_totals = {}
    subject_counts = {}
    
    for student in students:
        for i, score in enumerate(student['scores']):
            subject = f'Subject {i + 1}'
            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0
            subject_totals[subject] += score
            subject_counts[subject] += 1
            
    subject_averages = {subject: total / count for subject, (total, count) in zip(subject_totals.keys(), zip(subject_totals.values(), subject_counts.values()))}
    return subject_averages

def get_top_performers(students, top_n=3):
    averages = calculate_average_performance(students)
    top_performers = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return top_performers