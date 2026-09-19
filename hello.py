def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the sequence with the first two terms
    sequence = [0, 1]
    
    # Loop to calculate the remaining terms
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence

# Example usage: Get the first 10 terms
print(fibonacci_iterative(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

