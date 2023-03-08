class FileReader:
    def __init__(self, filename):
        self.file = open(filename, newline='')
        self.line = self.file.readlines()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.line):
            self.file.close()
            raise StopIteration
        letter = self.line[self.index]
        self.index += 1
        return letter


for line in FileReader(r"C:\Users\k2lig\Downloads\lorem.txt"):
    print(line.strip())

