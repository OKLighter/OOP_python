class Mark:
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print("call next mark")
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        print("call getitem")
        return self.name[item]

    # def __iter__(self):
    #     print("call iter")
    #     return iter(self.name)

    # def __iter__(self):
    #     print("call iter")
    #     self.index = 0
    #     return self

    def __iter__(self):
        print("call iter")
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print("call next student")
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


mark = Mark([5, 4, 5, 4, 3])
actor = Student("kianu", "reevs", mark)
for i in actor:
    print(i)
