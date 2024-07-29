# Ask for input N
N = int(input("Please enter a positive integer: "))

# Read N
print('The number you entered is ' + str(N))

# Initialize an empty list to store the N numbers
numbers = []

# Ask for input N numbers
for i in range(N):
    num = int(input(f"Please enter number {i+1}: "))
    numbers.append(num)

# Read the N Numbers
print('The ' + str(N) + ' numbers you entered:', numbers)

# Ask for input X
X = int(input("Please enter an integer X: "))

# Check if X is in the list of numbers and output the result
if X in numbers:
    # Find the index of X and add 1 to convert to 1-based index
    index = numbers.index(X) + 1
    print(index)
else:
    print(-1)
