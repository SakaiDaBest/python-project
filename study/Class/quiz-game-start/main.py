from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]

for question in question_data:
    question_text=question['text']
    question_ans=question['answer']
    new_question = Question(question_text,question_ans)
    question_bank.append(new_question)

print(question_bank[0].answer)
something = True
qcount = len(question_bank)
count =1
cur = QuizBrain(question_bank)
while something:
    ans = cur.next_question()
    cur.answer(ans)
    count+=1
    if count == qcount:
        break
print(f'Your score is {cur.return_score()}')