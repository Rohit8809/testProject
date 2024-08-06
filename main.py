# Simple Python code to add two numbers

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main part of the program
if __name__ == "__main__":
    # Input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    sum = add_numbers(num1, num2)

    # Print the result
    print(f"The sum of {num1} and {num2} is {sum}")
