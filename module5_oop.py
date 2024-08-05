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


def main():
    np = NumberProcessor()

    n = int(input("Please enter the number of elements (N): "))
    np.read_numbers(n)

    x = int(input("Please enter the number to search for (X): "))
    result = np.search_number(x)

    if result == -1:
        print("-1")
    else:
        print(f"Number found at position: {result}")

if __name__ == "__main__":
    main()
