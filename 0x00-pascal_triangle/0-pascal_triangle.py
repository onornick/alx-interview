def pascal_triangle(n):
    triangle = []
    for row_num in range(n):
        # Create a new row
        row = [1]  # First element of every row is always 1
        # Fill the row
        for j in range(1, row_num):
            row.append(triangle[row_num - 1][j - 1] + triangle[row_num - 1][j])
        if row_num > 0:
            row.append(1)  # Last element of every row is always 1
        triangle.append(row)
    return triangle
