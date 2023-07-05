class Question:
    def __init__(self, text, difficulty, right_answer):
        self.text = text
        self.difficulty = difficulty
        self.right_answer = right_answer

        self.is_asked = False
        self.user_answer = None
        self.score = self.difficulty * 10

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.right_answer == self.user_answer

    def build_question(self):
        return f'Вопрос: {self.text} \n' \
               f'Сложность: {self.difficulty}/5'

    def build_feedback(self):
        if self.is_correct():
            return f'Ответ верный, получено {self.score} баллов'
        return f'Ответ неверный, верный ответ {self.right_answer}'
