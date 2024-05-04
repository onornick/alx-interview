def pascal_triangle(n):
    triangle = [[1]]
    for row_num in range(1, n):
        # Generate the next row using list comprehension
        row = [1] + [triangle[row_num - 1][j] + triangle[row_num - 1][j + 1] for j in range(row_num - 1)] + [1]
        triangle.append(row)
    return triangle
