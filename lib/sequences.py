#!/usr/bin/env python3

def print_fibonacci(length):
    # If the length is 0, print an empty list
    if length == 0:
        print([])
        return

    # Start with the first two numbers of the Fibonacci sequence
    fib_sequence = [0, 1]

    # If the requested length is 1, only include the first number
    if length == 1:
        print([0])
        return

    # Generate the Fibonacci sequence until it reaches the required length
    while len(fib_sequence) < length:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    # Print the sequence up to the required length
    print(fib_sequence[:length])
