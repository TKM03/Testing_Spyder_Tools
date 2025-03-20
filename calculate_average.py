# Small project: Calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Avoid division by zero
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

# Test the function
my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average of {my_numbers} is {result}")