class Student:
    def __init__(self, name, age, current_class=None):
        self.name = name
        self.age = age
        self.current_class = current_class
        self.test_scores = []

    def add_test_score(self, score):
        self.test_scores.append(score)

    def calculate_average_score(self):
        if len(self.test_scores) == 0:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

student1 = Student("Alice", 20, "Math Class")
student1.add_test_score(90)
student1.add_test_score(85)
student1.add_test_score(78)
average_score = student1.calculate_average_score()

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Owl(Bird):
    def speak(self):
        return f"{self.name} says 'Hoot hoot!'"

class Dodo(Bird):
    def speak(self):
        return f"{self.name} says 'Extinct!'"

bird1 = Owl("Hedwig")
bird2 = Dodo("Dodo")

print(f"{student1.name}'s average test score is {average_score}.")
print(bird1.speak())
print(bird2.speak())
