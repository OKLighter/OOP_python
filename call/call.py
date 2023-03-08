class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print("init object", self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)

        print(f"Наш экземпляр вызывался {self.counter} раз")


s = Counter()
s()  # Наш экземпляр вызывался 1 раз
s(2, 3, 4, 5, 6, 7)  # Наш экземпляр вызывался 2 раз
print(s.summa)
print(s.length)
print(s.counter)
s(3, 4, 5)
print(s.summa)
