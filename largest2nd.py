
N = int(input("Enter the number of elements: 
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
if N < 2:
    print("Not enough numbers to find the second largest.")
else:
    # Remove duplicates
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        print("No second largest number exists (all numbers are equal).")
    else:
        unique_numbers.sort(reverse=True) 
        print("The second largest number is:", unique_numbers[1])
