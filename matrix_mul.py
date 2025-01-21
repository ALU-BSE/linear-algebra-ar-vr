
# Example arrays
a = [
    [100, 200],
    [300, 400],
    [500, 600]
]

b = [5,10]

# Calculate the result
# Create a matrix of zeros
result = [[0 for _ in range(len(b))] for _ in range(len(a))]

for i in range(len(a)):
  for j in range(len(a[i])):
    result[i][j] = a[i][j] * b[j]
print(result)
