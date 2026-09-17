def generate_report():
    correct_answers = 8
    wrong_answers = 2
    total_questions = correct_answers + wrong_answers

    score = (correct_answers / total_questions) * 100

    with open("report.txt", "w") as f:
        f.write("ONLINE EXAMINATION SYSTEM REPORT\n")
        f.write("================================\n\n")
        f.write("Total Questions: " + str(total_questions) + "\n")
        f.write("Correct Answers: " + str(correct_answers) + "\n")
        f.write("Wrong Answers: " + str(wrong_answers) + "\n")
        f.write("Score: " + str(int(score)) + "/100\n")

    print("Result report generated.")
    print("Score:", int(score), "/100")


if __name__ == "__main__":
    generate_report()