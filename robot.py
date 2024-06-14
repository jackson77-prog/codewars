def robot_transfer(matrix, k):
    # Function to convert "x,y" string to tuple (x, y)
    def parse_point(point):
        return tuple(map(int, point.split(',')))

    n = len(matrix)  # Size of the matrix
    count = 0  # Initialize the count of valid points

    # Iterate over each point in the matrix
    for i in range(n):
        for j in range(n):
            x, y = i, j  # Starting point
            for move in range(k):
                x, y = parse_point(matrix[x][y])  # Move to the next point
                if (x, y) == (i, j) and move < k - 1:
                    # If we return to the start before making k moves, break
                    break
            else:
                # If we complete exactly k moves and return to the start, increment count
                if (x, y) == (i, j):
                    count += 1

    return count  # Return the total count

# Example usage
matrix = [
    ["0,1", "0,0", "1,2"],
    ["1,1", "1,0", "0,2"],
    ["2,1", "2,0", "0,0"]
]
k = 2
print(robot_transfer(matrix, k))  # Output: 8