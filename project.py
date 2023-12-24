# importing requisite libraries

import sqlite3


def main():
    # Displaying the menu
    option = input(
        "1. Try your Knowledge\n2. Add Questions\n3. Delete Question\n4. Show all QnA\ninput: "
    )

    if option == "1":
        marks = answer_questions(db)
        score = calculate_score(marks)
        print(f"Your Score : {score * 100:.2f} %")

    elif option == "2":
        while True:
            question = input("Question: ")

            if "done" in question.lower():
                break
            else:
                answer = input("Answer: ")
                add_questions(db, connect, question, answer)

    elif option == "3":
        while True:
            id = input("What is the id of the question you wanna delete? ")
            if "done" in id:
                break
            else:
                confirmation = input("You sure you wanna delete that question? (y/n) ")
                if "y" in confirmation:
                    delete_question(db, connect, id)
                else:
                    print("Delete Operation Stopped!")
                    break

    elif option == "4":
        show_questions(db)


# option for revising the questions or answering
def answer_questions(db):
    n = db.execute("SELECT COUNT(id) FROM questions")
    n = int(n.fetchone()[0])

    a = input("Number of questions? (number/all) ")

    try:
        number_of_questions = n if a == "all" else int(a)
    except:
        print("Enter a Valid number")

    qna = db.execute(
        f"SELECT * FROM questions ORDER BY RANDOM() LIMIT {number_of_questions}"
    ).fetchall()
    score = 0
    for question in qna:
        answer = input(f"{question[1]} ? ")
        if check_answer(question[2], answer):
            score += 1
            print("Correct!")
        else:
            print("Incorrect")
    return score, number_of_questions


# Function to add questions to the database as flash cards
def add_questions(db, connect, question, answer):
    try:
        db.execute(
            "INSERT INTO questions(question, answer) VALUES(?, ?)", (question, answer)
        )
        connect.commit()
        print("done!")
    except:
        print("Error")


# Function to delete any question in database
def delete_question(db, connect, id):
    try:
        db.execute(f"DELETE FROM questions WHERE id = {id}")
        connect.commit()
        print("Deleted Successfully")
    except:
        print("Error while deletion check your id")


# Function to show all the questions in database
def show_questions(db):
    questions = db.execute(f"SELECT * FROM questions").fetchall()
    for question in questions:
        print(f"id : {question[0]} Question : {question[1]} Answer : {question[2]}")


# Function to check if answer is right
def check_answer(question, answer):
    if question.lower() == answer.lower():
        return True
    else:
        return False


# Fucntion to calculate score
def calculate_score(marks):
    return float(marks[0] / marks[1])


if __name__ == "__main__":
    print("Flash Cards!!")
    try:
        # connecting to the database
        connect = sqlite3.connect("database.db")
        print("Connected to database Successfully!!")
    except:
        print("Connection to database Failed..")

    # making a variable for cursor
    db = connect.cursor()
    main()
