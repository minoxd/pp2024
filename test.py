import math

# Get student score as input
raw_score = float(input("Enter student score: "))

# Round down to 1-digit decimal using math.floor()
rounded_score = math.floor(raw_score * 10) / 10

# Print the rounded score
print("Rounded down score:", rounded_score)

print(math.floor(0 * 10) / 10)
