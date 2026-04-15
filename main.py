students = {
    "Ali": 85,
    "Vali": 92,
    "Gul": 88
}

best = max(students, key=students.get)
print("Eng yaxshi:", best, students[best])
