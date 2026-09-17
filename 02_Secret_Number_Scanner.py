user_input = int(input("Enter a number to stop at: "))

for number in range(1, user_input):
    if number % 2 == 0 and number > 10:
        print(f"{number} is an even number greater than 10.")