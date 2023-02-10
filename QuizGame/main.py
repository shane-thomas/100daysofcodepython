from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    qtext = question["text"]
    qanswer = question["answer"]
    new_Question = Question(qtext, qanswer)
    question_bank.append(new_Question)
