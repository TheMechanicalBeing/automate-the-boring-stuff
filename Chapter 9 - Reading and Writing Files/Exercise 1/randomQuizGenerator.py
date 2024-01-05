import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    with open(f"quizzes/capitals_quiz{quizNum + 1}.txt", 'w') as quiz, \
         open(f"answers/capitals_quiz_answers{quizNum + 1}", "w") as ans:

        quiz.write("Name:\n\nDate:\n\nPeriod:\n\n")
        quiz.write(f"State Capitals Quiz {quizNum + 1}".rjust(25, " ") + "\n\n")

        states = list(capitals.keys())
        random.shuffle(states)

        for questionNum in range(50):
            correctAnswer = capitals[states[questionNum]]

            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)

            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            quiz.write(f"{questionNum+1}. What is capital of {states[questionNum]}?\n")

            for i in range(4):
                quiz.write(f"   {'ABCD'[i]}. {answerOptions[i]}\n")
            quiz.write('\n')

            ans.write(f"{questionNum+1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
