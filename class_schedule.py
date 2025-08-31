print("="*50)
print("   BirdyPhillips School of Science and Technology   ")
print("="*50)
print("Welcome to BirdyPhillips School Class Schedule!")
print("Find your classroom, instructor, and meeting time below.")

# Dictionaries for course info
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "Mon 8:00 a.m.",
    "CSC102": "Tue 9:00 a.m.",
    "CSC103": "Wed 10:00 a.m.",
    "NET110": "Thu 11:00 a.m.",
    "COM241": "Fri 1:00 p.m."
}

room_names = {
    "CSC101": "Intro to computing",
    "CSC102": "Advanced Programming",
    "CSC103": "AI and Machine Learning",
    "NET110": "Information System Networks",
    "COM241": "Business Communication"
}

print("Available courses:")
for course in room_numbers:
    print(f"  {course}: {room_names[course]}")

# User input loop
while True:
    course = input("Enter a course number (e.g., CSC101) or type 'quit' to exit: ").strip().upper()
    if course == 'QUIT':
        print("Goodbye!")
        print("="*50)
        print("Thank you for using BirdyPhillips School Class Schedule!")
        print("May your studies be exciting and your code bug-free!")
        print("="*50)
        break
    if course in room_numbers:
        print(f"Course: {course}")
        print(f"Course Name: {room_names[course]}")
        print(f"Room Number: {room_numbers[course]}")
        print(f"Instructor: {instructors[course]}")
        print(f"Meeting Time: {meeting_times[course]}")
    else:
        print("Course not found.")
