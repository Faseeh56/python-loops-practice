temperatures = [31, 34, 29, 36, 33, 27, 38, 35, 30, 32]

print("All temperatures:")
print(temperatures)

count_above_35 = 0
print("Temperatures 35 or above:")    
for temp in temperatures:
    if temp >= 35:
        print(temp)
        count_above_35 += 1

print(f"Number of temperatures 35 or above: {count_above_35}")

count_below_30 = 0
for temp in temperatures:
    if temp < 30:
        count_below_30 += 1

print(f"Number of temperatures below 30: {count_below_30}")