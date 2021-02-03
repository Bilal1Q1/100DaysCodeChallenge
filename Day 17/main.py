from quiz_data import question_data
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1 
        user_choice = input(f"Q.{self.question_number}: {current_question.text} (Ture/False): ")
        self.correct_question(user_choice, current_question.answer)
    
    def is_still_question(self):
        return self.question_number < len(self.question_list)

    def correct_question(self, user_choice, correct_answer):
        if user_choice.lower() == correct_answer.lower() :
            self.score += 1
            print('Correct Answer ✅')
        else:
            print('Wrong Answer ❌')
        print(f"the correct Answer was {correct_answer}.")
        print(f"Your current Score is {self.score}/{self.question_number}\n")


question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.is_still_question():
    quiz.next_question()


print('Quiz has been finished 🎉✨')
print(f"Your final score is {quiz.score}/{quiz.question_number}")