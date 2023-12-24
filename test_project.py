import sqlite3
from project import add_questions, delete_question, check_answer, calculate_score

connect = sqlite3.connect("test_database.db")
db = connect.cursor()

def test_delete_question():
    add_questions(db, connect, "delete", "deleting")
    x = db.execute("SELECT id FROM questions WHERE question = 'delete'").fetchall()
    for y in x:
        delete_question(db, connect, y[0])

    x = db.execute("SELECT question, answer FROM questions WHERE question = 'delete'").fetchone()
    assert x == None

def test_add_questions():
    add_questions(db, connect, "xz", "yz")
    x = db.execute("SELECT question, answer FROM questions WHERE answer = 'yz'").fetchone()
    question, answer = x
    assert question == "xz"
    assert answer == "yz"

    add_questions(db, connect, "What is CS50", "Best thing in education world")
    x = db.execute("SELECT question, answer FROM questions WHERE question = 'What is CS50'").fetchone()
    question, answer = x
    assert question == "What is CS50"
    assert answer == "Best thing in education world"

def test_check_answer():
    assert check_answer("London","london") == True
    assert check_answer("pie", "3.142") == False
    assert check_answer("98", "98") == True

def test_calculate_score():
    assert calculate_score((5, 10)) == 0.5
    assert calculate_score((2, 5)) == 0.4
    assert calculate_score((3, 6)) == 0.5
