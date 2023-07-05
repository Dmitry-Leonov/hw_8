import json

from question import Question


def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for item in data:
        text = item['q']
        difficulty = int(item['d'])
        right_answer = item['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions


def build_statistics(questions):
    score = 0
    count = 0

    for question in questions:
        if question.is_correct():
            score += question.score
            count += 1
    return f'Вот и все!\n' \
           f'Отвечено {count} вопросов из 10 \n' \
           f'Набрано баллов: {score}'