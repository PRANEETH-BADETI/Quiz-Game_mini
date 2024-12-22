
class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank
    def next_question(self):
        curr_q = self.question_list[self.question_number]
        print(f"Q.{self.question_number+1}: {curr_q.text}")
        for idx, opt in enumerate(curr_q.options, start=1):
            print(f"{idx}. {opt}")
        ans = int(input("Choose the correct option (1/2/..: "))
        self.check_answer(curr_q.options[ans-1], curr_q.answer)
        self.question_number += 1

    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        print("Quiz Ended")
        return False

    def check_answer(self,ans,correct_ans):
        if ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("Oh! That's Wrong")
        print(f"The correct answer : {correct_ans}")
