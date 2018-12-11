"""
Write a program that asks the user how many Fibonacci numbers to generate and then generates them.

"""


def fibonacci_numbers_recursion(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        prev_elts = fibonacci_numbers_recursion(n - 1)
        prev_elts.append(prev_elts[-1] + prev_elts[-2])
        return prev_elts


def fibonacci_numbers_iterative(n):
    elements = [0, 1]
    if n < 2:
        return elements[:n]

    for i in range(2, n + 1):
        elements.append(elements[-1] + elements[-2])
    return elements


def fibonacci_numbers_using_generator(n):
    elements = [0, 1]
    for i in range(n + 1):
        if i < 2:
            yield elements[i]
        else:
            n_value = elements[-1] + elements[-2]
            yield n_value
            elements[0], elements[1] = elements[1], n_value


how_many = int(input("How many fibonacci numbers? "))
print("Recursion: %s" % fibonacci_numbers_recursion(how_many))
print("Iterative: %s" % fibonacci_numbers_iterative(how_many))
print("Generator: %s" % list(fibonacci_numbers_using_generator(how_many)))
