matrix = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"Enter row {i + 1}, column {j + 1} data: ")))
    matrix.append(row)

print(matrix)
