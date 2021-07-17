class Person:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern
        self.index = 0
        self.numberOfCorrectAnswers = 0

    def checkAnswer(self, correctAnswer):
        answer = self.pattern[self.index]
        if answer == correctAnswer:
            self.numberOfCorrectAnswers += 1

        self.index = (self.index + 1) % len(self.pattern)


adrian = Person("Adrian", ["A", "B", "C"])
bruno = Person("Bruno", ["B", "A", "B", "C"])
goran = Person("Goran", ["C", "C", "A", "A", "B", "B"])
persons = [adrian, bruno, goran]

numberOfQuestions = int(input())
answers = list(input())
for answer in answers:
    for person in persons:
        person.checkAnswer(answer)

winners = []
mostCorrectAnswers = 0
for person in persons:
    if mostCorrectAnswers < person.numberOfCorrectAnswers:
        winners = [person]
        mostCorrectAnswers = person.numberOfCorrectAnswers
    elif mostCorrectAnswers == person.numberOfCorrectAnswers:
        winners.append(person)

print(winners[0].numberOfCorrectAnswers)
for winner in winners:
    print(winner.name)
