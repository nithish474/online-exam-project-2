def generate_report():
    students = [
        ("101", "Rahul", 85),
        ("102", "Priya", 92),
        ("103", "Arun", 78),
        ("104", "Sneha", 88),
        ("105", "Kiran", 95)
    ]

    total_students = len(students)
    total_marks = sum(s[2] for s in students)
    average_marks = total_marks / total_students

    with open("report.txt", "w") as f:
        f.write("ONLINE EXAMINATION SYSTEM REPORT\n")
        f.write("================================\n\n")

        f.write("Examination: Python Programming Test\n")
        f.write("Total Students: " + str(total_students) + "\n")
        f.write("Average Marks: " + str(round(average_marks, 2)) + "\n\n")

        f.write("STUDENT RESULTS\n")
        f.write("----------------\n")

        for student_id, name, marks in students:
            if marks >= 90:
                result = "Excellent"
            elif marks >= 75:
                result = "Pass"
            else:
                result = "Pass"

            f.write(
                "ID: " + student_id +
                " | Name: " + name +
                " | Marks: " + str(marks) +
                " | Result: " + result + "\n"
            )

        f.write("\nReport generated successfully by Jenkins.\n")

    print("Result report generated.")
    print("report.txt created successfully.")


if __name__ == "__main__":
    generate_report()