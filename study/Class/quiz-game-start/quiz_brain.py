class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score=0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        return str(input(f'{self.question_number}: {current_question.text}(True/False)\n'))

    def answer(self, ans):
        current_question = self.question_list[self.question_number]
        if current_question.answer == ans:
            print("\nCORRECT\n")
            self.score+=1
        else:
            print(f"\nYOU WRONG\n")
        self.question_number+=1
    def return_score(self):
        return self.score
