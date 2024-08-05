class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        for i in range(n):
            number = int(input(f"Please enter number {i+1}: "))
            self.numbers.append(number)

    def search_number(self, x):
        try:
            index = self.numbers.index(x) + 1
            return index
        except ValueError:
            return -1