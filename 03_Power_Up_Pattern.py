base_number = int(input("Enter a base number: "))
stop_number = int(input("Enter the number to stop at: "))

for power in range(1, stop_number):
    print(power * base_number)