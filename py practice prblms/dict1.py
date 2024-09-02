def analyze_employee_data(employees):
    result = {}

    for i,j in employees.items():
        if j['department']

    return result

# Example usage:
employees = {
    1001: {"name": "John Smith", "department": "Sales", "salary": 50000},
    1002: {"name": "Jane Doe", "department": "Marketing", "salary": 60000},
    1003: {"name": "Bob Johnson", "department": "Engineering", "salary": 75000},
    1004: {"name": "Alice Brown", "department": "Sales", "salary": 55000},
    1005: {"name": "Charlie Davis", "department": "Engineering", "salary": 70000},
    1006: {"name": "Emma Wilson", "department": "Marketing", "salary": 65000}
}

# Test the function
analysis_result = analyze_employee_data(employees)
print(analysis_result)













# Write a Python function that takes this library dictionary and returns a list of all books (across all genres) that have more than 
# a specified number of copies.The function should:

# Take two parameters: the library dictionary and the minimum number of copies.
# Return a list of tuples, where each tuple contains the book title and its genre.
# Sort the result alphabetically by book title.

def books_with_min_copies(library, min_copies):
    result = []

    for genre, books in library.items():
        for title, book_info in books.items():
            if book_info['copies'] >= min_copies:
                result.append((title, genre))

    return sorted(result)  # Sort alphabetically by book title


# Example usage:
library = {
    'Fiction': {
        'The Great Gatsby': {'author': 'F. Scott Fitzgerald', 'copies': 5},
        '1984': {'author': 'George Orwell', 'copies': 3},
        'To Kill a Mockingbird': {'author': 'Harper Lee', 'copies': 4}
    },
    'Non-Fiction': {
        'A Brief History of Time': {'author': 'Stephen Hawking', 'copies': 2},
        'The Immortal Life of Henrietta Lacks': {'author': 'Rebecca Skloot', 'copies': 3},
        'Sapiens': {'author': 'Yuval Noah Harari', 'copies': 4}
    },
    'Mystery': {
        'The Da Vinci Code': {'author': 'Dan Brown', 'copies': 3},
        'Gone Girl': {'author': 'Gillian Flynn', 'copies': 2}
    }
}

# Test the function
result = books_with_min_copies(library, 3)
print(result)









# Write a Python function that takes this dictionary and a subject name as input, and returns the name of the student with the highest 
# score in that subject.
# For example, if the function is called with 'Science' as the subject, it should return 'Alice' since she has the highest Science score.


# def highest_score_student(scores, subject):
#     highest_score = 0
#     top_student = ''
    
#     for i, j in scores.items():
#         #print(j.keys())
#         if subject in j.keys():
#             if j[subject] > highest_score:
#                 highest_score = j[subject]
#                 top_student = i
    
#     return top_student

# # Test the function
# student_scores = {
#     'Alice': {'Math': 85, 'Science': 90, 'History': 78},
#     'Bob': {'Math': 92, 'Science': 88, 'History': 95},
#     'Charlie': {'Math': 78, 'Science': 85, 'History': 80}
# }

# result = highest_score_student(student_scores, "Science")
# print(result)  # This should print 'Alice'