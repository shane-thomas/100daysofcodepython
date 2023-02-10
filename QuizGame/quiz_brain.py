class QuizBrain:
    def __init__(self, questions_list):
        self.qnumber = 0
        self.score = 0
        self.qlist = questions_list
    
    def still_has_questions(self):
        return self.qnumber < len(self.qlist)

    def next_question(self):
        current_question = self.qlist[self.qnumber]
        self.qnumber += 1
        user_answer = input(f"Q.{self.qnumber}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's not right.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.qnumber}")
        print("\n")
