from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    qtext = question["text"]
    qanswer = question["answer"]
    new_Question = Question(qtext, qanswer)
    question_bank.append(new_Question)

quiz = QuizBrain(question_bank)
quiz.next_question()
