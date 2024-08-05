from module5_mod import NumberProcessor

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