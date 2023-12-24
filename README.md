# pyFlash Cards

#### Made by [dewasheeshkumar](https://github.com/dewasheeshkumar)

#### Video Demo: https://youtu.be/THLG6MMt4WQ

#### Description:
Introducing pyFlash Cards, a command-line Python project that helps learning through interactive flashcards. Seamlessly enhance your knowledge with a user-friendly interface, enabling quick recall of facts, terms, and concepts. Create custom questionaire and effortlessly quiz yourself on any subject. With intuitive commands, this lightweight flashcard system makes learning engaging and efficient. Boost your memory retention and knowledge acquisition with pyFlash Cards tool for mastering new information effortlessly from the command line

#### Implementaion
Python's sqlite3 library is used to interact with the database of questions to add, delete questions from the database and to quiz yourself from added questions in the database

### Setup:
Intall various libraries required by:
> `pip install requirements.txt`

#### SQL queries used to create tables:
CREATE TABLE questions (id INTEGER NOT NULL, question TEXT NOT NULL, answer TEXT NOT NULL, PRIMARY KEY(id));

### Working

#### Try your Knowledge
What this option does is asks the user for the number of questions they wanna be quizzed from or from all the questions in the database the input can be a number here or a "all"

#### Add Questions
This option prompts the user for a question and then for an answer to that question which the user wants to add and then adds that question to the database this function runs in loop to make sure that user enters all questions needed in one go user can type "done" when prompted for question to exit the loop

#### Delete Question
This option prompt user for the id (Which user can get by checking id of questions from option 4 i.e. Show all QnA) of the question the user wants to delete then confirms the user in they sure (y/n) this option is in a loop to make sure that user deletes all question they want in one go rather than running program again and again they can just enter "done" when asking for id to exit the loop

#### Show all QnA
This option shows all the available questions in the database along with there answers and ids in format as given in example below

> `id: 69  Question: What's Radius of Earth in km rounded off to hundredth place Answer: 6400`
