class Student:
    # [assignment] Skeleton class. Add your code here
    # (assignment)code added below
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    #Methods
    def change_name(self, name):
        self.name = name
        print(f"You have changed name to: {name}")
    def change_age(self, age):
        self.age = int(age)
        print(f"You have changed age to: {age}")
    def add_track(self, tracks):
        self.track = list(tracks)
        print(f"You have changed track to: {tracks}")
    def get_score(self):
        print(f"You score is: {self.score}")
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
