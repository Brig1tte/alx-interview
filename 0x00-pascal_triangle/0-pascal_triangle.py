def pascal_triangle(n):
    # Funct returns an empty list if n <= 0
    if n <= 0:
        return []

    # Funct initializes the first row of the triangle
    triangle = [[1]]

    # Funct generates the rest of the triangle
    for a in range(1, n):
        # Funct to initialize the next row with a 1
        next_row = [1]

        # Funct generates the middle numbers of the row
        for b in range(1, a):
            # Middle numbers are the sum of the two numbers above
