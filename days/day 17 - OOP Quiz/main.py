from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from api import datas
import html

question_bank = []

# for question in question_data:
#     input_text = question["text"]
#     input_answer = question["answer"]
#     question_bank.append(Question(input_text, input_answer))

for question in datas:
    input_text = html.unescape(question["question"])
    input_answer = question["correct_answer"]
    question_bank.append(Question(input_text, input_answer))


quiz = QuizBrain(question_bank)

while quiz.have_question:
    quiz.next_question()



