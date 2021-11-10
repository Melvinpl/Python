from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    data_text = data["text"]
    data_answer = data["answer"]
    new_question = Question(data_text, data_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your Final score was : {quiz.score}/{quiz.question_number}")