student_name = "TONY STARK"
register_no = "AV_01"

total_questions = 10
correct_answers = 8
wrong_answers = 2

marks = correct_answers * 10

if marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

with open("result.txt", "w") as f:
    f.write("ONLINE EXAMINATION RESULT\n")
    f.write("=========================\n")
    f.write(f"Student Name: {student_name}\n")
    f.write(f"Register Number: {register_no}\n")
    f.write(f"Total Questions: {total_questions}\n")
    f.write(f"Correct Answers: {correct_answers}\n")
    f.write(f"Wrong Answers: {wrong_answers}\n")
    f.write(f"Marks: {marks}/100\n")
    f.write(f"Result: {result}\n")

print("Result report generated.")