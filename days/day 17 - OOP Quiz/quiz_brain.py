class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct_answers = 0
        self.have_question = True


    def check_answer(self, answer, current_question):
        cleaned_answer = answer
        main_answer = current_question.lower()
        if (cleaned_answer == main_answer):
            self.correct_answers += 1
            print("your answer is correct")
        else:
            print("your answer is wrong")

        print(f"you have correct of {self.correct_answers} out of {self.question_number}.")
        print("\n")


        if self.question_number == len(self.question_list):
            print("we have finished, thank you")
            self.have_question = False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower().strip()
            if answer == "false" or answer == "true":
                self.check_answer(answer, current_question.answer)
                break
            else:
                print("Please provide true or false as answer")
